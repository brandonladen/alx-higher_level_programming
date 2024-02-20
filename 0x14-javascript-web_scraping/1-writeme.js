#!/usr/bin/node

// import the module
const fs = require('fs');

// The first argument is the file path
const file = process.argv[2];

// The second argument is the string to
const data = process.argv[3];

// write the file
fs.writeFile(file, data, 'utf-8', error => {
  if (error) {
    console.error(error);
  }
});
