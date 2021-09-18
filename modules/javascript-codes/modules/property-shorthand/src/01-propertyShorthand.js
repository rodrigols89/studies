/*
* Rodrigo Leite - Software Engineer
* 19/11/2017
*/

/* eslint-disable */

function display(text) {
  console.log(text); // eslint-disable-line no-console
}

const name = 'Rodrigo';
const age = 27;
const job = 'Software Engineer';


// Implementação antiga JavaScript.
const person = {
  name: name,
  age: age,
  job: job,
};
display(person);


// Implementação com ES6.
const personTwo = {
  name,
  age,
  job,
};
display(personTwo);
