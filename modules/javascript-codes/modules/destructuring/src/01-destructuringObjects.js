/*
* Rodrigo Leite - Software Engineer
* 20/11/2017
*/

/* eslint-disable */

function display(data) {
  console.log(data);
}

const data = {
  name: 'Rodrigo',
  lastName: 'Silva',
  age: 28,
  blog: 'https://drigols.github.io/',
  social: {
    twitter: 'https://twitter.com/drigols_code',
    github: 'https://github.com/drigols',
  },
};

const name = data.name;
const lastName = data.lastName;
const age = data.age;
const linkTwitter = data.social.twitter;
const linkGithub = data.social.github;

const employee = {
  eName: 'drigols',
  eLastName: 'Silva',
  eAge: 28,
  eBlog: 'https://drigols.github.io/',
  social: {
    eTwitter: 'https://twitter.com/drigols_code',
    eGithub: 'https://github.com/drigols',
  },
};

const {
  eName, eLastName, eAge, eBlog, social,
} = employee;

display(eName);
display(eLastName);
display(eAge);
display(eBlog);
display(social.eTwitter);
display(social.eGithub);
