#!/usr/bin/node

if (process.argv.length <= 3) { console.log('0'); } else {
  const array = [];
  process.argv.flatMap(function (d) {
    const lr = parseInt(d);
    if (!isNaN(lr)) {
      array.push(lr);
      return lr;
    }
    return 0;
  });
  array.sort((a, b) => a - b);
  console.log(array[array.length - 2]);
}
