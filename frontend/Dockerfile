FROM node:20-alpine

WORKDIR /app

# Kopiera package.json först och installera dependencies
COPY package*.json ./
RUN npm install

# Kopiera resten av frontend-koden (inkl. src och public)
COPY . .

ENV NODE_ENV=production
RUN npm run build

RUN npm install -g serve

EXPOSE 8012
CMD ["serve", "-s", "dist", "-l", "8012"]
