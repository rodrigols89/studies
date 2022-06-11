# Por que usar Docker?

## Contents

 - [01 - Introdução e Perguntas chaves](#01)
 - [02 - Ambientes semelhantes](#02)
   - [02.1 -  A criação de um container Docker aceita argumentos (Ou seja, ambientes diferentes)](#02-1)
 - [03 - Aplicação como pacote completo](#03)

---

<div id="01"></div>

## 01 - Introdução e Perguntas chaves

Docker tem sido um assunto bem comentado ultimamente, mas muitas pessoas ainda fazem as perguntas mais básica quando se trata da possibilidade de utilizar qualquer nova tecnologia:

 - **“Por que devo usar isso?”**
 - **“O que isso tem a me oferecer diferente do que já tenho hoje?”**

**NOTE:**  
Agora nós vamos tentar resolver essas perguntas de alguma forma.

---

<div id="02"></div>

## 02 - Ambientes semelhantes

> Uma vez que sua aplicação seja transformada em uma imagem Docker, ela pode ser instanciada como container em qualquer ambiente que desejar.

**NOTE:**  
Isso significa que poderá utilizar sua aplicação no notebook do desenvolvedor da mesma forma que seria executada no servidor de produção.

---

<div id="02-1"></div>

## 02.1 -  A criação de um container Docker aceita argumentos (Ou seja, ambientes diferentes)

Uma imagem Docker aceita argumentos **(Esses parâmetros são definidos na criação da imagem)** durante o início do container, isso indica que a mesma imagem pode se comportar de formas diferentes entre ambientes distintos.

 - Esse container pode conectar-se a seu banco de dados local para testes, usando as credenciais e base de dados de teste;
 - Mas quando o container for criado a partir da mesma imagem e receber argumentos do ambiente de produção, acessará a base de dados em uma infraestrutura mais robusta, com suas respectivas credenciais e base de dados de produção, por exemplo.

---

<div id="03"></div>

## 03 - Aplicação como pacote completo

> Com utilização de imagens Docker é possível empacotar toda sua aplicação e dependências, facilitando a distribuição, pois não será mais necessário enviar uma extensa documentação explicando como configurar a infraestrutura necessária para permitir a execução, basta disponibilizar a imagem em repositório e liberar o acesso para o usuário e, ele mesmo pode baixar o pacote, que será executado sem problemas.

---

**REFERENCES:**  
[Por que usar Docker?](https://stack.desenvolvedor.expert/appendix/docker/porque.html)
