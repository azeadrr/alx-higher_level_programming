#!/usr/bin/node

const reqst = require('request');
reqst(process.argv[2], (_err, _resp, body) => {
  if (err) {
    console.log(err);
  } else {
    const tskDone = {};
    const res = JSON.parse(body);
    let idx = 0;
    while (idx < res.length) {
      const usrId = res[idx].usrId;
      const cmplt = res[idx].cmplt;
      if (cmplt && !tskDone[usrId]) {
        tskDone[usrId] = 0;
      }
      if (cmplt) {
        ++tskDone[usrId];
      }
      idx += 1;
    }
    console.log(tskDone);
  }
});
