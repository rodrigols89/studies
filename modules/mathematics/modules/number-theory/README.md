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
