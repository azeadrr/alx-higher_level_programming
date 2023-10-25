#!/usr/bin/node

const reqst = require('request');
const apiStarWar = 'https://swapi-api.alx-tools.com/api/films/'.concat(process.argv[2]);
reqst(apiStarWar, (_err, _resp, body) => {
  const res = JSON.parse(body).characters;
  let idx = 0;
  while (idx < res.length) {
    reqst(res[idx], (_charErr, _charResp, charBody) => {
      console.log(JSON.parse(charBody).name);
    });
    idx = idx + 1;
  }
});
