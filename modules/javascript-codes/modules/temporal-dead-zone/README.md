# Temporal Dead Zone - (Hoisting)

```js
console.log(x) // "undefined"
var x = 100;
```

**O que? (What?)**  
> Bem pessoas é seguintes: quando declaramos uma variável com a palavra-chave **"var"**, é como se, quando o interpretador inicia seu trabalho, ele já reserve espaços na memória para essas variáveis **(var)**, no entanto, seus valores ainda não foram definidos como é o caso de **"undefined"**.

Isso também é conhecido em JavaScript como ***"Hoisting"***. Mas isso não é interessante e pode até causar alguns problemas que não mencionaremos aqui.

**NOTE:**  
O importante é saber que, quando criamos variáveis com as palavras-chave *"let"* e *"const"*, isso não é mais possível no JavaScript.

```js
// Error 01
console.log(x);
let x = 10;

// Error 02
console.log(y);
const y = 20;
```

Esse seria o resultado usando as palavras-chave **"let"** e **"const"**.

**Output:**
```js
Uncaught ReferenceError: x is not defined
Uncaught ReferenceError: y is not defined
```

---

**Rodrigo Leite -** *Software Engineer*
