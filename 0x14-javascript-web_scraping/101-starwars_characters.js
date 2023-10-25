#!/usr/bin/node

const reqst = require('request');
const apiStarWar = 'https://swapi-api.alx-tools.com/api/films/'.concat(process.argv[2]);
const retv = (array, idx) => {
  if (idx === array.length) return;
  reqst(array[idx], (err, resp, body) => {
    if (err) console.log(err);
    console.log(JSON.parse(body).name);
    retv(array, idx + 1);
  });
};

reqst(apiStarWar, (err, _response, body) => {
  if (err) console.log(err);
  const res = JSON.parse(body).characters;
  retv(res, 0);
});
