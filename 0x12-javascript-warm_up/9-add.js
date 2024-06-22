#!/usr/bin/node

const numbers = process.argv;

function add (a, b) {
  const result = a + b;
  console.log(result);
}

const a = parseInt(numbers[2]);
const b = parseInt(numbers[3]);
add(a, b);
