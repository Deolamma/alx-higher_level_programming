#!/usr/bin/node
class Rectangle {
// creating constructor of a class
  constructor (w, h) {
    // if constructor args is 0 or less
    // create a class with default constructor
    if (w > 0 && Number.isInteger(w) && h > 0 && Number.isInteger(h)) {
      this.width = w;
      this.height = h;
    }
  }
}
module.exports = Rectangle;
