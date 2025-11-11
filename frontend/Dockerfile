FROM node:20-alpine

WORKDIR /app

# Kopiera och installera dependencies först
COPY package*.json ./
RUN npm install

# Kopiera övriga filer
COPY public/ ./public/
COPY src/ ./src/

# Bygg frontend
ENV NODE_ENV=production
RUN npm run build

# Installera serve för att köra byggda filer
RUN npm install -g serve

EXPOSE 8012
CMD ["serve", "-s", "dist", "-l", "8012"]
