# Trabalhando com “let”

> Uma variável declarada com a palavra-chave **"let" - NÃO PODE SER REESCRITA NO MESMO ESCOPO**.

De fato, uma variável declarada com a palavra-chave **"let"** precisa que seus valores sejam reatribuídos. Faz sentido, porque, caso contrário, o que realmente precisamos é uma constante **(const)**:

```js
let animal = 'cat';
sayAnima(animal);
```

Veja o código abaixo:  

```js
let animal = 'cat';
let animal = 'dog'
```

**Output:**  

```
The following error would result:
U SyntaxError: Identifier 'animal' has already been declared.
```

Isso ocorre porque estamos tentando criar uma variável que já foi criado com a palavra reservada ***"let" no mesmo escopo***.


**NOTE:**  
O código abaixo resultaria em um erro porque uma variável declarada no escopo global está disponível nos outros blocos internos.

```js
// let animal = 'Elephant';
 
/* SECOND SCOPE. */
{
  // Animal variable declared with "let" in the SECOND SCOPE.
  let animal = 'cat';
  sayAnima(animal);
 
  animal = 'catTwo';
  sayAnima(animal);
}
 
 
/* THIRD SCOPE. */
{
  // Animal variable declared  with "let" in THIRD SCOPE.
  let animal = 'dog';
  sayAnima(animal);
 
  animal = 'dogTwo';
  sayAnima(animal);
}
```

**Rodrigo Leite -** *Software Engineer*
