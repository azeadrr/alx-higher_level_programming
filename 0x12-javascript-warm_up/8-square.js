#!/usr/bin/node

const arg = process.argv[2];
const value = parseInt(arg);
if (!isNaN(value)) {
  for (let index = 0; index < Number(value); index++) {
    let output = '';
    for (let colu = 0; colu < Number(value); colu++) {
      output += 'X';
    }
    console.log(output);
  }
} else { console.log('Missing size'); }
