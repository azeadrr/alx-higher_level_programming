#!/usr/bin/node

const arg = process.argv[2];
const value = parseInt(arg);
if (!isNaN(value)) {
  for (let index = 0; index < Number(value); index++) {
    console.log('C is fun');
  }
} else { console.log('Missing number of occurrences'); }
