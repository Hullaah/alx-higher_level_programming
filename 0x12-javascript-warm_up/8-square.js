#!/usr/bin/node
const x = parseInt(process.argv[2]);

for (let i = 0; !isNaN(x) && i < x; i++) {
  let hash = '';
  for (let j = 0; j < x; j++) {
    hash += 'X';
  }
  console.log(hash);
}
if (isNaN(x)) {
  console.log('Missing size');
}
