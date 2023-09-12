#!/usr/bin/node

const arg = process.argv[2];
const value = parseInt(arg);
if (!isNaN(value)) { console.log(`${fact(Number(value))}`); } else { console.log(1); }

function fact (num) {
	  if (num === 0) { return 1; } else { return (num * fact(num - 1)); }
}
