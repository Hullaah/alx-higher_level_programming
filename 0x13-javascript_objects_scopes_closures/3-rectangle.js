#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.height = h;
      this.width = w;
    }
  }

  print () {
    for (let i = this.height; i > 0; i--) {
      let hash = '';
      for (let j = this.width; j > 0; j--) {
        hash += 'X';
      }
      console.log(hash);
    }
  }
}
module.exports = Rectangle;
