#!/usr/bin/node
const cmdLineArg = process.argv[2];

if (isNaN(cmdLineArg)) {
  console.log('Not a number');
} else {
  console.log('My number:', parseInt(cmdLineArg));
}
