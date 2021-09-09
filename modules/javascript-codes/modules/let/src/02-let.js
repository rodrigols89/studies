/*
* Rodrigo Leite - Software Engineer
* 19/11/2017
*/

function sayAnima(animal) {
  console.log(animal); // eslint-disable-line no-console
}


// let animal = 'Elephant';


/* SECOND SCOPE. */
{
  // Animal variable declared with "let" in the SECOND SCOPE.
  let animal = 'cat';
  sayAnima(animal);

  animal = 'catTwo';
  sayAnima(animal);
}


/* THIRD SCOPE. */
{
  // Animal variable declared  with "let" in THIRD SCOPE.
  let animal = 'dog';
  sayAnima(animal);

  animal = 'dogTwo';
  sayAnima(animal);
}
