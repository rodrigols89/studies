# K-Armed Bandit Problem

## Conteúdo

 - [01 - Introdução & Ideia Geral](#01)
 - [02 - Resultados diferente para a mesma Ação](#02)
 - [03 - O Problema de tentar resolver por Força Bruta](#03)
 - [04 - 10-Armed Bandit Problem](#04)

<div id="01"></div>

## 01 - Introdução & Ideia Geral

Um problema muito explorado em *Reinforcement Learning* é o **K-Armed Bandit**. Ele basicamente consiste no seguinte:

 - **1ª -** Nós temos uma quantidade **K** de *Ações* a serem tomadas e nós vamos ter que escolher uma delas;
 - **2ª -** Cada ação vai gerar uma recompensa, porém essa recompensa **não é fixa**; **ela pode variar (%)**.

Por exemplo, vamos imaginar um beber chorando e nós precisamos fazer ele parar de chorar. Cada ação (escolha) que nós tomamos vai gerar a seguinte recompensa:

 - **(+1)** Se ele parar de chorar;
 - **(-1)** Se ele continuar chorando.

![img](images/k-armed-bandit-01.png)  

**NOTE:**  
Outra observação aqui é que não necessariamente você precisa declarar as *recompensas* como **(+1)** ou **(-1)**. Você pode colocar **0.7** se ele diminuir o choro, mas ainda continuar chorando ou até colocar uma *porcentagem (%)*, etc.

Por exemplo, veja o diagrama abaixo:

![img](images/k-armed-bandit-02.png)  

**NOTE:**  
Veja que cada **escolha DA MESMA AÇÃO** tem uma *porcentagem (%)* diferente relacionada. Voltando para o nosso exemplo de uma criança chorando essas **escolhas (ações)** poderiam ser:

 - **Colocar ele no colo** - (70%);
 - **Dar uma chupeta** - (30%);
 - **Dar comida** - (55%);
 - **Chamar a mãe del**e - (100%).

---

<div id="02"></div>

## 02 - Resultados diferente para a mesma Ação

Agora vamos supor o seguinte, em determinado momento o pai da criança viu a criança chorando e colocou ela no colo e logo em seguida ela parou de chorar.  

**Ou seja, a Ação teve 100% de Recompensa (+1)**.

![img](images/father-crying-baby-01.jpg)  

O problema é que em outro momento **(ou estado)** o pai viu a criança chorando e pensou o seguinte:

> **"Eu vou fazer o mesmo procedimento *(Ação)* e a criança vai parar de chorar**.

![img](images/father-crying-baby-02.jpg)

**NOTE:**  
Então, como vocês viram acima nessa ocasião **(ou estado)** a criança não parou de chorar. Ou seja, essa *Ação* **variou** de **100%** para **50%**.

![img](images/k-armed-bandit-03.png)  

**NOTE:**  
Ou seja, da mesma Ação que nós tentamos 2 vezes apenas uma recompensa foi positiva.

---

<div id="03"></div>

## 03 - O Problema de tentar resolver por Força Bruta

O problema aqui é que nós não temos todo o tempo do mundo para ficar tentando várias Ações diferentes e a mesma Ação várias vezes.

> Isso porque a criança está chorando e nós precisamos fazer ela parar de chorar o mais rápido possível.

**NOTE:**  
Se nós ficarmos tentando todas as possibilidades possíveis basicamente nós estamos tentando uma abordagem de **Força Bruta**. E isso é um problema porque nós não temos todo o tempo do mundo para ficar tentando tudo e também não temos recurso computacional ilimitado.

> **Para isso nós precisamos maximizar as tentativas de recompensa. Ou seja, eu quero tomar as Ações que vão me levar ao resultado correto o mais rápido possível.**

---

<div id="04"></div>

## 04 - 10-Armed Bandit Problem

OK, vamos recapitular... Nós sabemos que o **K-Armed Bandir Problem** consiste em **K** *Ações* e cada *Ação* vai gerar uma *recompensa*, porém essa *recompensa* **não é fixa**, **ela pode variar**.

Agora suponha que nós temos um **10-Armed Bandit Problem**, ou seja, **10 Ações** com cada uma delas tendo uma *recompensa* associada.

Veja o plot abaixo para ver como ficou:

![img](images/10-armed-bandit.png)  

**NOTE:**  
Se você prestar atenção vai ficar claro que cada *recompensa* foi dada sobre uma **distribuição de probabilidade**; Também fica claro que cada *Ação* vai ter sua própria média, como pode ser vista abaixo:

![img](images/10-armed-bandit-01.png)  

**NOTE:**  
Essa média é a média de todas as recompensas para cada Ação. Por exemplo:

 - **`q*(1)` -** É a média de todas as recompensas da Ação **`q*(1)`**.

**Mas por que pensar nessa abordagem?**  
Por exemplo, suponha que nós vamos executar inifinitas *(ou milhares*) vezes cada uma das **10 Ações (10-Armed Bandit Problem)**. Tirar essa média seria interessante para saber qual das *Ações* daria a melhor *Recompensa*.

**NOTE:**  
Suponha que nós temos que escolher uma destas *Ações* a melhor seria a *Ação* **`q*(3)`**, pois nos dar a melhor *recompensa*; Com a melhor **distribuição de probabilidade**.

---

**REFERENCES:**  
[Didática Tech - Inteligência Artificial & Data Science](https://didatica.tech/)  

---

**Rodrigo Leite -** *Software Engineer*
