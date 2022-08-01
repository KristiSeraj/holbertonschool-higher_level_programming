#!/usr/bin/node
const myArg = process.argv.slice(2);
myArg.forEach((val) => {
  console.log(`${val}`);
});
