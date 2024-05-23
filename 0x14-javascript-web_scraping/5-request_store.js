#!/usr/bin/node

const fs = require('fs');
const request = require('request');

const url = process.argv[2];
const filePath = process.argv[3];

request(url, (error, response, body) => {
  if (!error && response.statusCode === 200) {
    fs.writeFileSync(filePath, body, 'utf-8');
    console.log(`File saved successfully at ${filePath}`);
  } else {
    console.error(`Error: ${error}`);
  }
});
