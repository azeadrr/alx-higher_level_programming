#!/usr/bin/node
const reqst = require('request');
const apiStarWar = process.argv[2];
let count = 0;
reqst(apiStarWar, (_err, _resp, body) => {
  const resp = JSON.parse(body).results;
  let idx = 0;
  while (idx < resp.length) {
    const chars = resp[idx].characters;
    let jdx = 0;
    while (jdx < chars.length) {
      const char = chars[jdx];
      const charId = char.split('/')[5];
      count += (charId === '18') ? 1 : 0;
      jdx += 1;
    }
    idx += 1;
  }
  console.log(count);
});
