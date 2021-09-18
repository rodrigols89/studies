# Trabalhando com Arrow Functions

O exemplo "Função da seta" abaixo permite que um desenvolvedor crie uma função JavaScript com menos linhas de código. O que mudou?

 - 1º) Removemos a palavra-chave "fucntion";
 - 2º) Adicionamos a seta após os parâmetros.

**NOTE:**  
Parênteses não são necessários se apenas uma expressão (instrução) estiver presente no mesmo bloco:

```js
function display(result) {
  console.log(result); // eslint-disable-line no-console
}
 
const multiply = (x, y) => x * y;
display(multiply(5, 10));
```

**NOTE:**  
Parênteses são opcionais quando apenas um parâmetro () está presente. O que isso significa? Veja o código abaixo:

```js
const msg = message => message;
```

Agora vamos:

 - Chama a função **display()** para exibir alguma mensagem no console;
 - Passar a função **msg()** como argumento;
 - E um argumento para a função **msg()**.

```js
function display(msg) {
  console.log(msg); // eslint-disable-line no-console
}

const msg = message => message;
display(msg('drigols - Software Engineer'));
```

---

**Rodrigo Leite -** *Software Engineer*
