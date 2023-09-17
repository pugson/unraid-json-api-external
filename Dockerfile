FROM node:20
WORKDIR /app
COPY package*.json ./
RUN npm install
COPY . .
ENV PORT=3203
EXPOSE $PORT
CMD [ "node", "index.js" ]
