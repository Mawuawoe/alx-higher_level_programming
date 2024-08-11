#!/usr/bin/node

const request = require('request');
const url = process.argv[2];

request(url, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    const data = JSON.parse(body);
    const films = data.results;
    let i = 0;

    for (const film of films) { // Iterate over each film
      if (film.characters.includes('https://swapi-api.alx-tools.com/api/people/18/')) {
        i += 1; // Increment the counter when the character is found
      }
    }

    console.log(i); // Output the count of films featuring the character
  }
});
