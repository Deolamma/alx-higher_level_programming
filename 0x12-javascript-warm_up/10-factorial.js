#!/usr/bin/node

function factorial (number) {
  // If number argument is NaN
  if (Number.isNaN(number)) {
    return 1;
  }
  if (number === 1) {
    return 1;
  } else {
      return (number * factorial(number - 1));
  }
}
console.log(factorial(process.argv[2]));
