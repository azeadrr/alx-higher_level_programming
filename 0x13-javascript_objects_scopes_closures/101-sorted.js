#!/usr/bin/node

const dict = require('./101-data.js').dict;
const newDict = {};

for (const [str, size] of Object.entries(dict)) {
  newDict[size] ? newDict[size].push(str) : (newDict[size] = [str]);
}
console.log(newDict);
