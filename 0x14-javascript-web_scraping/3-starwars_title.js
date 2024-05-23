#!/usr/bin/node
const request = require('request');

const filmID = process.argv[2];
request('https://swapi-api.hbtn.io/api/films/' + filmID, function (error, response, body) {
  if (error) {
    console.error('error:', error);
  } else {
    console.log(JSON.parse(body).title);
  }
});
