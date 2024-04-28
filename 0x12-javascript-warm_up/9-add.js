#!/usr/bin/node
'use strict';

function add (a, b) {
  if (isNaN(a) || isNaN(b)) {
    console.log('NaN');
  } else {
    const sum = Number(a) + Number(b);
    console.log(sum);
  }
}

// Example usage from command line arguments
const args = process.argv.slice(2); // Skip the first two elements
add(args[0], args[1]);
