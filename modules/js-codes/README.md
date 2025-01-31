# JavaScript

## Contents

 - [**let**](#intro-to-let)
   - [let shadowing](#let-shadowing)
   - [Illegal shadowing](#illegal-shadowing)
 - [**const**](#intro-to-const)
   - [const and immutable objects](#const-and-immutable-objects)
 - [**Arrow Functions**](#arrow-functions)
 - [**REFERENCES**](#ref)
<!---
[WHITESPACE RULES]
- Same topic = "10" Whitespace character.
- Different topic = "50" Whitespace character.
--->




















































<!--- ( let ) --->

---

<div id="intro-to-let"></div>

## let

Variáveis declaradas com **"let"**:

 - Podem ter seus valores reatribuídos no mesmo escopo;
 - Mas não podem ser redeclaradas no mesmo escopo. 

Por exemplo:

[let-01.js](src/let-01.js)
```js
let x = 10;
x = 20;  // ✅ Permitido (reatribuição de valor)

let x = 30; // ❌ Erro: Identifier 'x' has already been declared
```

**OUTPUT:**
```bash
SyntaxError: Identifier 'x' has already been declared
```

Vejam que no exemplo acima nós:

 - ✅ Reatribuimos o valor de x para 20;
 - ❌ Mas se declararmos outra variável com o mesmo nome no mesmo escopo, isso acaba gerando um erro.










---

<div id="let-shadowing"></div>

## let Shadowing

> Visto que uma variável declarada como **"let"** não pode ser declarada novamente no mesmo escopo o código abaixo resultará em um erro?

[let-02.js](src/let-02.js)
```js
function sayAnima(animal) {
  console.log(animal);
}

// Global SCOPE.
let animal = "Elephant";

/* SECOND SCOPE. */
{
  // Animal variable declared with "let" in the SECOND SCOPE.
  let animal = "cat";
  sayAnima(animal);

  animal = "catTwo";
  sayAnima(animal);
}

/* THIRD SCOPE. */
{
  // Animal variable declared  with "let" in THIRD SCOPE.
  let animal = "dog";
  sayAnima(animal);

  animal = "dogTwo";
  sayAnima(animal);
}
```

Bem, nós temos uma variável **"let"** declarada globalmente o que significa que ela está disponível no escopo global.

Vamos testar:

**OUTPUT:**  
```bash
cat
catTwo
dog
dogTwo
```

> **What?**  
> Bem, isso é o que nós conhecemos como ***"Shadowing"***.

#### 🔹 Como funciona o "sombreamento" (shadowing)?

Se uma variável for declarada dentro de um escopo interno com o `mesmo nome` de uma declarada anterior em um escopo global, essa nova variável vai substituir temporariamente a variável global dentro daquele escopo.

> **NOTE:**  
> O escopo global continua existindo, mas a variável (let) dentro do bloco se refere apenas à variável do bloco.










---

<div id="illegal-shadowing"></div>

## Illegal Shadowing

So, if we try to shadow let variable by var variable, it is known as **"Illegal Shadowing"** and it will give the error as “variable is already defined.” 

For example:

[illegal-shadowing.js](src/illegal-shadowing.js)
```js
function func() {
    var a = "Geeks";
    let b = "Geeks";

    if (true) {
        let a = "GeeksforGeeks"; // Legal Shadowing
        var b = "Geeks"; // Illegal Shadowing
        console.log(a); // It will print 'GeeksforGeeks'
        console.log(b); // It will print error
    }
}
func();
```

**OUTPUT:**
```bash
SyntaxError: Identifier 'b' has already been declared
```

> **NOTES:**  
> Vejam que diferente de antes onde nós podíamos ter uma variável de bloco (interna) com o mesmo nome de uma variável global, quando estamos quando uma variável com a palavra reservada **"var"** isso não é possível.





















































<!--- ( const ) --->

---

<div id="intro-to-const"></div>

## const

> Com a palavra-chave **"const"**, podemos criar uma variável que não permita alterar seus valores (veremos mais adiante que isso não é verdade)

Por exemplo:

[const-01.js](src/const-01.js)
```js
function sayName(name) {
    console.log(name);
}

const myName = "Rodrigo Leite da Silva";
sayName(myName);

// Error!
myName = 'drigols';
```

**OUTPUT:**
```bash
name = 'drigols';
     ^

TypeError: Assignment to constant variable.
```










---

<div id="const-and-immutable-objects"></div>

## const and immutable objects

Imagine that we have a constant object with the keyword **"const"**:

[const-02.js](src/const-02.js)
```js
function sayPerson(person) {
    console.log(person);
}

const person = {
    name: "Rodrigo",
    age: 28,
};
sayPerson(person);
```

**OUTPUT:**
```bash
{ name: 'Rodrigo', age: 28 }
```

Now, the question is:

> **"Can we change the values of the properties of the object?"**

Let's try:

[const-02.js](src/const-02.js)
```js
function sayPerson(person) {
    console.log(person);
}

const person = {
    name: "Rodrigo",
    age: 28,
};
sayPerson(person);


person.name = "drigols - Software Engineer";
person.age = 15;
sayPerson(person);
```

**OUTPUT:**
```bash
{ name: 'Rodrigo', age: 28 }
{ name: 'drigols - Software Engineer', age: 15 }
```

> **What?**  
> Yes, we can change the values of the properties of the object.

To solva that problem, we need to freeze the object with the function **freeze()** of the object "Object".

[const-02.js](src/const-02.js)
```js
function sayPerson(person) {
    console.log(person);
}

const person = {
    name: "Rodrigo",
    age: 28,
};
sayPerson(person);

person.name = "drigols - Software Engineer";
person.age = 15;
sayPerson(person);

// Freeze the object "person".
Object.freeze(person);

person.name = "Rodirgo Santoro";
person.age = 50;
sayPerson(person);
```

**OUTPUT:**
```bash
{ name: 'Rodrigo', age: 28 }
{ name: 'drigols - Software Engineer', age: 15 }
{ name: 'drigols - Software Engineer', age: 15 }
```

> **NOTE:**  
> See that now we can't change the values of the properties of the object.





















































<!--- ( Arrow Functions ) --->

---

<div id="arrow-functions"></div>

## Arrow Functions

Para criar uma Arrow Functions nós:

 - **1st) -** Transformamos a função em uma variável adicionando:
   - `const (mais recomendado)`, `let` ou `var`.
 - **2nd) -** Removemos a palavra-chave `function`;
 - **2º) -** Adicionamos a seta após os parâmetros.

Por exemplo, veja a função abaixo:

```js
function display(result) {
    console.log(result);
}
```

Agora vamos transformar ela em uma Arrow Function:

```js
const display = (result) => {
    console.log(result);
};
```

Parênteses não são necessários se apenas uma expressão (instrução) estiver presente no mesmo bloco:

```js
const display = (result) => console.log(result);

display(10);
```

**OUTPUT:**
```bash
10
```






















































<!--- ( REFERENCES ) --->

---

<div id="ref"></div>

## REFERENCES

 - **let:**
   - [Variable Shadowing in JavaScript](https://www.geeksforgeeks.org/variable-shadowing-in-javascript/)

---

**Rodrigo** **L**eite da **S**ilva - **drigols**
