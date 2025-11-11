FROM node:20-bullseye-slim

WORKDIR /app

# Kopiera package.json + package-lock.json
COPY package*.json ./

# Installera ALLA dependencies inklusive devDependencies
RUN npm install

# Kopiera frontend-koden inklusive vite.config.js
COPY . .

# Bygg frontend
RUN npm run build

# Installera serve för att serva dist/
RUN npm install -g serve

EXPOSE 8012
CMD ["serve", "-s", "dist", "-l", "8012"]
