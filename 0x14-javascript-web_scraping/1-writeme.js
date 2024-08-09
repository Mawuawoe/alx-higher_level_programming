#!/usr/bin/node

// Import the file system module
const fs = require('fs');
// Get the file path from the first command-line argument
const filePath = process.argv[2];
const stringToprint = process.argv[3];

// Read the file content in utf-8 encoding
fs.writeFile(filePath, stringToprint, 'utf8', function (err) {
  if (err) {
    console.error(err); // Print the error object if an error occurred
  }
});
