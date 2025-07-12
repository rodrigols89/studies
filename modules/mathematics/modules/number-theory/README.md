# Teoria dos Números

## Conteúdo

 - [**Dividores (O que são divisores de um número?)**](#divisors)
   - [O número 1 é divisor de todos os números (Inteiros ou Não-Inteiros)?](#1-divisor)
   - [Quando um número é divisível por "2"?](#divisible-by-2)
   - [Quando um número é divisível por "3"?](#divisible-by-3)
   - [Quando um número é divisível por "5"?](#divisible-by-5)
   - [Quando um número é divisível por "6"?](#divisible-by-6)
   - [Quando um número é divisível por "9"?](#divisible-by-9)
 - [**Multiplos (O que são multiplos de um número?)**](#multiples)
 - [**Números Primos**](#prime-numbers)
   - [O número "1" é primo?](#prime-number-1)
   - [Podemos formar qualquer número natural com a multiplicação de primos?](#prime-multiplication)
 - **Questões Abertas:**
 - **Questões do ENEM:**
 - **Questões de Concurso:**
<!---
[WHITESPACE RULES]
- Same topic = "10" Whitespace character.
- Different topic = "100" Whitespace character.
--->



















































<!--- ( Dividores ) --->

---

<div id="divisors"></div>

## Dividores (O que são divisores de um número?)

> O que são divisores de um número?

<details>

<summary>RESPOSTA</summary>

<br/>

**📌 Definição formal:**  
Um número 𝑑 é divisor de 𝑛 se:

```bash
𝑛 ÷ 𝑑 tem resto 0 (ou seja, 𝑛 mod 𝑑 = 0)
```

**Exemplo 01:** Divisores de 12  

 - ✅ 12 ÷ 1 = 12 *(resto/mod 0)*
 - ✅ 12 ÷ 2 = 6 *(resto/mod 0)*
 - ✅ 12 ÷ 3 = 4 *(resto/mod 0)*
 - ✅ 12 ÷ 4 = 3 *(resto/mod 0)*
 - ✅ 12 ÷ 6 = 2 *(resto/mod 0)*
 - ✅ 12 ÷ 12 = 1 *(resto/mod 0)*

> **NOTE:**  
> Lembrando que esse processo *inicia dividindo por 1* e *termina dividindo por ele mesmo*.

Logo, os divisores de **12** são:

```bash
{1, 2, 3, 4, 6, 12}
```

</details>










---

<div id="1-divisor"></div>

## O número 1 é divisor de todos os números (Inteiros ou Não-Inteiros)?

> **O número 1 é divisor de todos os números (Inteiros ou Não-Inteiros)?**

<details>

<summary>RESPOSTA</summary>

<br/>

 - ❌ NÃO.
   - Se o número não for inteiro, o conceito de divisor não se aplica da mesma forma.
 - ✅ SIM.
   - Se o número for inteiro sim porque qualquer número dividido por 1 dá ele mesmo, sem deixar resto.

### 🧠 Pensamento-chave:

 - Divisores pertencem ao *"universo dos números inteiros"*.  
 - Se você usa números decimais, o conceito vira divisão comum (aritmética real), e não divisibilidade.

</details>










---

<div id="divisible-by-2"></div>

## Quando um número é divisível por "2"?

> Qual a condição para um número ser divisível por "2"?

<details>

<summary>RESPOSTA</summary>

<br/>

> Um número é divisível por "2" quando o último dígito (algarismo) é par (0, 2, 4, 6, 8):

Por exemplo:

 - 4**0** ÷ 2 = 20
 - 25**2** ÷ 2 = 126
 - 48**6** ÷ 2 = 243
 - 127**8** ÷ 2 = 639

</details>










---

<div id="divisible-by-3"></div>

## Quando um número é divisível por "3"?

> Qual a condição para um número ser divisível por "3"?

<details>

<summary>RESPOSTA</summary>

<br/>

> Um número é divisível por "3" quando a soma dos digitos (algarismos) é múltiplo de 3.

Por exemplo:

```bash
36 = 3 + 6 = 9 (múltiplo de 3 porque 3x3 = 9)
216 = 2 + 1 + 6 = 9 (múltiplo de 3 porque 3x3 = 9)
468 = 4 + 6 + 8 = 18 (múltiplo de 3 porque 3x6 = 18)
1278 = 1 + 2 + 7 + 8 = 18 (múltiplo de 3 porque 3x6 = 18)
```

</details>










---

<div id="divisible-by-5"></div>

## Quando um número é divisível por "5"?

> Qual a condição para um número ser divisível por "5"?

<details>

<summary>RESPOSTA</summary>

<br/>

> Um número é divisível por "5" quando o último digito (algarismo) é **0 ou (∨) 5**.

Por exemplo:

 - 2**5** ÷ 5 = 5
 - 62**5** ÷ 5 = 125
 - 30**0** ÷ 5 = 60
 - 48**0** ÷ 5 = 96

</details>










---

<div id="divisible-by-6"></div>

## Quando um número é divisível por "6"?

> Qual a condição para um número ser divisível por "6"?

<details>

<summary>RESPOSTA</summary>

<br/>

> Um número é divisível por "6" quando é divisível por **"2" e (∧) "3"** ao mesmo tempo.

Por exemplo:

```bash
1278 = 1 + 2 + 7 + 8 = 18 (múltiplo de 3 porque 3x6 = 18)
1278 = o último dígito é um número par.
1278 ÷ 6 = 213

156 = 1 + 5 + 6 = 12 (múltiplo de 3 porque 3x4 = 12)
156 = o último dígito é um número par.
156 ÷ 6 = 26

288 = 2 + 8 + 8 = 18 (múltiplo de 3 porque 3x6 = 18)
288 = o último dígito é um número par.
288 ÷ 6 = 48
```

</details>










---

<div id="divisible-by-9"></div>

## Quando um número é divisível por "9"?

> Qual a condição para um número ser divisível por "9"?

<details>

<summary>RESPOSTA</summary>

<br/>

> Um número é divisível por "9" quando a soma dos seus dígitos (algarismos) é múltiplo de 9.

Por exemplo:

```bash
216 = 2 + 1 + 6 = 9 (múltiplo de 3 porque 9x1 = 9)
4068 = 4 + 0 + 6 + 8 = 18 (múltiplo de 3 porque 9x2 = 18)
```

</details>




















































<!--- ( Multiplos ) --->

---

<div id="multiples"></div>

## Multiplos (O que são multiplos de um número?)

> O que são multiplos de um número?

<details>

<summary>RESPOSTA</summary>

<br/>

**📌 Definição formal:**  
Um número é múltiplo de outro quando ele é o resultado de uma multiplicação por esse número.

Por exemplo, para saber os múltiplos de 6, fazemos:

 - ✅ 6 × 0 = **0 (multiplo de 6)**
 - ✅ 6 × 1 = **6 (multiplo de 6)**
 - ✅ 6 × 2 = **12 (multiplo de 6)**
 - ✅ 6 × 3 = **18 (multiplo de 6)**
 - ✅ 6 × 4 = **24 (multiplo de 6)**
 - ✅ 6 × 5 = **30 (multiplo de 6)**
 - ✅ 6 × 6 = **36 (multiplo de 6)**
 - ✅ 6 × 7 = **42 (multiplo de 6)**
 - ✅ 6 × 8 = **48 (multiplo de 6)**
 - ✅ 6 × 9 = **54 (multiplo de 6)**
 - ✅ 6 × 10 = **60 (multiplo de 6)**

> **NOTE:**  
> Eles nunca terminam, porque podemos sempre multiplicar o 6 por números maiores.

</details>




































































<!--- ( Números Primos ) --->

---

<div id="prime-numbers"></div>

## Números Primos

> Qual a condição para um número ser considerado primo?

<details>

<summary>RESPOSTA</summary>

<br/>

> Para um número se considerado primo ele **só pode ser divisível por 1 e por ele mesmo**.

Por exemplo:

```bash
    2                 3                 5
   / \               / \               / \
  ÷   ÷             ÷   ÷             ÷   ÷
 /     \           /     \           /     \
1       2         1       3         1       5
|       |         |       |         |       |
2       1         3       1         5       1



    7                 11               13
   / \               /  \             /  \
  ÷   ÷             ÷    ÷           ÷    ÷
 /     \           /      \         /       \
1       7         1       11       1        13
|       |         |        |       |         |
7       1         11       1       13        1
```

</details>

---

<div id="prime-number-1"></div>

## O número "1" é primo?

Sabendo que um número é considerado primo de se ele é divisível por 1 e por ele mesmo.

> O número "1" é um número primo?

<details>

<summary>RESPOSTA</summary>

<br/>

#### 🧠 Regra-chave

Um número primo deve ter dois divisores **distintos**:

 - 1.
 - e ele mesmo.

Agora observe:

> O número 1 só tem um divisor, que é ele mesmo.

#### E por que essa definição é importante?

É uma questão de coerência matemática.  
Se o número 1 fosse considerado primo, quebraria várias regras e teoremas.

#### ✅ Exemplo: Teorema Fundamental da Aritmética

> Todo número inteiro maior que 1 pode ser escrito como produto de primos únicos (fatoração única).

Se o 1 fosse primo, por exemplo:

```bash
6 = 2 × 3
```

Mas também: 

```bash
6 = 1 × 2 × 3

ou

6 = 1 × 1 × 2 × 3, etc...
```

**🔁 Isso geraria infinitas fatorações diferentes!**  
😵‍💫 A matemática perderia a unicidade da fatoração.

#### 🧮 Então o número 1 é o quê?

> O número **1** é uma **“unidade”** — um número neutro da multiplicação.

Ele não é primo, nem composto, e tem papel especial:

```bash
1 × n = n
```

Ele não contribui para a estrutura de fatores primos.

#### ✅ Conclusão

 - O número 1 não é considerado primo porque não tem dois divisores distintos.
 - Além disso, chamá-lo de primo quebraria regras fundamentais da matemática, como a fatoração única.

</details>










---

<div id="prime-multiplication"></div>

## Podemos formar qualquer número natural com a multiplicação de primos?

> É possível formar qualquer número natural com a multiplicação de números primos?

<details>

<summary>RESPOSTA</summary>

<br/>

> Sim, nós podemos formar qualquer número natural com a multiplicação de números primos.

Por exemplo:

```bash
15 pode ser formado com a multiplicação dos seguintes números primos:
3 x 5 = 15

50 pode ser formado com a multiplicação dos seguintes números primos:
2 x 5 x 5 = 50
```

</details>




















































<!--- ( REFERÊNCIA ) --->

---

<div id="ref"></div>

## REFERÊNCIA

 - **Cursos:**
   - [Licenciatura - Matemática](https://www.faculdadeunica.com.br/graduacao/ead/matematica-3080)

---

**Rodrigo** **L**eite da **S**ilva - **rodrigols89**

<details>

<summary></summary>

<br/>

RESPOSTA

```bash

```

![img](images/)  

</details>
