#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
request(url, (error, response, body) => {
  if (error);
  const movies = JSON.parse(body);
  const moviesWithWedgeAntilles = movies.results.filter((movie) =>
    movie.characters.some(x => x.includes('18'))
  );
  console.log(moviesWithWedgeAntilles.length);
});
