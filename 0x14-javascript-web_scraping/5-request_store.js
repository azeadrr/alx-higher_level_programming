#!/usr/bin/node

const reqst = require('request');
const fs = require('fs');
const apiStarWar = process.argv[2];

reqst(apiStarWar, (_err, _resp, body) => {
  fs.writeFile(process.argv[3], body, 'utf8', (err) => {
    if (err) {
      console.log(err);
    }
  });
});
