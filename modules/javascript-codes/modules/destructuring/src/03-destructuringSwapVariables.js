/*
* Rodrigo Leite - Software Engineer
* 20/11/2017
*/

let x = 10;
let y = 20;

console.log(`Valor de x: ${x}, Valor de y: ${y}`); // eslint-disable-line no-console

// Swap com "desestruturação"
[x, y] = [y, x];

console.log(`Valor de x: ${x}, Valor de y: ${y}`); // eslint-disable-line no-console
