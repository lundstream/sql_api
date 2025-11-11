from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from sqlalchemy import create_engine, MetaData
from sqlalchemy.exc import SQLAlchemyError

app = FastAPI()
engine = None
metadata = None

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount("/static", StaticFiles(directory="frontend/dist"), name="static")

class MSSQLConfig(BaseModel):
    server: str
    database: str
    username: str
    password: str

@app.post("/connect")
def connect_db(config: MSSQLConfig):
    global engine, metadata
    try:
        conn_str = (
            f"mssql+pyodbc://{config.username}:{config.password}"
            f"@{config.server}/{config.database}"
            "?driver=ODBC+Driver+18+for+SQL+Server&TrustServerCertificate=yes"
        )
        engine = create_engine(conn_str)
        metadata = MetaData(bind=engine)
        metadata.reflect()
        return {"status": "connected", "tables": list(metadata.tables.keys())}
    except SQLAlchemyError as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.get("/tables")
def list_tables():
    if metadata is None:
        raise HTTPException(status_code=400, detail="Not connected")
    return {"tables": list(metadata.tables.keys())}

@app.get("/tables/{table_name}")
def get_table(table_name: str):
    if metadata is None:
        raise HTTPException(status_code=400, detail="Not connected")
    if table_name not in metadata.tables:
        raise HTTPException(status_code=404, detail="Table not found")
    table = metadata.tables[table_name]
    with engine.connect() as conn:
        rows = conn.execute(table.select()).fetchall()
    return [dict(row._mapping) for row in rows]
