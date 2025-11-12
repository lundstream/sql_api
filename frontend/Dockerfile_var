FROM node:20-bullseye-slim
WORKDIR /app

# Build-arg för API URL
ARG VITE_API

# Kopiera package.json + package-lock.json
COPY package*.json ./

# Installera dependencies
RUN npm install

# Kopiera resten av frontend-koden
COPY . ./

# Sätt miljövariabeln innan bygg
ENV VITE_API=$VITE_API

# Bygg frontend (Vite ersätter import.meta.env.VITE_API)
RUN npm run build

# Installera serve för att serva dist/
RUN npm install -g serve

EXPOSE 8012

CMD ["serve", "-s", "dist", "-l", "8012"]
