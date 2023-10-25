#!/usr/bin/node
const reqst = require('request');
reqst(process.argv[2], (err, _resp, body) => {
  if (err) {
    console.log(err);
  } else {
    const tasksDone = {};
    const res = JSON.parse(body);
    let idx = 0;
    while (idx < res.length) {
      const usrId = res[idx].usrId;
      const completed = res[idx].completed;
      if (completed && !tasksDone[usrId]) {
        tasksDone[usrId] = 0;
      }
      if (completed) {
        ++tasksDone[usrId];
      }
      idx = idx + 1;
    }
    console.log(tasksDone);
  }
});
