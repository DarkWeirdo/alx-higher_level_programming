#!/usr/bin/node
'use strict';

function add (a, b) {
  if (isNaN(a) || isNaN(b)) {
    console.log('Error: One or both arguments are not numbers.');
  } else {
    const sum = Number(a) + Number(b);
    console.log(sum);
  }
}
