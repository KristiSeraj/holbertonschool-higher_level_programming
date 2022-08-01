#!/usr/bin/node
const myArgs = process.argv.slice(1);
let len = 0;
while (myArgs[len] !== undefined) {
  len++;
}
if (len === 1) {
  console.log('No argument found');
} else {
  let j = 1;
  while (j < len) {
    console.log(myArgs[j]);
    j++;
  }
}
