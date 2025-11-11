FROM python:3.12

# Installera ODBC-drivrutin och nödvändiga verktyg
RUN apt-get update && \
    apt-get install -y curl gnupg2 apt-transport-https unixodbc-dev build-essential && \
    curl https://packages.microsoft.com/keys/microsoft.asc | gpg --dearmor > microsoft.gpg && \
    mv microsoft.gpg /etc/apt/trusted.gpg.d/ && \
    curl https://packages.microsoft.com/config/debian/12/prod.list -o /etc/apt/sources.list.d/mssql-release.list && \
    apt-get update && ACCEPT_EULA=Y apt-get install -y msodbcsql18 && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

# Skapa arbetsmapp
WORKDIR /app

# Installera Python-dependencies
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Kopiera backend-filer
COPY main.py ./

# Exponera port
EXPOSE 8000

# Starta FastAPI
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
