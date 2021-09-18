# Rocketseat (Starter / React.js)

![image](res/logo.gif)

## Conteúdo

 - **O que eu aprendi que eu não sabia?**
   - [01 - Como criar um serviço para consumir uma API com Axios](#01)
   - [02 - Quando utilizar o componentDidMount()](#02)
   - [03 - Consumir dados de uma API com Axios](#03)
   - [04 - Armazenar os dados pegos da API em um estado (state)](#04)
   - [05 - Criar botões de Previous e Next de acordo com as informações da API](#05)
   - [06 - Utilizar a biblioteca react-router-dom para criar rotas](#06)

<div id='01'></div>

## 01 - Como criar um serviço para consumir uma API com Axios

É muito comum nossas aplicações precisarem consumir dados externos de outras aplicações. Para isso uma maneira é consumir dados de uma API externa. Por exemplo, veja abaixo como ter acesso a uma API da Rocketseat para testes:

[services/api.js](src/services/api.js)
```js
import axios from 'axios';

const api = axios.create({
  baseURL: 'https://rocketseat-node.herokuapp.com/api'
});

export default api;
```

A função **crete()** do *Axios* é usada para criar uma instância a qual nós vamos consumir (API).

<div id='02'></div>

## 02 - Quando utilizar o componentDidMount()

Sabe quando você tem uma tarefa que deve ser executada assim que um componente é iniciado? Então, é ai que entrar o **componentDidMount()**.

```js
componentDidMount() {
  this.loadProducts();
}
```

<div id='03'></div>

## 03 - Consumir dados de uma API com Axios

Lembram que quando nós criamos uma instância do Axios nós passamos o seguinte endereço:

```js
https://rocketseat-node.herokuapp.com/api
```

**NOTE:**  
Só esse endereço não nos diz qual **recurso** queremos consumir; Só **onde (local)** que nós vamos pegar esses recursos. Você pode testar isso no navegador que vai ter o seguinte retorno:

```js
Cannot GET /api
```

Dentro da API da Rocketseat existe o recurso **/products** e para consumir ele basta adicioná-lo a nosso endereço no navegador, ficando assim:

```js
https://rocketseat-node.herokuapp.com/api/products
```

**OUTPUT:**  
```json
// 20200821215004
// https://rocketseat-node.herokuapp.com/api/products

{
  "docs": [
    {
      "_id": "5b6b31eb31762700049b33df",
      "title": "React Native",
      "description": "A framework for building native apps with React.",
      "url": "https://github.com/facebook/react-native",
      "createdAt": "2018-08-08T18:09:47.706Z",
      "__v": 0
    },
    {
      "_id": "5b6b33ef31762700049b33e0",
      "title": "ReactJS",
      "description": "A declarative, efficient, and flexible JavaScript library for building user interfaces.",
      "url": "https://github.com/facebook/react",
      "createdAt": "2018-08-08T18:18:23.481Z",
      "__v": 0
    },
    {
      "_id": "5b6b344331762700049b33e1",
      "title": "Nuclice",
      "description": "An open IDE for web and native mobile development, built on top of Atom",
      "url": "https://github.com/facebook/nuclide",
      "createdAt": "2018-08-08T18:19:47.921Z",
      "__v": 0
    },
    {
      "_id": "5b6b345231762700049b33e2",
      "title": "Relay",
      "description": "Relay is a JavaScript framework for building data-driven React applications.",
      "url": "https://github.com/facebook/relay",
      "createdAt": "2018-08-08T18:20:02.073Z",
      "__v": 0
    },
    {
      "_id": "5b6b346931762700049b33e3",
      "title": "create-react-app",
      "description": "Create React apps with no build configuration.",
      "url": "https://github.com/facebook/create-react-app",
      "createdAt": "2018-08-08T18:20:25.374Z",
      "__v": 0
    },
    {
      "_id": "5b6b347931762700049b33e4",
      "title": "flow",
      "description": "Adds static typing to JavaScript to improve developer productivity and code quality.",
      "url": "https://github.com/facebook/flow",
      "createdAt": "2018-08-08T18:20:41.704Z",
      "__v": 0
    },
    {
      "_id": "5b6b348731762700049b33e5",
      "title": "flipper",
      "description": "A desktop debugging platform for mobile developers.",
      "url": "https://github.com/facebook/flipper",
      "createdAt": "2018-08-08T18:20:55.689Z",
      "__v": 0
    },
    {
      "_id": "5b6b349b31762700049b33e6",
      "title": "Jest",
      "description": "Delightful JavaScript Testing.",
      "url": "https://github.com/facebook/jest",
      "createdAt": "2018-08-08T18:21:15.191Z",
      "__v": 0
    },
    {
      "_id": "5b6b34a831762700049b33e7",
      "title": "Metro",
      "description": "The JavaScript bundler for React Native.",
      "url": "https://github.com/facebook/metro",
      "createdAt": "2018-08-08T18:21:28.595Z",
      "__v": 0
    },
    {
      "_id": "5b6b34bd31762700049b33e8",
      "title": "watchman",
      "description": "Watches files and records, or triggers actions, when they change.",
      "url": "https://github.com/facebook/watchman",
      "createdAt": "2018-08-08T18:21:49.787Z",
      "__v": 0
    }
  ],
  "total": 13,
  "limit": 10,
  "page": 1,
  "pages": 2
}
```

Viram que agora nós temos um objeto *(docs)* **JSON (JavaScript Object Notation)** com vários atributos e valores que podemos trabalhar (consumir).

Tem como pegar esses dados e exibir no console para ver se está tudo indo bem? Claro:

```js
loadProducts = async () => {
  const response = await api.get(`/products`);
  console.log(response.data.docs)
}
```

Vejam como foi simples... Nós apenas utilizamos o o método **get()** da nossa instância do *Axios* e pegamos o recurso **/products**.

<div id='04'></div>

## 04 - Armazenar os dados pegos da API em um estado (state)

Bem, nós já sabemos como criar uma instância do *Axio* para fazer referência a uma API; Como consumir (pegar) os recursos da API, mas como armazenar os recursos (dados) em um estado para depois trabalhar com eles?

No React não é comum ficar salvando nossos dados em uma variável. Ao invés disso nós utilizamos um conceito chamado estado (state). **Outra coisa importante a se saber é que esses estados sempre serão objetos**.

Por exemplo, vamos representar os dados que nós queremos consumir da API como um objeto (state/estado) assim:

```js
state = {
  products: [],
  productInfo: {},
  page: 1,
}
```

Bem, como podem ver nós criamos estados (states) vazios... Agora como preencher esses estados? Simples, basta utilizar o **this.setState** e depois atualizar. Vai ficar assim:

```js
loadProducts = async (page = 1) => {
  const response = await api.get(`/products?page=${page}`);
  const { docs, ...productInfo } = response.data;
  this.setState({ products: docs, productInfo, page });
}
```

<div id='05'></div>

## 05 - Criar botões de Previous e Next de acordo com as informações da API

A API que estamos consumindo tem bastante informações. Então, chegou a hora de criar 2 botões utilizando lógica e informações da API para deixar eles ativados e desabilitados:

```jsx
state = {
  products: [],
  productInfo: {},
  page: 1,
}

prevPage = () => {
  const { page } = this.state;
  if (page === 1) return;
  const pageNumber = page - 1;
  this.loadProducts(pageNumber);
}

nextPage = () => {
  const { page, productInfo } = this.state;
  if (page === productInfo.pages) return;
  const pageNumber = page + 1;
  this.loadProducts(pageNumber);
}

<div className="actions">
  <button disabled={page === 1} onClick={this.prevPage}>Previous</button>
  <button disabled={page === productInfo.pages} onClick={this.nextPage}>Next</button>
</div>
```

<div id='06'></div>

## 06 - Utilizar a biblioteca react-router-dom para criar rotas

É muito comum uma aplicação web ter várias rotas para navegar. Por isso é importa definir bem essas rotas para não deixar o usuário perdido na aplicação.

Para criar as rotas da aplicação foi feito o seguinte:

[routes.js](src/routes.js)
```jsx
import React from 'react';

import { BrowserRouter, Switch, Route } from 'react-router-dom';

import HomeContent from './pages/home-content/HomeContent';
import Product from './pages/product/Product';

const Routes = () => (
  <BrowserRouter>
    <Switch>
      <Route exact path="/" component={HomeContent} />
      <Route path="/products/:id" component={Product} />
    </Switch>
  </BrowserRouter>
)

export default Routes;
```

Onde:

```md
</BrowserRouter>
- Indica que nós estamos utilizando nossas rotas através de um Browser.

</Switch>
- O Switch nesse contexto vai ser utilizado para fazer com que apenas uma rota seja utilizada ao mesmo tempo.
- Isso porque em uma rota você pode querer que mais de um componente seja exibido ao mesmo tempo por rota.

<Route exact path="/" component={HomeContent} />
- Quando a aplicação não tiver nenhuma rota seleciona nós vamos apenas exibir o component HomeContent:
  - Tipo o Home da aplicação.
- O atributo exact significa que ele só vai utilizar essa rota, ou eja, "/" quando for só ela e mais nada.

<Route path="/products/:id" component={Product} />
- Aqui foi criada a rota /products e o id do produto, por isso, :id.
- E nós chamamos o component "Product".
```

Ok, tudo lindo! Já temos as rotas configuradas mas como linkar elas com os nossos botões? Grças a Deus o **react-router-dom** também tem algo para isso e é mesmo o **Link**:

```jsx
import { Link } from 'react-router-dom'

<Link to={`/products/${product._id}`}>Access</Link>
```

Veja que ao invés nós criarmos um `</a>` com um **href**, nós chamamos o **Link** do **react-router-dom** e passamos a referência para a rota que nós criamos **/products** e pegamos o id do produto.

**NOTES:**  
Se você prestar atenção vai ver no navegador que quando você mudar para a rota **/products** ele vai exibir o ID do produto no final.

---

**REFERENCES:**  
[ReactJS](https://rocketseat.com.br/)

---

**Rodrigo Leite** *- Software Engineer*
