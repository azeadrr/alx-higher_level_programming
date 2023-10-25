#!/usr/bin/node
const fs = require('fs');
fs.readFile(process.argv[2], 'utf8', (error, result) => {
	if (error) {
    console.log(error);
  } else {
    process.stdout.write(result);
  }
});
