#!/usr/bin/node

exports.esrever = function (list) {
  const newList = [];
  // check if list length is greater than zero
  if (list && (list.length > 0)) {
    // newListIndexNum helps us avoid overflow when reordering list
    let newListIndexNum = list.length - 1;
    list.forEach((item) => {
      newList[newListIndexNum] = item;
      newListIndexNum--;
    });
  } else {
    // Return the list if it is empty or null
    return list;
  }
  return newList;
};
