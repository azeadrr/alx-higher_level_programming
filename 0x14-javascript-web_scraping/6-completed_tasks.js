#!/usr/bin/node

const reqst = require('request');
reqst(process.argv[2], (err, _resp, body) => {
  if (err) {
    console.log(err);
  } else {
    const tskDone = {};
    const res = JSON.parse(body);
    let idx = 0;
    while (idx < res.length) {
      const userId = res[idx].userId;
      const cmplt = res[idx].cmplt;
      if (cmplt && !tskDone[userId]) {
        tskDone[userId] = 0;
      }
      if (cmplt) {
        ++tskDone[userId];
      }
      idx += 1;
    }
    console.log(tskDone);
  }
});
