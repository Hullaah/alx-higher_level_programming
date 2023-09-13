#!/usr/bin/node
const secondBiggest = process.argv?.slice(2)
  .map(x => parseInt(x))
  .filter(x => !isNaN(x))
  .filter((x, i, a) => x !== Math.max(...a))
  .find((x, i, a) => x === Math.max(...a));
console.log(secondBiggest || 0);
