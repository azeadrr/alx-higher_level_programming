#!/usr/bin/node
const fs = require('fs');
fs.readFile(process.argv[2], 'utf8', (err, result) => {
  if (err) {
    console.log(err);
  } else {
    process.stdout.write(result);
  }
});
