FROM node:20-bullseye-slim

WORKDIR /app

# Kopiera package.json + package-lock.json från frontend-mappen
COPY frontend/package*.json ./

# Installera alla dependencies inklusive devDependencies
RUN npm install

# Kopiera resten av frontend-koden
COPY frontend/ ./

# Bygg frontend
RUN npm run build

# Installera serve för att serva dist/
RUN npm install -g serve

EXPOSE 8012

# Starta server för statiska filer
CMD ["serve", "-s", "dist", "-l", "8012"]
