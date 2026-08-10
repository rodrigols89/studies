# Expressões Algébricas

## Conteúdo

 - **Monômio:**
   - [`O que é um "monômio"?`](#what-is-a-monomial)
 - **Binômio:**
   - [`O que é um "binômio"?`](#what-is-a-binômio)
 - **Polinômio:**
   - [`O que é um "polinômio"?`](#what-is-a-polinomial)
 - **Evidência:**
   - [`O que é "por em evidência"?`](#por-em-evidencia)
   - [`O que é fator comum polinomial (binomial em evidência)?`](#binomial-in-evidence)
   - [`O que é Fatoração por Agrupamento?`](#factor-by-grouping)
   - [`Como colocar em evidência um fator negativo?`](#putting-negative-factors-in-evidence)
 - **Produtos Notáveis:**
   - [`O que são "Produtos Notáveis"?`](#notable-products)
   - [`Qual o Produto Notável do "Quadrado da soma"?`](#sum-of-squares)
   - [`Qual o Produto Notável do "Quadrado da Diferença"?`](#difference-of-squares)
   - [`Produto da soma pela diferença`](#product-of-sum-by-difference)
   - [`Binômios com mesmo primeiro termo`](#binomials-with-same-first-term)
 - [**REFERÊNCIA**](#ref)
<!---
[WHITESPACE RULES]
- Same topic = "20" Whitespace character.
- Different topic = "200" Whitespace character.
--->









































































































<!--- ( Monômio ) --->

---

<div id="what-is-a-monomial"></div>

## `O que é um "monômio"?`

Um **monômio** é um *número e/ou letra(s) ligados apenas por um produto*, em que:

 - As letras aparecem com **expoentes inteiros não negativos**.

**Exemplos e Contraexemplos:**

| Expressão     | É monômio? | Motivo                                                                   |
|----------------|-----------|--------------------------------------------------------------------------|
| $7x$           | ✅ Sim    | Número e letra ligados por produto.                                      |
| $-3x^2y$       | ✅ Sim    | Produto de coeficiente e variáveis com expoentes inteiros não negativos. |
| $5$            | ✅ Sim    | É apenas um número (pode ser visto como $5x^0$).                         |
| $\dfrac{1}{x}$ | ❌ Não    | Expoente negativo: $x^{-1}$.                                             |
| $\sqrt{x}$     | ❌ Não    | Expoente fracionário: $x^{1/2}$.                                         |
| $2x + y$       | ❌ Não    | Tem **soma**, não é só produto.                                          |

> **Resumindo**  
> ➡️ **Monômio = um único termo** (número e letras multiplicados, com expoentes inteiros não negativos).  









































































































<!--- ( Monômio ) --->

---

<div id="what-is-a-binômio"></div>

## `O que é um "binômio"?`

> Um **binômio** é uma **expressão algébrica formada pela soma ou subtração de exatamente dois monômios**.

Ou seja:

* Cada parcela deve ser um **monômio**.
* Deve haver **apenas dois termos**, ligados por **+** ou **−**.

**Exemplos e Contraexemplos:**

| Expressão          | É binômio? | Motivo                                                                     |
| ------------------ | ---------- | -------------------------------------------------------------------------- |
| $x + 3$            | ✅ Sim      | Possui exatamente dois monômios.                                           |
| $2x - y$           | ✅ Sim      | Dois monômios ligados por subtração.                                       |
| $5a^2 + 7b$        | ✅ Sim      | Soma de dois monômios.                                                     |
| $4x$               | ❌ Não      | Possui apenas um termo (é um monômio).                                     |
| $x + y + z$        | ❌ Não      | Possui três termos (é um trinômio).                                        |
| $\dfrac{1}{x} + 2$ | ❌ Não      | $\dfrac{1}{x}$ não é um monômio, pois possui expoente negativo ($x^{-1}$). |
| $\sqrt{x} + 1$     | ❌ Não      | $\sqrt{x}$ não é um monômio, pois possui expoente fracionário ($x^{1/2}$). |

> **Resumindo**  
> ➡️ **Binômio = exatamente dois monômios ligados por uma soma ou subtração.**









































































































<!--- ( Polinômios ) --->

---

<div id="what-is-a-polinomial"></div>

## `O que é um polinômio?`

Um **polinômio** é uma **soma ou subtração de monômios**, em que:

 - As variáveis aparecem com **expoentes inteiros não negativos**;
 - **Sem variáveis no denominador**:
   - Quando falamos que um polinômio não pode ter denominador, estamos nos referindo a denominador com a variável.
   - 👉 Ou seja, a letra (incógnita) não pode aparecer no denominador.

**Exemplos e Contraexemplos:**

| Expressão             | É polinômio? | Motivo                                                 |
|-----------------------|--------------|--------------------------------------------------------|
| $3x^2 + 2x - 5$       | ✅ Sim       | Soma de monômios com expoentes inteiros não negativos. |
| $7x^3 - 4x^2 + x + 9$ | ✅ Sim       | Soma de monômios.                                      |
| $2x^2y + 3y^2 - xy$   | ✅ Sim       | Polinômio em duas variáveis.                           |
| $\dfrac{1}{x} + 2$    | ❌ Não       | Variável no denominador (expoente negativo).           |
| $\sqrt{x} + 3$        | ❌ Não       | Expoente fracionário ($x^{1/2}$).                      |
| $2^x + 1$             | ❌ Não       | Expoente não é constante, é a variável.                |

**EXEMPLO-01:**

$7x^2$  
(apesar de ter só um termo, ainda é considerado um polinômio: um **monômio**).

<br/>

**EXEMPLO-02:**

$3x + 5$  
(pol. com 2 termos: um com variável, outro constante).

<br/>

**EXEMPLO-03:**

$y^2 - 4$  
(pol. com 2 termos → chamado **binômio**).

<br/>

**EXEMPLO-04:**

$2a + 3b - 7$  
(pol. com 3 termos → chamado **trinômio**).

<br/>

**EXEMPLO-05:**

$4x^3 + 2x^2 - x + 9$  
(pol. com 4 termos → não tem nome especial, apenas **polinômio**).

<br/>

**EXEMPLO-06:**

$\frac{1}{2}x^2 - \frac{3}{4}x + \frac{5}{6}$

<br/>

**EXEMPLO-07:**

$6x^5 - 3x^3 + x^2 - 8$

> **Resumindo:**  
> ➡️ **Polinômio = soma (ou subtração) de monômios, "sem variáveis no denominador" e "sem expoentes negativos" ou "fracionários".**











































































































<!--- ( Por em evidência ) --->

---

<div id="por-em-evidencia"></div>

## `O que é "por em evidência"?`

Bem, para entender esse conceito vamos com a *Propriedade Distributiva*:

$a(b + c) = a \cdot b + a \cdot c$

> **Mas qual relação essa propriedade (distributiva) tem com "Por em evidência"?**

Vamos partir da seguinte expressão:

$7 \cdot 4 + 3 \cdot 4$

> **Agora, qual termo aparece em comum nas 2 expressões?**  
> "4".

Vocês concordam que nós poderíamos fazer:

$7 \cdot 4 + 3 \cdot 4 = 4(7 + 3)$

> **What?**  
> Isso mesmo nós fizemos o caminho inverso da *"Propriedade Distributiva"*.

Vamos ver outros exemplos para ficar mais claro:

**EXEMPLO-01:**  
$4 \cdot π \cdot 3 + 2 \cdot  π =  π(4 \cdot 3 + 2)$

**EXEMPLO-02:**  
$8\sqrt{2} - 3 \sqrt{2} = \sqrt{2}(8 - 3)$

**EXEMPLO-03:**  
$4 \sqrt{3} + \frac{\sqrt{3}}{2}$

**NOTE:**  
Bem, essa expressão acima é peculiar... vocês concordam que a segunda parte da expressão acima poderia se escrita assim:

$\frac{\sqrt{3}}{2} = \sqrt{3} \cdot \frac{1}{2} $

Isso porque existe uma propriedade fundamental da divisão que é a seguinte:

$a \div b = a \cdot  \frac{1}{b}, \ b \neq 0$

Ou seja, na nossa expressão, onde $a = \sqrt{3}$ e $b = 2$ nós teríamos:

$\sqrt{3} \div 2 = \sqrt{3} \cdot \frac{1}{2} = \frac{\sqrt{3}}{2}$

Continuando, agora nossa expressão vai ser a seguinte:

$4 \sqrt{3} + \sqrt{3} \cdot \frac{1}{2}$

Agora, sabendo que o temro $\sqrt{3}$ aparece nas 2 expressões, podemos por em evidência assim:

$4 \sqrt{3} + \sqrt{3} \cdot \frac{1}{2} = \sqrt{3}(4 + \frac{1}{2})$

> **NOTE:**  
> Uma observação é que essa regra se aplica as 4 operações matemáticas: `+`, `-`, `*`, `/`.






















---

<div id="binomial-in-evidence"></div>

## `O que é fator comum polinomial (binomial em evidência)?`

Muitas vezes o fator comum não é um número ou variável, e sim um **polinômio inteiro**.

$A \cdot P(x) + B\cdot P(x) = P(x)(A + B)$

> **NOTE:**  
> A ideia é a mesma de **"Por em evidência" simples**:

**EXEMPLO-01:**

$2(x + 1) + 3(x + 1)$

👉 Fator comum: $(x + 1)$.

$(2+3)(x+1) = 5(x+1)$

**EXEMPLO-02:**

$x(x + 2) + 5(x + 2)$

👉 Fator comum: $(x + 2)$

$(x + 5)(x + 2)$

**EXEMPLO-03:**

$(x^2+1)(x-3) - 4(x^2+1)$
  
👉 Fator comum: $(x^2+1)$

$(x^2+1)\big((x-3)-4\big) = (x^2+1)(x-7)$























---

<div id="factor-by-grouping">

## `O que é Fatoração por Agrupamento?`

> **O que é Fatoração por Agrupamento?**

> Às vezes, não existe **um único fator comum** em **todos os termos** da expressão.

 - Nesse caso, podemos **agrupar** os termos em pares (ou blocos) e colocar em evidência dentro de cada grupo (bloco).
 - Depois, se sobrar um fator comum polinomial, conseguimos fatorar de forma completa.

**EXEMPLO-01:**

$ax + ay + bx + by$
  
👉 Agrupando em bloco nós teremos: 

$(ax + ay) + (bx + by)$

👉 Colocando em evidência dentro de cada bloco:  

$a(x+y) + b(x+y)$
  
👉 Agora o fator comum é $(x + y)$:

$(x+y)(a+b)$

<br/>

**EXEMPLO-02:**

$ab + ac + db + dc$
  
👉 Agrupando em bloco nós teremos:

$(ab + ac) + (db + dc)$

👉 Colocando em evidência:

$a(b+c) + d(b+c)$
  
👉 Fator comum: $(b+c)$:

$(b+c)(a+d)$

<br/>

**EXEMPLO-03:**

$2x^2 + 6x + 5x + 15$
  
👉 Agrupando em bloco nós teremos:

$(2x^2+6x) + (5x+15)$

👉 Colocando em evidência:

$2x(x+3) + 5(x+3)$
  
👉 Fator comum: $(x+3)$:

$(x+3)(2x+5)$

<br/>

**EXEMPLO-04:**

$x^3+3x^2+2x+6$
  
👉 Agrupando em bloco nós teremos:

$(x^3+3x^2)+(2x+6)$
  
👉 Colocando em evidência:

$x^2(x+3)+2(x+3)$

👉 Fator comum: $(x+3)$:

$(x+3)(x^2+2)$

<br/>

**EXEMPLO-05:**

$a^3+2a^2+3a+6$

👉 Agrupando em bloco nós teremos:

$(a^3+2a^2)+(3a+6)$

👉 Colocando em evidência:

$a^2(a+2)+3(a+2)$
  
👉 Fator comum: $(a+2)$:

$(a+2)(a^2+3)$

<br/>

**EXEMPLO-06:**

$2x^3+4x^2+3x+6$

👉 Agrupando em bloco nós teremos:

$(2x^3+4x^2)+(3x+6)$

👉 Colocando em evidência:

$2x^2(x+2)+3(x+2)$
  
👉 Fator comum: $(x+2)$:

$(x+2)(2x^2+3)$

#### 🚀 Conclusão

Se vocês prestarem atenção vão ver que nessa abordagem:

 - Primeiro, nós separaramos (agrupamos) os termos em blocos;
 - Depois colocamos em evidência esses agrupamentos (blocos):
   - Claro, fazendo com que apareçam termos semelhantes que possam ser colocados em evidência.
   - E isso é feito realizando manipulações algébricas.

























---

<div id="putting-negative-factors-in-evidence">

## `Como colocar em evidência um fator negativo?`

> Como colocar em evidência um fator negativo?

Até agora, vimos como colocar fatores positivos em evidência.  
Mas também podemos **colocar em evidência um fator negativo** quando isso ajuda a simplificar a expressão.  

> ➡️ O truque é **"puxar" o sinal negativo para fora dos parênteses**, o que inverte o sinal de todos os termos dentro.

**EXEMPLO-01:**

$-x - y = -(x + y)$

**EXEMPLO-02:**

$-a - b - c = -(a + b + c)$

**EXEMPLO-03:**

$-2x + 4 = -(2x - 4)$

**EXEMPLO-04:**

$-x^2 - 3x = -(x^2 + 3x)$

**EXEMPLO-05:**

$-m^2 + n^2 = -(m^2 - n^2)$

**EXEMPLO-06:**

$-4x^2 - 8x = -4(x^2 + 2x)$

**EXEMPLO-07:**

$-a^3 - 2a^2 - a = -(a^3 + 2a^2 + a)$

**EXEMPLO-08:**

$-3x^2y - 6xy^2 = -3xy(x + 2y)$

**EXEMPLO-09:**

$-x^3 - x^2 - x - 1 = -(x^3 + x^2 + x + 1)$

**EXEMPLO-10:**

$-2x^3 - 4x^2 - 6x = -2(x^3 + 2x^2 + 3x)$

#### 🚀 Conclusão

 - Colocar um **fator negativo em evidência** é útil para simplificar expressões e preparar uma fatoração mais organizada.  
 - A regra prática é:
   - Se todos os termos têm sinal negativo, podemos colocar **$-1$** em evidência.
   - Se todos os termos têm um fator comum **e negativo**, podemos colocá-lo em evidência (ex: $-2$, $-3x$, etc.).  












































































































<!--- ( Produtos notáveis ) --->

---

<div id="notable-products"></div>

## `O que são "Produtos Notáveis"?`

 - *Produtos Notáveis* são multiplicações de expressões (geralmente binômios) que seguem *padrões fixos*.  
 - **NOTE:** Eles derivam da **propriedade distributiva** e servem como *atalhos* para expandir (multiplicar) ou reconhecer *fatorações*.

#### ✅ Resumindo, Produtos Notáveis são (é)
 
 - *Padrões de multiplicação* que vêm da *distributiva*.
 - Servem para *expandir rápido* e para *fatorar reconhecendo padrões*.






















---

<div id="sum-of-squares"></div>

## `Qual o Produto Notável do "Quadrado da soma"?`

![img](images/sum-of-squares-01.jpeg)  























---

<div id="difference-of-squares"></div>

## `Qual o Produto Notável do "Quadrado da Diferença"?`

![img](images/difference-of-squares-01.jpeg)  
























---

<div id="product-of-sum-by-difference"></div>

## `Produto da soma pela diferença`

![img](images/product-of-sum-by-difference-01.jpeg)  
























---

<div id="binomials-with-same-first-term"></div>

## `Binômios com mesmo primeiro termo`

![img](images/binomials-with-same-first-term-01.jpeg)












































































































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
