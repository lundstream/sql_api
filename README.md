# MSSQL REST API Viewer

## Översikt
Detta projekt är ett komplett system för att ansluta till och läsa data från en Microsoft SQL Server via ett REST API och visa resultatet i ett modernt webbgränssnitt.  
Systemet består av tre huvuddelar:

1. **MSSQL-databas (Docker-container för test)**
2. **FastAPI-backend (Python)**
3. **React-frontend (Vite)**

------------------------------------------------------------------------------------------

## Arkitektur

[React/Vite Frontend]
|
v
HTTP (fetch)
|
v
[FastAPI Backend] ---> [SQLAlchemy + pyodbc] ---> [MSSQL Server]
|
v
JSON-respons tillbaka till frontend

## 1. MSSQL-databas

### Containerkonfiguration
Exempel på Portainer-konfiguration:

- **Image:** `mcr.microsoft.com/mssql/server:2022-latest`
- **Port:** `1433`
- **Environment:**
  ```env
  ACCEPT_EULA=Y
  MSSQL_SA_PASSWORD=YourStrong!Passw0rd
  MSSQL_PID=Developer
Databasexempel: TestDB

Exempel på tabeller:
Products
Users

Exempel på SQL för att skapa tabeller:
```
CREATE TABLE Products (
    Id INT PRIMARY KEY IDENTITY,
    Name NVARCHAR(50),
    Price DECIMAL(10,2)
);

INSERT INTO Products (Name, Price)
VALUES ('Keyboard', 299.00), ('Mouse', 199.00);

CREATE TABLE Users (
    Id INT PRIMARY KEY IDENTITY,
    Username NVARCHAR(50),
    Email NVARCHAR(100)
);

INSERT INTO Users (Username, Email)
VALUES ('admin', 'admin@test.com'), ('user1', 'user1@test.com');
```
## 2. FastAPI-backend
Syfte
Tillhandahåller ett REST API som frontend eller externa klienter (t.ex. PowerShell) kan anropa för att:
Ansluta till valfri MSSQL-databas
Lista tabeller
Hämta tabellinnehåll i JSON-format

Teknologier
FastAPI
SQLAlchemy
pyodbc
pydantic
uvicorn

Viktiga endpoints

POST /connect
Input:
```
{
  "server": "192.168.1.20,1433",
  "database": "TestDB",
  "username": "sa",
  "password": "YourStrong!Passw0rd"
}
Respons:
{
  "status": "connected",
  "tables": ["Products", "Users"]
}
```
POST /tables/{table_name}
Input:
```
{
  "server": "192.168.1.20,1433",
  "database": "TestDB",
  "username": "sa",
  "password": "YourStrong!Passw0rd"
}
Respons:
[
  {"Id": 1, "Name": "Keyboard", "Price": 299.00},
  {"Id": 2, "Name": "Mouse", "Price": 199.00}
]
```

Exempel på PowerShell-anrop
### Anslut till server
```
$body = @{
    server = "192.168.1.20,1433"
    database = "TestDB"
    username = "sa"
    password = "YourStrong!Passw0rd"
} | ConvertTo-Json

Invoke-RestMethod -Uri "http://192.168.1.20:8011/connect" -Method POST -Body $body -ContentType "application/json"
```

### Hämta tabell
```
Invoke-RestMethod -Uri "http://192.168.1.20:8011/tables/Products" -Method POST -Body $body -ContentType "application/json"
```
## 3. React-frontend (Vite)
Syfte
Ger ett enkelt gränssnitt för att ange anslutningsuppgifter, lista tabeller och visa data.

Teknologier
React 18
Vite
Fetch API
useState (React Hooks)

Flöde
Användaren anger:
Serveradress (ex. 192.168.1.20:1433)
Databasnamn (TestDB)
Användare (sa)
Lösenord
Klickar Anslut
Gör POST /connect
Backend returnerar tabellnamn
Klick på tabell
Gör POST /tables/{tabell}
Data returneras som JSON och visas i tabellformat

## 4. Körning
Backend
```
uvicorn main:app --host 0.0.0.0 --port 8011
```
Frontend
```
npm run dev
```

URL:er
Backend API: http://192.168.1.20:8011

Frontend (Vite dev): http://192.168.1.20:8012 eller containerport

## 5. Sammanfattning
|Del	            |Tekniker	                      |Syfte
|-----------------|-------------------------------|--------------------------
|Databas	        |MSSQL (Docker)	                |Lagrar tabeller och data
|Backend	        |FastAPI, SQLAlchemy, pyodbc	  |REST API mot MSSQL
|Frontend	        |React, Vite	                  |Visar tabeller och data

Kommunikation: JSON via HTTP	API mellan frontend och backend

Systemet är helt dynamiskt: det kräver inga fördefinierade databasanslutningar i koden – användaren matar in uppgifterna i gränssnittet och backend ansluter live.

## 6. Vidare utveckling
- Lägg till CRUD-stöd (INSERT, UPDATE, DELETE)
- Autentisering via JWT-token
- Serverlista / favoriter i frontend
- Exportera data till CSV/Excel
- Loggning med uvicorn + rotating file handler

