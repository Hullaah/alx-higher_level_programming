#!/usr/bin/node
const fs = require('fs');
fs.readFileSync(process.argv[2], 'utf8', (err, data) => console.log(err ?? data));
