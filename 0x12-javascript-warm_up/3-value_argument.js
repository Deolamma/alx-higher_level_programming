#!/usr/bin/node
const myArr = process.argv.slice(2);
let arrLen = 0;

myArr.forEach(() => {
  arrLen++;
});

if (arrLen === 0) {
  console.log('No argument');
} else {
  for (const element of myArr) {
    console.log(element);
  }
}
