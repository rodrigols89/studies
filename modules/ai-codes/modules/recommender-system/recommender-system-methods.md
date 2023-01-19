# Métodos (abordagens) utilizadas em Sistema de Recomendação

## Conteúdo

 - [01 - Introdução aos Métodos (abordagens) utilizadas em Sistema de Recomendação](#intro)
   - [01.1 - Filtragem por Conteúdo (Content-based)](#content-based)
   - [01.2 - Filtragem Colaborativa](#collaborative-filtering)
 - [02 - Relação entre Henry Ford e Sistema de Recomendação](#henry-ford)

---

<div id="intro"></div>

## 01 - Introdução aos Métodos (abordagens) utilizadas em Sistema de Recomendação

Basicamente, se você tem interesse em trabalhar com **Sistemas de Recomentação**, os métodos (abordagens) mais utlizadas atualmente são:

 - Filtragem por Conteúdo (Content-based);
 - Filtragem Colaborativa (Collaborative Filtering);
 - Ou um método (abordagem) hibrido, ou seja, utilizando as duas abordagens acima.

Agora sabendo os métodos (abordagens) básicas, vamos fazer uma breve análise de cada uma.

---

<div id="content-based"></div>

## 01.1 - Filtragem por Conteúdo (Content-based)

> A **Filtragem por Conteúdo (Content-based)** consiste basicamente em trazer recomendações com base nas características dos *produtos* ou *serviços*.

Imagine que nós estamos analisando filmes e nós demos várias notas para diversos filmes. O que a **Filtragem por Conteúdo (Content-based)** vai fazer é *recomendar* um filme com base nas características. Por exemplo:

 - Se eu costumo assistir mais filmes de **ação** > ele vai recomendar mais filmes de **ação**.
 - Se eu costumo assistir mais filmes de **comédia** > ele vai recomendar mais filmes de **comédia**.

**NOTE:**  
Ou seja, essa abordagem está mais preocupada nas **características** dos *produtos* ou *serviços*.

 - **Vantagens:**
   - A primeira vantagem desse método (abordagem) é que ele não precisa de muitos dados para começar a trazer boas recomendações:
     -  Por exemplo, se eu tiver assistido a partir de um filme ele já vai poder recomendar um filme com base nessa características.
 - **Desvantagens:**
   - Um dos problemas desse método (abordagem) é que ele pode se tornar em uma **bolha de recomendação**, ou seja:
     - Esse método (abordagem) não vai te trazer ideias fora da caixa, por exemplo:
       - Suponha que eu comprei um jogo na amazon, esse método (abordagem) não vai ser capaz de recomendar um outro jogo que talvez eu goste, pelo simples motivo dele não ter a características que ele viu antes.

---

<div id="collaborative-filtering"></div>

## 01.2 - Filtragem Colaborativa

> A **Filtragem Colaborativa (Collaborative Filtering)** diferentemente da **Filtragem por Conteúdo (Content-based)** está preocupada com as interações do usuário com os conteúdos.

**NOTE:**  
Por exemplo, imagine que nós assistimos um filme. Um **Filtragem Colaborativa (Collaborative Filtering)** vai recomenda filmes que outras pessoas que assistiram o mesmo filme que você assistiu antes costumam assistir (ou gostar de ver). Por isso, **"Colaborativo"**.

**NOTE:**  
Outro exemplo é o seguinte, imagine que você comprou um jogo na Amazon, essa abordagem **"Colaborativa"**, pode indicar (recomendar) que pessoas que jogam esse jogo costumam comprar uma placa de vídeo mais potente. 

 - **Vantagens:**
   - Você não fica limitado a uma esfera de informações (conteúdo ou características).
 - **Desvantagens:**
   - Imagine que nós temos uma quantidade de produtos é muito vasta (por exemplo, na base dos milhões), eu não vou conseguir comprar todos essses produtos:
     - Isso faz com que a nossa matriz (dataset), onde:
       - As linhas são os usuários.
       - E as colunas são os produtos.
       - Vai ser  um Dataset (matriz) muito esparso.
       - E também vamos ter muitos dados faltantes (missing):
         - Isso, porque vão ter muitas combinações que não existem entre usuários e produtos.
   - Esse método (abordagem) também pode ter um custo computacional muito grande visto que nós vamos ter uma Matriz muito grande.

---

<div id="henry-ford"></div>

## 02 - Relação entre Henry Ford e Sistema de Recomendação

Nem sempre os usuários (pessoas) sabem de certo o que precisam, por isso, muitas vezes é importante recomendar com base em **características** ou **interações** o que é melhor para os usuários. Por exemplo, veja essa frase famosa de **Henry Ford** abaixo:

> Se eu fosse atrás do que as pessoas realmente querem, elas me pediriam cavalos mais rápidos.

**NOTE:**  
Ou seja, o que **Ford** fez foi ao invés de lhes dar o que elas **achavam** que precisavam, lhes deu algo melhor - **Carro**.

**NOTE:**  
Outra observação é que Amazon declarou que 60% das vendas dela vem de Sistemas de Recomendação.

---

**REFERÊNCIA:**  
[Didática Tech](https://didatica.tech/)

---

**Rodrigo Leite -** *drigols*
