FROM node:20-alpine

WORKDIR /app

# Kopiera package.json och package-lock.json först
COPY package*.json ./

# Installera dependencies
RUN npm install

# Kopiera resten av koden
COPY public/ ./public/
COPY src/ ./src/

# Bygg frontend
ENV NODE_ENV=production
RUN npm run build

# Serve byggda filer
RUN npm install -g serve

EXPOSE 8012
CMD ["serve", "-s", "dist", "-l", "8012"]
