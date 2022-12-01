# Counting instructions (In Algorithms)

## Contents

 - [Simple Instructions](#simple-instructions)
 - [02 - Pior caso (Worst-case)](#worst-case)

<div id="simple-instructions"></div>

## Simple Instructions

To analyze an Algorithm we need count how many instructions the Algorithm run. Knowing, Knowing this, let's start counting **simple instructions**:

> **A simple instruction is an instruction that can be run directly by the CPU or something close to that.**

 - **Instruction types:**
   - Assign a value to a variable.
   - Access the value (element) of the determined array.
   - Compare Arrays.
   - Increment a value.
   - Arithmetic Operations:
     - Add
     - Sub
     - Div
     - Mult
 - **Let's assume that:**
   - The instructions have the same cost.
   - The selections command has zero (0) cost.

For example, imagine we have an Algorithm that receive an **Array "A"** with **"n"** elements and store the higher element into **"M"** variable:

```cpp
01 int M = A[0];
02 for(int i = 0; i < n; i++)
03     if (A[i] >= M)
04         M = A[i];
```

Now, let's count how many **simple instructions** the Algorithm above running:

**Line 01:**
```cpp
                                Cost:     Times:
01 int M = A[0];                c1        1
02 for(int i = 0; i < n; i++)
03     if (A[i] >= M)
04         M = A[i];
```

**Cost to INITIALIZE the for() (line2) instruction is 2:**
 - The **for()** instruction need be initialized:
   - 1 Instruction: **int i = 0**.
 - And same that the **Array A** have size zero (0) at least (ao menos) one comparison will be run:
   - **i < n**; That is, more 1 instruction.
```cpp
                                Cost:     Times:
01 int M = A[0];                c1        1
02 for(int i = 0; i < n; i++)   c2        2
03     if (A[i] >= M)
04         M = A[i];
```

**Cost to RUN the for() (line 2) instruction is 2n:**
 - At the end (ao final) of each iteration of the *for() loop*, we need:
   - Increment:
     - **"i++"**
   - And an instruction to compare if the loop will continue:
     - **"i < n"**
 - The loop will be run **"n"** time, that is, the **2 instructions** above will be run **"n"** times:
   - **+ 2n (Instructions)**.
```cpp
                                Cost:     Times:
01 int M = A[0];                c1        1
02 for(int i = 0; i < n; i++)   c2        2 + 2n
03     if (A[i] >= M)
04         M = A[i];
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

**Coming soon...**  
01.
https://inst.eecs.berkeley.edu/~cs61b/sp06/labs/s7-2-1.html#:~:text=An%20alternative%20to%20timing%20a,coded%20in%20closely%20related%20languages

02
https://www.google.com/search?q=Counting+statements&sxsrf=ALiCzsarI_6oY5Wwq4DXtJJqY_sdkdp3EQ%3A1669683354593&ei=mliFY8bzI8vh1sQP2LSb6Ao&ved=0ahUKEwjGqPOZl9L7AhXLsJUCHVjaBq0Q4dUDCA8&uact=5&oq=Counting+statements&gs_lcp=Cgxnd3Mtd2l6LXNlcnAQAzIICAAQFhAeEAoyBQgAEIYDMgUIABCGAzIFCAAQhgMyBQgAEIYDOgoIABBHENYEELADOgUIABCRAjoECAAQQzoFCC4QkQI6BQgAEIAEOggILhCABBDUAjoHCAAQgAQQCjoGCAAQFhAeSgQIQRgASgQIRhgAUNAEWLYbYLAdaAJwAXgAgAG5AYgBvgySAQQwLjEwmAEAoAEByAEIwAEB&sclient=gws-wiz-serp


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

**REFERENCES:**  
[]()  

---

Ro**drigo** **L**eite da **S**ilva - **drigols**
