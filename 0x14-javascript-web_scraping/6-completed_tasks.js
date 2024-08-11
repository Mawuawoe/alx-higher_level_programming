#!/usr/bin/node

const request = require('request');
const url = process.argv[2]; // API URL passed as the first argument

request(url, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
    return;
  }

  const data = JSON.parse(body);
  const completedTasksByUser = {};

  // Aggregate completed tasks by userId
  data.forEach(task => {
    if (task.completed) {
      if (!completedTasksByUser[task.userId]) {
        completedTasksByUser[task.userId] = 0;
      }
      completedTasksByUser[task.userId] += 1;
    }
  });

  // Print user IDs with completed tasks
  console.log(completedTasksByUser);
});
