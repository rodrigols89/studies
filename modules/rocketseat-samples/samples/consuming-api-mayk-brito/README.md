# Consumindo API no Front & no Back-end

## Conteúdo

 - **O que eu aprendi que eu não sabia?**
   - [01 - Utilizar o npx lite-server](#01)
   - [02 - Criar uma função assíncrona para consumir dados de uma API /+ try..catch](#02)
   - [03 - Utiliza o "cors" para liberar acesso a nossa API a partir de outros browsers/serviços](#03)
   - [04 - Utiliza o Nodemon para ficar ouvindo atualizações no arquivo server.js](#04)
   - [05 - Criar uma lista dinamica no navegador](#05)
   - [06 - Pegar o "data" direto com axios](#06)

<div id='01'></div>

## 01 - Utilizar o npx lite-server

**O que é lite-server?**  
lite-server é um servidor web de desenvolvimento leve com suporte para **Single Page Apps (SPAs)**. Na verdade, é um pouco mais técnico do que isso. Mas, para nossos propósitos, isso é bom o suficiente.

```
npx lite-server
```

<div id='02'></div>

## 02 - Criar uma função assíncrona para consumir dados de uma API /+ try..catch

**Exemplo Browser:**  
```js
(async () => {
  try {
    const response = await fetch('http://localhost:4567/');
    // Espere (await) transformar response em JSON, depois salve na variável data.
    const data = await response.json();
    show(data)
  } catch (error) {
    console.error(error);
  }
})();
```

No exemplo acima, nós temos uma função executável. Ou seja, ela vai executar logo depois de ser lida sem precisar ser invocada/chamada.

> A função fetch() é exclusica do Browser. Ou seja, não podemos utilizar ele no back-end sozinha (sem utilizar outra biblioteca).

**Exemplo no back-end:**  
```js
app.get('/', async (req, res) => {

  try {
    // "response" é a resposta do axios, MAS eu tiro o "data" de "response".
    const { data } = await axios.get('https://jsonplaceholder.typicode.com/users');
    return res.json(data);
  } catch (error) {
    console.log(error);
  }
});
```

**NOTE:**  
O **try{... }** vai passando linha por linha dentro do bloco e se não tiver nenhuma erro ele continua, senão ele entra no bloco catch (se tiver), onde nós podemos exibir um erro.

<div id='03'></div>

## 03 - Utiliza o "cors" para liberar acesso a nossa API a partir de outros browsers/serviços

```js
const cors = require('cors');

app.use(cors());
```

<div id='04'></div>

## 04 - Utiliza o Nodemon para ficar ouvindo atualizações no arquivo server.js

```json
"scripts": {
  "start": "nodemon server.js"
}
```

<div id='05'></div>

## 05 - Criar uma lista dinamica no navegador

```js
// Função executável
(async () => {
  try {
    const response = await fetch('http://localhost:4567/');
    // Espere (await) transformar "response" em JSON, depois salve na variável "data".
    const data = await response.json();
    show(data)
  } catch (error) {
    console.error(error);
  }
})();

function show(users) {
  let output = '';
  for(let user of users) output += `<li>${user.name}</li>`
  document.querySelector('main').innerHTML = output; // innerHTML recebe um valor. Não é uma função!
}
```

<div id='06'></div>

## 06 - Pegar o "data" direto com axios

Bem, se você prestou atenção no exemplo direto do browser (HTML)... Primeiro, nós pegamos a resposta (response) do nosso *fetch()* e transformamos em um JSON; E depois salvamos na variável **data**.

No axios ele já tem o *data* prontinho para nós utilizamos:

```js
const axios = require('axios')

try {
  // "response" é a resposta do axios, MAS eu tiro o "data" de "response".
  const { data } = await axios.get('https://jsonplaceholder.typicode.com/users');
  console.log(data);
  return res.json(data);
} catch (error) {
  console.log(error);
}
```

---

**REFERENCES:**  
[Consumindo API no Front & no Back-end](https://www.youtube.com/watch?v=vYlz3SmNXQQ&t=1863s)  

---

**Rodrigo Leite** *- Software Engineer*
