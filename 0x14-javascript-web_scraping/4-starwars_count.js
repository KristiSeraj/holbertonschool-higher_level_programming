#!/usr/bin/node

const axios = require('axios');
let count = 0;

axios.get(process.argv[2])
  .then(function (response) {
    response.data.results.forEach(element => {
      element.characters.forEach(movies => {
        movies.includes('18') ? count++ : count;
      });
    });
    console.log(count);
  })
  .catch(function (error) {
    console.log(error);
  });
