FROM node:20-alpine

WORKDIR /app

# Kopiera package.json och package-lock.json
COPY package*.json ./

# Installera dependencies inklusive devDependencies (plugin-react)
RUN npm install

# Kopiera resten av frontend-koden inklusive vite.config.js
COPY . .

ENV NODE_ENV=production

# Bygg frontend
RUN npm run build

# Installera serve för att serva dist/
RUN npm install -g serve

EXPOSE 8012
CMD ["serve", "-s", "dist", "-l", "8012"]
