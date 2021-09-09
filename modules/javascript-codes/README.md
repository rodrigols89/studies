# JavaScript

![js-logo](res/logo.png)

## Conteúdo

 - [Trabalhando com “let”](modules/let)
 - [Trabalhando com "const"](modules/const)
 - [Temporal Dead Zone - (Hoisting)](modules/temporal-dead-zone)
 - [Trabalhando com Arrow Functions](modules/arrow-functions)
 - [Trabalhando com "Template Literal"](modules/template-literal)
 - [Trabalhando com "Property Shorthand"](modules/property-shorthand)
 - [Trabalhando com "Parâmetros Default"](modules/default-parameter)
 - [Desestruturando Objetos](modules/destructuring)

## Install

Assim que clonar o repositório basta executar o script **npm install** para baixar as dependência do projeto. Essas dependências são módulos que usaremos no projeto **(ESLint, husky)**.

```
npm install
```

__package.json__  
```json
"scripts": {
  "build": "npm install eslint husky --save-dev"
}
```

## Hooks

Vamos usar [husky](https://github.com/typicode/husky) no projeto. Ele permite que você crie hooks git mais facilmente.

__hooks:__  
O que são hooks? Hooks são alguns scripts que são executados antes/depois de algumas tarefas git. Por exemplo:

 - commit.
 - push.
 - git fetch.

__Husky Repository__  
https://github.com/typicode/husky

Vamos usar apenas o **"prepush"** para executar o **ESLint** antes de um `push`, ou seja, antes de enviar os arquivos para o nosso repositório, ele executará o **ESLint** em nosso projeto:

__package.json__
```json  
"scripts": {
  "lint": "./node_modules/.bin/eslint *.js/../",
  "prepush": "npm run lint"
}
```

---

**Rodrigo Leite -** *Software Engineer*
