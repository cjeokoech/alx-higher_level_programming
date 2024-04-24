#!/usr/bin/node

const request = require('request');
const starWar = 'https://swapi-api.hbtn.io/api/films/'.concat(process.argv[2]);

request(starwar, function (error, req, body) {
  const characters = JSON.parse(body).characters;

  for (let i = 0; i < characters.length; ++1) {
    request(characters[i], function (charError, charReq, charBody) {
      console.log(JSON.parse(charBody).name;
    });
  }
});
