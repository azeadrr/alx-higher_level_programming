#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) { [this.width, this.height] = [w, h]; }
  }
  print () {
    for (let i = 0; i < this.height; i++) {
      let ph = '';
      for (let inf = 0; inf < this.width; inf++) {
        ph += 'X';
      }
      console.log(ph);
    }
  }

  rotate () {
    this.width = this.height;
    this.height = this.width;
  }

  double () {
    this.height = this.height * 2;
    this.width = this.width * 2;
  }
}
module.exports = Rectangle;
