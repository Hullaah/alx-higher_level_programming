#!/usr/bin/node
const fs = require('fs');
const path = require('path');
const file1Path = path.join(process.cwd(), process.argv[2]);
const file2Path = path.join(process.cwd(), process.argv[3]);
const filePath = path.join(process.cwd(), process.argv[4]);
const contents = fs.readFileSync(file1Path, 'utf8') + fs.readFileSync(file2Path, 'utf8');
fs.writeFileSync(filePath, contents);
