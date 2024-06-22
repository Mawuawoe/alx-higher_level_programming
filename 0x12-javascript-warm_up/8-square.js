#!/usr/bin/node

const args = process.argv;
const size = parseInt(args[2]);

if (size) {
  for (let x = 0; x < size; x++) {
    console.log('X'.repeat(size));
  }
} else {
  console.log('Missing size');
}
