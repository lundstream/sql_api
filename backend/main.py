from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from sqlalchemy import create_engine, MetaData, Table, select
from sqlalchemy.exc import SQLAlchemyError

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class MSSQLConfig(BaseModel):
    server: str
    database: str
    username: str
    password: str

@app.post("/connect")
def connect_db(config: MSSQLConfig):
    """
    Anslut till SQL Server med dynamiska parametrar.
    Returnerar tabeller eller error.
    """
    try:
        conn_str = (
            f"mssql+pyodbc://{config.username}:{config.password}"
            f"@{config.server}/{config.database}"
            "?driver=ODBC+Driver+18+for+SQL+Server&TrustServerCertificate=yes"
        )
        engine = create_engine(conn_str)
        metadata = MetaData()
        metadata.reflect(bind=engine)
        tables = list(metadata.tables.keys())
        return {"status": "connected", "tables": tables}
    except SQLAlchemyError as e:
        return {"status": "error", "detail": str(e)}
    except Exception as e:
        return {"status": "error", "detail": str(e)}

@app.post("/tables/{table_name}")
def get_table(table_name: str, config: MSSQLConfig):
    """
    Hämtar data från en specifik tabell med dynamiska credentials.
    """
    try:
        conn_str = (
            f"mssql+pyodbc://{config.username}:{config.password}"
            f"@{config.server}/{config.database}"
            "?driver=ODBC+Driver+18+for+SQL+Server&TrustServerCertificate=yes"
        )
        engine = create_engine(conn_str)
        metadata = MetaData()
        metadata.reflect(bind=engine)
        if table_name not in metadata.tables:
            return {"status": "error", "detail": "Table not found"}
        table = metadata.tables[table_name]
        with engine.connect() as conn:
            rows = conn.execute(select(table)).all()
        return [dict(row._mapping) for row in rows]
    except Exception as e:
        return {"status": "error", "detail": str(e)}
