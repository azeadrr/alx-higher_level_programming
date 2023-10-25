#!/usr/bin/node

const reqst = require('request');
const apiStarWar = 'https://swapi-api.alx-tools.com/api/films/'.concat(process.argv[2]);
reqst(apiStarWar, (err, resp, body) => {
  const res = JSON.parse(body);
  console.log(res.title);
});
