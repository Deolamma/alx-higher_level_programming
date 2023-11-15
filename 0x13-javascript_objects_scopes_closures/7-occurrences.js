#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  let count = 0;
  if (list && (list.length > 0)) {
    list.forEach((item) => {
      if (item === searchElement) {
        count++;
      }
    });
    return count;
  }
};
