/*
* Rodrigo Leite - Software Engineer
* 19/11/2017
*/

function employee(name = 'anonymous', business = 'Google') {
  console.log(`Nome: ${name}, ${business}`); // eslint-disable-line no-console
}


employee();
employee(undefined, 'IBM');
employee('drigols');
employee('Rodrigo', 'Amazon');
