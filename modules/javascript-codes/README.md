# JavaScript

## Contents

 - [**let**](#intro-to-let)
   - [let shadowing](#let-shadowing)
   - [Illegal shadowing](#illegal-shadowing)
 - [**REFERENCES**](#ref)
<!---
[WHITESPACE RULES]
- Same topic = "10" Whitespace character.
- Different topic = "50" Whitespace character.
--->




















































<!--- ( Let) --->

---

<div id="intro-to-let"></div>

## let

Variáveis declaradas com **"let"**:

 - Podem ter seus valores reatribuídos no mesmo escopo;
 - Mas não podem ser redeclaradas no mesmo escopo. 

Por exemplo:

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






















































































<!--- ( Let) --->

---

<div id="ref"></div>

## REFERENCES

 - **let:**
   - [Variable Shadowing in JavaScript](https://www.geeksforgeeks.org/variable-shadowing-in-javascript/)

---

**Rodrigo** **L**eite da **S**ilva - **drigols**
