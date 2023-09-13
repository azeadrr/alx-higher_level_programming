#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let index = 0; index < this.height; index++) {
      let ph = '';
      for (let inf = 0; inf < this.width; inf++) {
        ph += 'X';
      }
      console.log(ph);
    }
  }
}
