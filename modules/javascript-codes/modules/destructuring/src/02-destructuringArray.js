/*
* Rodrigo Leite - Software Engineer
* 20/11/2017
*/

function display(data) {
  console.log(data); // eslint-disable-line no-console
}

const arr = ['drigols', 'Software Engineer', 28, 'Goole'];
const [name, job, age, company] = arr; // destructing

display(name);
display(job);
display(age);
display(company);
