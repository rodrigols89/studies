# Trabalhando com "Property Shorthand"

Vamos ver uma maneira bem interessante de trabalhar na inicialização de objetos:

```js
function display(text) {
  console.log(text);
}

// Valores para possíveis atributos.
const name = 'Rodrigo';
const age = 27;
const job = 'Software Engineer';


// Implementação na versão antiga do JavaScript.
const person = {
  name: name,
  age: age,
  job: job,
};
display(person);
```

**NOTE:**  
Em outras linguagens *(como Java)*, precisamos usar a palavra-chave **"this"** para diferenciar variáveis locais (escopo) de variáveis globais.

Uma coisa interessante sobre o ES6 é que ele permite **omitir o nome das propriedades se elas tiverem o mesmo nome que as variáveis**. Veja o exemplo abaixo:

```js
const personTwo = {
  name,
  age,
  job,
};
display(personTwo);
```

**NOTE:**  
Outra coisa é que no ES6 também podemos **omitir a palavra-chave "função" dentro de um objeto**, veja o exemplo abaixo:

```js
const person = {
  hello() {
    console.log('Hello World!');
  },
};

person.hello();
```

---

**Rodrigo Leite -** *Software Engineer*
