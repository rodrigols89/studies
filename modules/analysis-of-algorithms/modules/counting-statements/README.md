# Contando Instruções

## Conteúdo

 - [01 - Introdução a Contagem de Instruções](#intro)
 - [02 - Pior caso (Worst-case)](#worst-case)

<div id="intro"></div>

## 01 - Introdução a Contagem de Instruções

Suponha que nós temos um Algoritmo que recebe um array **A** com **n** elementos e armazena o maior deles em uma variável **M**:

```cpp
int M = A[0];
for(int i = 0; i < n; i++)
  if (A[i] >= M)
    M = A[i];
```

Agora vamos contas quantas **instruções simples** o algoritmo acima executa:

> **Uma Instrução Simples é uma instrução que pode ser executada diretamente pelo a CPU, ou algo muito próximo disso.**

 - **Tipos de Instruções:**
   - Atribuição de um valor a uma variável;
   - Acesso ao valor de um determinado elemento de um array;
   - Comparação de valores;
   - Incremento de um valor;
   - Operações Aritméticas básicas como *adição* e *multiplição*...

**NOTE:**  
 - **Vamos assumir que:**
   - As instruções passuem o mesmo custo;
   - Comando de seleção passuem custo zero.

Então, seguindo essas regras qual o **custo** do nosso Algoritmo?

**O custo da linha 1 é de 1 Instrução:**
```cpp
                              Cost:     Times:
int M = A[0];                 c1        1
for(int i = 0; i < n; i++)    
  if (A[i] >= M)
    M = A[i];
```

**O custo de INICIALIZAÇÃO do laço *for() (linha 2)* é de 2 Instruções:**
 - O comando **for()** precisa ser inicializado, *1 Instrução*: **int i = 0**;
 - E mesmo que o array **A** tenha tamanho zero ao menos uma comparação será executada: **i < n**; O que custa mais *1 Instrução*.
```cpp
                              Cost:     Times:
int M = A[0];                 c1        1
for(int i = 0; i < n; i++)    c2        2
  if (A[i] >= M)
    M = A[i];
```

**O custo de EXECUÇÃO do laço *for() (linha 2)* é de 2n Instruções:**
 - Ao final de cada iteração do *laço for()*, precisamos de uma instrução de:
   - Incremento: **(i++)**;
   - E uma instrução para comparar ver se vamos continuar no *laço for()*: **(i < n)**
 - O laço for será executado **"n"** vezes, logo, essas *2 instruções* também serão executadas **"n"** vezes: **2n Intruções**.
```cpp
                              Cost:     Times:
int M = A[0];                 c1        1
for(int i = 0; i < n; i++)    c2        2 + 2n
  if (A[i] >= M)
    M = A[i];
```

**NOTE:**  
Ignorando os comando dentro do *laço for()*, teremos que o algoritmo precisa executar **3 + 2n Instruções**:
 - 3 Instruções antes de iniciar o *laço for()*;
 - 2 Instruções ao final de cada *laço for()*, que serão executadas **"n"** vezes.

Assim, considerando um laço vazio, podemos definir uma função matemática que representa o custo do Algoritmo em relação ao tamanho do array de entrada como:

![image](images/tn-01.png)  

Ok, mas e as Instruções dentro do *laço for()* como nós contamos?
 - O comando **if()** tem *1 Instrução* de comparação: **(A[i] >= M)**;
 - E dentro do **if()** nós temos mais *1 Instrução* de atribuição: **M = A[i]**.
```cpp
                              Cost:     Times:
int M = A[0];                 c1        1
for(int i = 0; i < n; i++)    c2        2 + 2n
  if (A[i] >= M)              c3        1 (Quantas vezes?)
    M = A[i];                 c4        1 (Quantas vezes?)
```

**Problema:**  
Bem, agora nós temos um probleminha, quantas vezes essas instruções serão executadas?
 - As Instruções vistas anteriormente eram sempre executadas;
 - Porém, as instruções dentro do *for()* podem ou não serem executadas.

Ou seja, antes bastava saber o tamanho do array **A**, **"n"**, para definir a função de custo **T(n)**. Agora também precisamos considerar o conteúdo do array. Por exemplo, veja os dois arrays abaixo:

```cpp
A1 = [1, 2, 3, 4]
A2 = [4, 3, 2, 1]
```

 - O array **A1** terá mais instruções, isso porque o **if()** sempre será verdadeiro;
 - E o array **A2** terá menos instruções porque o **if()** sempre será faldo.

<div id="worst-case"></div>

## 02 - Pior caso (Worst-case)

Ao analisarmos um Algoritmo, é muito comum considerarmos o **Pior caso (Worst-case)** possível.

> **O pior caso é quando o maior número de instruções é executado.**

No nosso Algoritmo **Pior caso (Worst-case)** ocorre quando o array possui valores em ordem crescente:
 - O valor de **"M"** é sempre substituído;
 - E o *laço for()* sempre executa as 2 Instruções de dentro **"n"** vezes.

Assim, a função de custo do Algoritmo será:

![image](images/tn-02.png)  

**NOTE:**  
Essa função representa o custo do Algoritmo em relação ao tamanho do array **A** **("n")** no **Pior caso (Worst-case)**

---

**Rodrigo Leite -** *Software Engineer*
