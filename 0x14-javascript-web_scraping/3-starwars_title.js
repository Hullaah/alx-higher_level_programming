#!/usr/bin/node
const request = require('request');
const url = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];
request(url, (error, response, body) => {
  if (!error) {
    const movie = JSON.parse(body);
    console.log(movie.title);
  }
});
