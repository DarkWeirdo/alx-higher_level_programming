#!/usr/bin/node
const request = require('request');

const apiUrl = process.argv[2];
const characterId = 18;
let count = 0;

request(apiUrl, function (error, response, body) {
  if (!error && response.statusCode === 200) {
    const films = JSON.parse(body).results;

    films.forEach(film => {
      const characters = film.characters;
      if (characters.includes(`https://swapi-api.alx-tools.com/api/people/${characterId}/`)) {
        count++;
      }
    });

    console.log(count);
  } else {
    console.log('Error fetching data from the API');
  }
});
