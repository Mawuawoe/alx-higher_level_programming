#!/usr/bin/node

const args = process.argv;
const arg1 = parseInt(args[2]);

if (arg1) {
  for (let x = 0; x < arg1; x++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}
