#!/usr/bin/node
const request = require('request');
const url = 'https://swapi-api.alx-tools.com/api/films/';
const id = parseInt(process.argv[2], 10);
request(url, (error, response, body) => {
  if (error);
  const movies = JSON.parse(body);
  movies.results[id - 1].characters.forEach(character => {
    request(character, (error, response, body) => {
      if (error);
      const characterObj = JSON.parse(body);
      console.log(characterObj.name);
    });
  });
});
