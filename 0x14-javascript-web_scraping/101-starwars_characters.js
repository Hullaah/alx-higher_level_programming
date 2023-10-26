#!/usr/bin/node
const request = require('request');
const url = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];
request(url, (error, response, body) => {
  if (error);
  const movie = JSON.parse(body);
  movie.characters.forEach(character => {
    request(character, (error, response, body) => {
      if (error);
      const characterObj = JSON.parse(body);
      console.log(characterObj.name);
    });
  });
});
