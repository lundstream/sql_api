FROM node:20-alpine

WORKDIR /app

# Kopiera package.json och package-lock.json
COPY package*.json ./

# Installera dependencies inklusive @vitejs/plugin-react
RUN npm install

# Kopiera resterande frontend-kod
COPY . .

ENV NODE_ENV=production
RUN npm run build

RUN npm install -g serve

EXPOSE 8012
CMD ["serve", "-s", "dist", "-l", "8012"]
