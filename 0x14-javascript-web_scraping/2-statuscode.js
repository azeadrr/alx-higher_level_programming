#!/usr/bin/node

const reqst = require('request');
reqst(process.argv[2], (_err, resp) => {
  console.log('code:', resp.statusCode);
});
