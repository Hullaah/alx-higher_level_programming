#!/usr/bin/node
const dict = require('./101-data.js').dict;
const newDict = {};
for (const [k, v] of Object.entries(dict)) {
  if (newDict[v]) {
    newDict[v].push(k);
  } else {
    newDict[v] = Array.of(k);
  }
}
console.log(newDict);
