# Desestruturando Objetos

Para entender melhor como funciona a **"Desestruturação de Objetos"**, suponha que tenhamos um objeto de dados para uma determinada pessoa, veja o código abaixo:

```js
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
```

Agora imagine que você precisa salvar essas informações em variáveis, veja o código abaixo:

```js
const name = data.name;
const lastName = data.lastName;
const age = data.age;
const linkTwitter = data.social.twitter;
const linkGithub = data.social.github;
```

**NOTE:**  
Como você pode ver, isso acaba sendo um problema. Uma maneira simples, com uma sintaxe diferente, você verá abaixo:

```js
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
```

Observe que, com apenas algumas linhas, simplificamos nosso código de uma maneira muito mais prática de trabalhar, onde o bloco **{}** recebe as variáveis e passamos a ele o objeto **"employee"**.

**NOTE:**  
> Os nomes das variáveis devem ter o mesmo nome que as propriedades do objeto.

```js
display(eName);
display(eLastName);
display(eAge);
display(eBlog);
display(social.eTwitter);
display(social.eGithub);
```

Você também pode aplicar *desestruturação* em arrays:

```js
function display(data) {
  console.log(data);
}

const arr = ['drigols', 'Software Engineer', 28, 'Goole'];
const [name, job, age, company] = arr; // destructing

display(name);
display(job);
display(age);
display(company);
```

Com a *desestruturação*, também é possível alterar os valores de uma variável sem a necessidade de variáveis temporárias *(temp)*:

```js
let x = 10;
let y = 20;

console.log(`Valor de x: ${x}, Valor de y: ${y}`);

// Swap com "desestruturação"
[x, y] = [y, x];

console.log(`Valor de x: ${x}, Valor de y: ${y}`);
```

---

**Rodrigo Leite -** *Software Engineer*
