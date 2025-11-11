FROM node:20-bullseye-slim

WORKDIR /app

# Build-arg för API URL
ARG VITE_API
ENV VITE_API=${VITE_API}

# Kopiera package.json + package-lock.json
COPY package*.json ./

# Installera dependencies
RUN npm install

# Kopiera resten av frontend-koden
COPY . .

# Bygg frontend
RUN npm run build

# Installera serve för att serva dist/
RUN npm install -g serve

EXPOSE 8012

# Starta server för statiska filer
CMD ["serve", "-s", "dist", "-l", "8012"]
