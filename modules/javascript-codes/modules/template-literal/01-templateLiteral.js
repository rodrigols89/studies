/*
* Rodrigo Leite - Software Engineer
* 19/11/2017
*/

/* eslint-disable */

function display(text) {
  console.log(text); // eslint-disable-line no-console
}


// Creates a "person" object.
const person = {
  name: 'Rodrigo',
  age: 28,
  job: 'Software Engineer',
};


// Concatenates a text with the values of the properties of the "person" object.
const text = "Meu nome: " + person.name + ", idade: " + person.age + ", profissão: " + person.job;
display(text); // Display text.



const textTwo = `Meu nome: ${person.name}, idade: ${person.age}, profissão: ${person.job}`;
display(textTwo); // Display text.
