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
      const userId = res[idx].userId;
      const completed = res[idx].completed;
      if (completed && !tasksDone[userId]) {
        tasksDone[userId] = 0;
      }
      if (completed) {
        ++tasksDone[userId];
      }
      idx = idx + 1;
    }
    console.log(tasksDone);
  }
});
