#!/usr/bin/node

const a = process.argv[2];
const b = process.argv[3];
const value1 = parseInt(a);
const value2 = parseInt(b);
if (!isNaN(value1) && !isNaN(value2)) {
  console.log(Number(value1) + Number(value2));
} else { console.log(NaN); }
