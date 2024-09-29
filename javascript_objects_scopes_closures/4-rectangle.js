#!/usr/bin/node

class Rectangle {
  constructor(w, h) {
    if (w <= 0 || h <= 0 || !Number.isInteger(w) || !Number.isInteger(h)) {
      // Create an empty object if w or h is 0 or not a positive integer
      return {};
    }
    this.width = w;  // Initialize the width
    this.height = h; // Initialize the height
  }

  print() {
    for (let i = 0; i < this.height; i++) {
      console.log('X'.repeat(this.width)); // Print the rectangle using 'X'
    }
  }

  rotate() {
    const temp = this.width;  // Store the width in a temporary variable
    this.width = this.height;  // Swap width and height
    this.height = temp;        // Assign the stored width to height
  }

  double() {
    this.width *= 2;           // Double the width
    this.height *= 2;          // Double the height
  }
}

module.exports = Rectangle; // Export the Rectangle class

