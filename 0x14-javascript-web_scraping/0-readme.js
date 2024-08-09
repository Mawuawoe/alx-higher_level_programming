#!/usr/bin/node

// Import the file system module
const fs = require('fs');
// Get the file path from the first command-line argument
const filePath = process.argv[2];

// Read the file content in utf-8 encoding
fs.readFile(filePath, 'utf8', function (err, data) {
  if (err) {
    console.error(err); // Print the error object if an error occurred
    return;
  }
  console.log(data); // Print the content of the file
});
