FROM node:20-alpine

WORKDIR /app

COPY frontend/package*.json ./
RUN npm install

COPY frontend/public/ ./public/
COPY frontend/src/ ./src/

ENV NODE_ENV=production
RUN npm run build

RUN npm install -g serve

EXPOSE 8012
CMD ["serve", "-s", "dist", "-l", "8012"]
