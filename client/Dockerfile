FROM node:lts-alpine

RUN npm install -g http-server

WORKDIR /usr/src/front

COPY . .

EXPOSE 8080

CMD [ "http-server"]