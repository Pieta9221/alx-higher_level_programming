#!/usr/bin/node
function add (a, b) {
  return a + b;
}
const n = parseInt(process.argv[2]);
const m = parseInt(process.argv[3]);
console.log(add(n, m));
