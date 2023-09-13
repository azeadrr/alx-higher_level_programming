#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }
  print () {
    for (let i = 0; i < this.height; i++) {
      let ph = '';
      for (let vl = 0; vl < this.width; vl++) {
        ph += 'X';
      }
      console.log(ph);
    }
  }
  rotate () {
    const both = this.height;
    this.height = this.width;
    this.width = both;
  }
  double () {
    this.height = this.height * 2;
    this.width = this.width * 2;
  }
}
module.exports = Rectangle;
