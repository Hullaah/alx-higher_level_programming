#!/usr/bin/node
const x = parseInt(process.argv[2]);
let i = 0;
while (!isNaN(x) && i !== x) {
  console.log('C is fun');
  i++;
}
if (isNaN(x)) {
  console.log('Missing number of occurrences');
}
