# Trabalhando com “const”

> Com a palavra-chave **"const"**, você pode criar uma variável que não permita alterar seus valores (veremos mais adiante que isso não é verdade)

```js
function sayName(name) {
  console.log(name); // eslint-disable-line no-console
}
 
const name = 'Rodrigo Leite da Silva';
sayName(name);
```

Veja que nós temos uma função que exibe o nome no console e uma variávle nome (name). Mas o que acontece se tentarmos reatribuir o valor dessa constante?

```js
name = 'drigols';
```

**Outpu:**  
```
16:1  error  'name' is constant           no-const-assign
```

#### Etapa 01: cria (ou tenta criar) um objeto constante com a palavra-chave "const".

```js
const person = {
  name: 'Rodrigo',
  age: 28,
};
```

#### Etapa 02 - Exibe os valores e propriedades do objeto "pessoa".

```js
sayPerson(person);
```

#### Etapa 03 - Altera os valores das propriedades do objeto "pessoa".

```js
person.name = 'drigols - Software Engineer';
person.age = 15;
sayPerson(person);
```

#### Etapa 04 - Exibe os novos valores das propriedades do objeto "pessoa"

```js
/*
* { name: 'Rodrigo', age: 28 }
* { name: 'drigols - Software Engineer', age: 15 }
*/
```

Como você pode ver, alteramos os valores das propriedades de um objeto, mesmo com a palavra-chave **"const"**.

Portanto, resolver esse problema é muito simples. Você simplesmente congela o objeto com a função **freeze()** do objeto "Objeto".

```js
// Freeze the Object.
Object.freeze(person);
```

#### Step 06 - Agora tente altera os valores das propriedades do objeto "pessoa".

```js
// Agora você pode ver que o objeto está imutável.
person.name = 'Rodrigo';
person.age = 10;
sayPerson(person);

{ name: 'Rodrigo', age: 28 }
{ name: 'drigols - Software Engineer', age: 15 }
{ name: 'drigols - Software Engineer', age: 15 }
```

**NOTE:**  
Como você pode ver agora, criamos um objeto imutável.

---

**Rodrigo Leite -** *Software Engineer*
