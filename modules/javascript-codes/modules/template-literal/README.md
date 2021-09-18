# Trabalhando com "Template Literal"

```js
// Função para exibir texto no console.
function display(text) {
  console.log(text);
}

// Cria um objeto pessoa (person)
const person = {
  name: 'Rodrigo',
  age: 28,
  job: 'Software Engineer',
};


// Aplica uma concatenação.
const text = "Meu nome: " + person.name + ", idade: " + person.age + ", profissão: " + person.job;
display(text);
```

Veja como é trabalhoso concatenar esses valores, e a medida que vai aumentando o número de valores (variáveis) fica ainda mais trabalhoso.

#### Tem uma maneira mais simples? Yes - Template Literal

Para codificar usando o Modelo Literal - ES6, NÃO usamos aspas simples **('...')** ou aspas duplas **("...")**. Em vez disso, usamos ***(`...`)***.

Este modelo de codificação ES6 nos permite codificar sem precisar usar o sinal **"+"** para concatenação. Em vez disso, usamos:

```js
${variable}
```

**Exemplo:**  

```js
const textTwo = `Meu nome: ${person.name}, idade: ${person.age}, profissão: ${person.job}`;
display(textTwo);
```

---

**Rodrigo Leite -** *Software Engineer*
