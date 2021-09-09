/*
* Rodrigo Leite - Software Engineer
* 19/11/2017
*/

function sayPerson(person) {
  console.log(person); // eslint-disable-line no-console
}


// Step - 01: Creates(tries) a constant object with the keyword "const".
const person = {
  name: 'Rodrigo',
  age: 28,
};
sayPerson(person); // Step 02 - Display the values and properties of the "person" object.


// Step 03 - Changes the values of the properties of the "person" object.
person.name = 'drigols - Software Engineer';
person.age = 15;
sayPerson(person); // Step 04 - Displays the new values of the properties of the "person" object
/*
* { name: 'Rodrigo', age: 28 }
* { name: 'drigols - Software Engineer', age: 15 }
*/

Object.freeze(person); // Step 05 - Freeze the object "person".


// Step 06 - Tries changes the values of the properties of the "person" object.
person.name = 'Rodrigo';
person.age = 10;
sayPerson(person); // Displays the values of the properties of the "person" object
/*
* { name: 'drigols - Software Engineer', age: 15 }
* As you can now see yes we have a created an immutable object.
*/
