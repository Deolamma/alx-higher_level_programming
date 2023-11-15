#!/usr/bin/node

exports.converter = function (base) {
  // convertToBase is a recursive function that does the binary conversion
  function convertToBase (n) {
    if (n < base) {
      return n.toString(base);
    } else {
      return convertToBase(Math.floor(n / base)) + (n % base).toString(base);
    }
  }
  // This is the function that is returned from the converter function
  return function (number) {
    if (typeof number !== 'number' || isNaN(number) || number < 0) {
      return 'Invalid input';
    }
    // This function returns convertToBase
    return convertToBase(number);
  };
};
