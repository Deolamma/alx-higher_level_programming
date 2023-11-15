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

  print () {
    for (let i = 0; i < this.height; i++) {
      for (let j = 0; j < this.width; j++) {
        process.stdout.write('X');
      }
      console.log();
    }
  }
  
  rotate () {
     let temp = this.width;
     this.width = this.height;
     this.height = temp;
  }
  
  double () {
     this.width *= 2;
     this.height *= 2;
  }
}
module.exports = Rectangle;
