#!/usr/bin/node
const request = require('request');

const apiUrl = process.argv[2];

request(apiUrl, (error, response, body) => {
  if (!error && response.statusCode === 200) {
    const todos = JSON.parse(body);

    const completedTasks = todos.filter(todo => todo.completed);

    const completedTasksCount = completedTasks.reduce((acc, todo) => {
      acc[todo.userId] = (acc[todo.userId] || 0) + 1;
      return acc;
    }, {});

    console.log(completedTasksCount);
  } else {
    console.log('Error fetching data from the API');
  }
});
