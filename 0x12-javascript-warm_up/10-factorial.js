#!/usr/bin/node

const args = process.argv;

const number = parseInt(args[2]);

function factorial (n) {
  if (args.length < 3) {
    return 1;
  }
  if (n === 0 || n === 1) {
    return 1;
  } else {
    return n * factorial(n - 1);
  }
}

console.log(factorial(number));
