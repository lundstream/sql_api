FROM python:3.12

# Installera ODBC-drivrutin och byggverktyg
RUN apt-get update && \
    apt-get install -y curl gnupg2 unixodbc-dev build-essential python3-dev && \
    curl https://packages.microsoft.com/keys/microsoft.asc | gpg --dearmor > microsoft.gpg && \
    mv microsoft.gpg /etc/apt/trusted.gpg.d/ && \
    curl https://packages.microsoft.com/config/ubuntu/22.04/prod.list -o /etc/apt/sources.list.d/mssql-release.list && \
    apt-get update && ACCEPT_EULA=Y apt-get install -y msodbcsql18 && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Kopiera och installera Python-dependencies
COPY backend/requirements.txt ./
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# Kopiera backend-koden
COPY backend ./backend

EXPOSE 8011

# Starta backend via uvicorn
CMD ["uvicorn", "backend.main:app", "--host", "0.0.0.0", "--port", "8011"]
