#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
request(url, (error, response, body) => {
  if (error);
  const todos = JSON.parse(body);
  const tasksCompleted = {};
  todos.forEach(element => {
    tasksCompleted[element.userId] = (tasksCompleted[element.userId] ?? 0) + element.completed;
  });
  console.log(tasksCompleted);
});
