FROM node:20-alpine

WORKDIR /app

# Kopiera package.json + package-lock.json
COPY package*.json ./

# Installera ALLA dependencies (inkl. devDependencies)
RUN npm install

# Kopiera resten av koden inklusive vite.config.js
COPY . .

# Bygg frontend
RUN npm run build

# Installera serve för att serva dist/
RUN npm install -g serve

EXPOSE 8012
CMD ["serve", "-s", "dist", "-l", "8012"]
