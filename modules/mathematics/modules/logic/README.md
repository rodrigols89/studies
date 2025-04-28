# Raciocínio Lógico

## Conteúdo

 - **Tabela-Verdade:**
   - **Questões abertas (livros, tutoriais):**
     - [Conjunção: Quando é verdadeiro?](#conjunction-table)
     - [Disjunção Inclusiva: Quando é verdadeiro?](#disjunction-inclusive-table)
     - [Disjunção Exclusiva: Quando é verdadeiro?](#disjunction-inclusive-table)
     - [Condicional: Quando é verdadeiro?](#conditional-table)
     - [Bicondicional: Quando é verdadeiro?](#biconditional-table)
     - [Tautologia & Contradição](#tautology-and-contradiction)
     - [Como saber quantas linhas e quais valores V/F em cada linha de uma Tabela-Verdade de "n" letras de proposições?](#n-letters-count)
     - [`A ∨ B' ⇒ (A ∨ B)'`](#qal-01)
     - [`(A ∨ A') ⇒ (B ∧ B')`](#qal-02)
     - [`[(A ∧ B') ⇒ C']'`](#qal-03)
   - **Questões de Concurso:**
     - **Fáceis:**
       - [3312948 CEBRASPE (CESPE) - 2025 - Analista Administrativo (ANM)/Administração](#qcf-01)
     - **Médias:**
     - **Dificeis:**
<!---
[WHITESPACE RULES]
- Same topic = "20" Whitespace character.
- Different topic = "100" Whitespace character.
--->





































































































<!--- ( Tabela-Verdade ) --->

---

<div id="conjunction-table"></>

## Conjunção: Quando é verdadeiro?

> Quando na Tabela-Verdade da **"conjunção"** seus valores lógicos são verdadeiros?

<details>

<summary>RESPOSTA</summary>

<br/>

> A Tabela-Verdade da *conjunção* só retorna *verdadeiro (V)* quando as proposições são verdadeiras *simultaneamente*.

![img](images/conjunction-table-01.png)  

</details>




















---

<div id="disjunction-inclusive-table"></>

## Disjunção Inclusiva: Quando é verdadeiro?

> Quando na Tabela-Verdade da **"Disjunção Inclusiva"** seus valores lógicos são verdadeiros?

<details>

<summary>RESPOSTA</summary>

<br/>

> Na Tabela-Verdade da **Disjunção Inclusiva**, basta que apenas uma das proposições seja *verdadeira (V)* para que seu retorno seja verdadeiro.

![img](images/disjunction-inclusive-table-01.png)  

> **NOTE:**  
> Veja que a **Disjunção Inclusiva** só é *falsa (F)* quanto as proposições são falsas simultaneamente.

</details>




















---

<div id="disjunction-inclusive-table"></>

## Disjunção Exclusiva: Quando é verdadeiro?

> Quando na Tabela-Verdade da **"Disjunção Exclusiva"** seus valores lógicos são verdadeiros?

<details>

<summary>RESPOSTA</summary>

<br/>

> Na Tabela-Verdade da **Disjunção Exclusiva** seus valores lógicos só são verdadeiros quando uma proposição é *verdadeira (V)* e a outra é *falta (F)*.

![img](images/exclusive-disjunction-table-01.png)  

</details>




















---

<div id="conditional-table"></>

## Condicional: Quando é verdadeiro?

> Quando na Tabela-Verdade **"Condicional"** seus valores lógicos são verdadeiros?

<details>

<summary>RESPOSTA</summary>

<br/>

> A Tabela-Verdade **Condicional** só retorna falso se a primeira proposição for *verdadeira (V)* e a segunda *falta (F)*.

![img](images/conditional-table-01.png)  

> **Mas por quê?**

Uma condicional (também chamada de "implicação lógica") tem a forma:

```bash
𝑝 → 𝑞
```

onde:

 - 𝑝 é a hipótese (ou antecedente);
 - 𝑞 é a conclusão (ou consequente).

Nesse, caso a condicional é considerada falsa apenas quando:

 - A **hipótese** (𝑝) é **verdadeira, mas**;
 - A **conclusão** (𝑞) é **falsa**.

> **Por quê?**  
> Porque quando você afirma `"Se 𝑝, então 𝑞"`, você está garantindo que sempre que 𝑝 acontecer, 𝑞 também acontecerá.

Então:

 - Se você cumpre 𝑝 (verdadeiro) e 𝑞 não acontece (falso), você **quebra a promessa da condicional**:
   - Portanto, ela é falsa.
 - Mas, se 𝑝 é falso, não importa o que acontece com 𝑞:
   - A **promessa não foi "testada"**, então a condicional continua considerada verdadeira. (não houve quebra da promessa).

</details>




















---

<div id="biconditional-table"></>

## Bicondicional: Quando é verdadeiro?

> Quando na Tabela-Verdade **"Bicondicional"** seus valores lógicos são verdadeiros?

<details>

<summary>RESPOSTA</summary>

<br/>

> A Tabela-Verdade **Bicondicional** só retorna verdadeiro se as 2 proposições forem *verdadeiras (V)*; ou as 2 proposições forem *falsas (F)*.

![img](images/bicondicional-table-01.png)  

> **Mas por quê?**

Uma bicondicional tem a forma:

```bash
𝑝 ↔ 𝑞
```

onde:

 - 𝑝 é a **hipótese**;
 - 𝑞 é a **conclusão**.

A bicondicional é considerada verdadeira apenas quando:

 - A *hipótese (𝑝)* e a *conclusão (𝑞)* **têm o mesmo valor lógico**.

> **Por quê?**  
> Porque na bicondicional você está fazendo uma promessa dupla.

 - **Prometo que 𝑝 e 𝑞 acontecem juntos:**
   - Se um é verdadeiro, o outro também será;
   - Se um é falso, o outro também será.

Logo:

 - Se a *hipótese (𝑝)* e a *conclusão (𝑞)* são iguais (ambas verdadeiras ou ambas falsas):
   - A promessa foi cumprida → resultado *verdadeiro (V)*.
 - Mas, se a hipótese e a conclusão são diferentes (um verdadeiro e o outro falso e vice-versa):
   - A promessa foi quebrada → resultado *falso (F)*.

</details>




















---

<div id="tautology-and-contradiction"></div>

## Tautologia & Contradição

### Tautologia

> **Quando uma proposição é considerada uma "tautologia"?**

<details>

<summary>RESPOSTA</summary>

<br/>

> Uma proposição é considerada uma **tautologia** quando ela sempre retorna *verdade (V)* em todas as linhas da Tabela-Verdade.

O exemplo mais simples de uma *tautologia* é `A ∨ A' (disjunção)`:

| A | A' | A ∨ A' |
|---|----|--------|
| V | F  | V      |
| F | V  | V      |

</details>

### Contradição

> **Quando uma proposição é considerada uma "contradição"?**

<details>

<summary>RESPOSTA</summary>

<br/>

> Uma proposição é considerada uma **contradição** quando ela sempre retorna *falso (F)* em todas as linhas da Tabela-Verdade.

O exemplo mais simples de uma *contradição* é `A ∧ A' (conjunção)`:

| A | A' | A ∧ A' |
|---|----|--------|
| V | F  | F      |
| F | V  | F      |

</details>




















---

<div id="n-letters-count"></div>

## Como saber quantas linhas e quais valores V/F em cada linha de uma Tabela-Verdade de "n" letras de proposições?

Saber quantas linhas e valores V/F de cada linha para uma proposição de 1 ou 2 letras de proposição é simples:

**Exemplo:** 1 letra de proposição:
| A |
|---|
| V |
| F |

**Exemplo:** 2 letras de proposição:
| A | B |
|---|---|
| V | V |
| V | F |
| F | V |
| F | F |

> **Mas para uma proposição de "n" letras de proposição, como saber quantas linhas e quais valores V/F da Tabela-Verdade?**

<details>

<summary>RESPOSTA</summary>

<br/>

> Uma maneira interessante é criar uma tabela-verdade é utilizando o conceito de *"árvore matemática"*.

Por exemplo, vamos criar uma *tabela-verdade* para 2 letras de proposição utilizando o conceito de *árvore matemática*:

```bash
                   nº de letras     nº de
                   proposição       possibilidades (linhas)
       •          
     /   \        
    V     F        2¹               2
   / \   / \
  V   F  V  F      2²               4
```

**Exemplo:** 2 letras de proposição:
| A | B |
|---|---|
| V | V |
| V | F |
| F | V |
| F | F |

**NOTE:**  
Como podem ver a fórmula para calcular o número de possibilidades (linhas) com base no número de letras de proposição é a seguinte: **2<sup>n</sup>** , sendo **“n”** o número de letras de proposição.

> **E se a proposição tiver 3 letras?**

```bash
                              nº de letras     nº de
                              proposição       possibilidades (linhas)
            •   
       /        \
      V           F           2¹               2
    /   \       /   \
   V     F     V      F       2²               4
  / \   / \   / \    / \
 V   F  V  F  V  F   V  F     2³               8
```

**Exemplo:** 3 letras de proposição:
| A | B | C |
|---|---|---|
| V | V | V |
| V | V | F |
| V | F | V |
| V | F | F |
| F | V | V |
| F | V | F |
| F | F | V |
| F | F | F |

</details>




















---

<div id="qal-01"></div>

## `A ∨ B' ⇒ (A ∨ B)'`

Qual a tabela-verdade para a seguinte *fórmula bem formada (fbf)*: `A ∨ B' ⇒ (A ∨ B)'`

<details>
<summary>RESPOSTA</summary>

<br/>

| A | B | B' | A ∨ B' | (A ∨ B) | (A ∨ B)' | A ∨ B' ⇒ (A ∨ B)' |
|:-:|:-:|:--:|:------:|:-------:|:--------:|:-----------------:|
| V | V | F  | V      | V       | F        | F                 |
| V | F | V  | V      | V       | F        | F                 |
| F | V | F  | F      | V       | F        | V                 |
| F | F | V  | V      | F       | V        | V                 |

</details>




















---

<div id="qal-02"></div>

## `(A ∨ A') ⇒ (B ∧ B')`

Qual a tabela-verdade para a seguinte fórmula bem formada (fbf): `(A ∨ A') ⇒ (B ∧ B')`

<details>

<summary>RESPOSTA</summary>

<br/>

| A | B | A' | B' | A ∨ A' | B ∧ B' | (A ∨ A') ⇒ (B ∧ B') |
|:-:|:-:|:--:|:--:|:------:|:------:|:-------------------:|
| V | V |  F |  F |   V    |   F    |          F          |
| V | F |  F |  V |   V    |   F    |          F          |
| F | V |  V |  F |   V    |   F    |          F          |
| F | F |  V |  V |   V    |   F    |          F          |

</details>




















---

<div id="qal-03"></div>

## `[(A ∧ B') ⇒ C']'`

Qual a tabela-verdade para a seguinte fórmula bem formada (fbf): `[(A ∧ B') ⇒ C']'`

<details>

<summary>RESPOSTA</summary>

<br/>

| A | B | C | B' | (A ∧ B') | C' | (A ∧ B') → C' | [(A ∧ B') ⇒ C']'  |
|:-:|:-:|:-:|:--:|:--------:|:--:|:-------------:|:-----------------:|
| V | V | V | F  | F        | F  | V             | F                 |
| V | V | F | F  | F        | V  | V             | F                 |
| V | F | V | V  | V        | F  | F             | V                 |
| V | F | F | V  | V        | V  | V             | F                 |
| F | V | V | F  | F        | F  | V             | F                 |
| F | V | F | F  | F        | V  | V             | F                 |
| F | F | V | V  | F        | F  | V             | F                 |
| F | F | F | V  | F        | V  | V             | F                 |

</details>






































































































<!--- ( Questões de Concurso/Fáceis  ) --->

---

<div id="qcf-01"></div>

## 3312948 CEBRASPE (CESPE) - 2025 - Analista Administrativo (ANM)/Administração

Considerando a proposição **P: “Não prometo que você voltará, e, se voltar, não será o mesmo.”**, julgue o item seguinte, em relação a aspectos da lógica sentencial dessa proposição.

A tabela-verdade referente à proposição P possui mais de 15 linhas.

 - Certo
 - Errado

<details>

<summary>RESPOSTA</summary>

<br/>

Primeiro vamos identificar quais (quantas) proposições simples tem a sentença:

 - (¬a) "Não prometo que você voltará";
 - (b) "e, se voltar";
 - (¬c) "não será o mesmo".

Logo, nós teremos a seguinte proposição composta:

```bash
¬a ∧ (b → ¬c)
```

> **NOTE:**  
> Porém, a questão que saber se "A tabela-verdade referente à proposição P possui mais de 15 linhas".

Sabendo que nós temos 3 proposições simples e a formula para calcular o número de linhas de uma tabela-verdade é dada por **2<sup>n</sup>**, sendo **“n”** o número de proposições simples, temos:

```bash
2³ = 8
```

Ou seja, a resposta correta seria **"Errado"**, pois nossa tabela-verdade não terá mais 15 linhas.

</details>





































































































<!--- ( REFERÊNCIA ) --->

---

<div id="ref"></div>

## REFERÊNCIA

 - **Cursos:**
   - [Licenciatura - Matemática](https://www.faculdadeunica.com.br/graduacao/ead/matematica-3080)
 - **Livros:**
   - [Fundamentos Matemáticos Para a Ciência da Computação](https://www.amazon.com.br/Fundamentos-Matem%C3%A1ticos-Para-Ci%C3%AAncia-Computa%C3%A7%C3%A3o/dp/8521614225)

---

**Rodrigo** **L**eite da **S**ilva - **rodrigols89**
