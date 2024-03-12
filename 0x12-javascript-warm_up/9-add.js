#!/usr/bin/node

function add (a, b) {
  const sum = a + b;

  console.log(sum);
}
const a = parseInt(process.argv[2]);
const b = parseInt(process.argv[3]);

if (isNaN(a) || isNaN(b)) {
  console.log('Arguments are not integer');
} else {
  add(a, b);
}
