# Asymptotic Analysis

## Contents

 - **Concepts:**
   - [Intro to Asymptotic Analysis (+Example)](#intro-to-aa)
 - **Types of Asymptotic Notations:**
   - [Big(O), Worst-Case](#big-o-notation)
   - [Omega(Ω), Best Case](#omega-notation)
   - [Theta(Θ), Average Case](#theta-notation)
 - **Asymptotic Classes:**
   - **[Constant, O(1)](#intro-to-constant-approach)**
   - **[Logarithmic, O(log n)](#intro-to-logarithmic-approach)**
   - **[Linear, O(n)](#intro-to-linear-approach)**
   - **[Loglinear, O(n log n)](#intro-to-loglinear-approach)**
   - **[Quadratic, O(n^2)](#intro-to-quadratic-approach)**
   - **[Polynomial, O(n^k)](#intro-to-polynomial-approach)**
   - **[Exponential, O(a^n) or O(b^n)](#intro-to-exponential-approach)**
   - **[Fatorial, O(n!)](#into-to-fatorial-approach)**
 - [**References**](#ref)








































<!--- ( Concepts ) -->

---

<div id="intro-to-aa"></div>

## Intro to Asymptotic Analysis (+Example)

> **Given two algorithms "g" and "h" for the same task, how do we find out which one is better?**

One naive (ingênua) way of doing this is – to implement both algorithms and run the two programs on your computer for different inputs and see which one takes less time.

**NOTE:**  
However, there are many problems with this approach for the analysis of algorithms.

 - It might be possible that for some inputs, the algorithm **"g"** performs better than the algorithm **"h"**.
 - And for another input, the algorithm **"h"** performs better than the algorithm **"g"**.
 - **NOTE:** For example, a search algorithm depends on how the data (elements) are distributed. Is the searched element at the beginning, middle, or end of the list?

Asymptotic Analysis is the big idea *that handles (que lida)* the above issues in analyzing algorithms:

 - In *Asymptotic Analysis*, we evaluate the performance of an algorithm in **terms of input size**.
 - We calculate how the time (or space) for an algorithm *increases as (aumenta a medida que)* the input size increases.

To understand more easily, imagine that the Algorithms **"g"** and **"h"** are the following functions:

![image](images/asymptotic-analysis-01.png)  

Some importants points here are:

 - **The "g" function has constants with greater values than the "h" function**
   - *Constants of the "g" function:* 100 and 500.
   - *Constants of the "h" function:* 1
 - **However, the "h" function has variables with orders of magnitude (magnitude) greater than the "g" function:**
   - *"g" function variables:* n
   - *"h" function variables:* n and n<sup>2</sup>

Now, let's test some **"n"** values to the functions (Algorithms) **g(n)** and **h(n)**:

 - **n = 10**
   - g(n): 10.500
   - h(n): 111
 - **n = 100**
   - g(n): 100.500
   - h(n): 10.101
 - **n = 1.000**
   - `g(n): 1.000.500` ←
   - `h(n): 1.001.001` ←
 - **n = 1.500**
   - g(n): 1.500.500
   - h(n): 2.251.501
 - **n = 2.000**
   - g(n): 2.000.500
   - h(n): 4.002.001
 - **n = 2.500**
   - g(n): 2.500.500
   - h(n): 6.252.501
 - **n = 3.000**
   - g(n): 3.000.500
   - h(n): 9.003.001
 - **n = 3.500**
   - g(n): 3.500.500
   - h(n): 12.253.501

Some important points here are:

 - For **"n >= 1000"** the function (algorithm) **h(n)** will always be greater than the function (algorithm) **g(n)**.
 - Although (embora/apesar) the function **g(n)** has higher constants multiplying (1000 and 500) your terms, there exists a value to **"n"** where the function (algorithms) **h(n)** will always be greater than the **g(n)** function.

> **NOTE:**  
> Therefore (portanto), *Asymptotic Analysis* **focuses on terms of input size**, **not constant values**.

For example, let's see other functions (algorithms) and their Asymptotic Analysis:

![image](images/asymptotic-analysis-02.png)  

> **NOTE:**  
> Note that the focus is always the largest term of the function.









































<!--- ( Types of Asymptotic Notations ) -->

---

<div id="big-o-notation"></div>
 
## Big(O), Worst-Case

> The **Big(O) notation (also called Worst-Case)** is the most common approach used to describe the asymptotic complexity of an algorithm.

 - In the **Big(O)**, we calculate the *upper bound* on the running time of an algorithm.
 - **NOTE:** We must know (devemos conhecer) the case that causes *a maximum number of operations to be executed*.

For example, *Linear Search* algorithm, in the **Big(O)** occurs when the element to be searched is not present in the array:

 - When the element is not present, the search() function compares it with all the elements of `arr[]` one by one.
 - Therefore, the worst-case time complexity of the linear search would be **O(n)**.

> **Briefly, the *Big(n)* occurs when the *maximum* number of statements is run!**

---

<div id="omega-notation"></div>

## Omega(Ω), Best Case

> The **Omega(Ω) notation (also called Best Case)** is also a common approach used to describe the asymptotic complexity of an algorithm.

 - In the **Omega(Ω)**, we calculate the *lower bound* on the running time of an algorithm.
 - **NOTE:** We must know (devemos conhecer) the case that causes *a minimum number of operations to be executed*.

For example, in the *Linear Search* algorithm problem, the best case occurs when x is present at the first location:

 - The number of operations in the best case is constant (not dependent on n).
 - So time complexity in the best case would be **Ω(1)**.

> **Briefly, the *Omega(Ω)* occurs when the *minimum* number of statements is run!**

---

<div id="theta-notation"></div>

## Theta(Θ), Average Case

> The **Theta(Θ) notation (also called Average Case)** is the rarely used approach to describing the asymptotic complexity of an algorithm.

 - In **Theta(Θ)**, we take all possible inputs and calculate the computing time (tempo de computação) for all of the inputs.

![img](images/average-case-01.png)








































<!--- ( Asymptotic Classes ) -->

---

<div id="intro-to-constant-approach"></div>

## Constant, O(1)

> An algorithm is considered constant, denoted as **O(1)**, if its execution time remains the same, regardless (independentemente) of the size of the input data.

 - This means that the execution time is not dependent on the size of the input data.
 - In other words, no matter how much data you feed the algorithm, it will always take the same amount of time to complete its operation.
 - *Time complexity:* The time complexity of a constant algorithm is always **O(1)**, which means the execution time is independent of the input size.
 - *Memory complexity:* The memory complexity of a constant algorithm is also usually **O(1)**, as it only needs to store a fixed amount of data.

For example:

![img](images/asymptotic-classes-01.png)

---

<div id="intro-to-logarithmic-approach"></div>

## Logarithmic, O(log n)

> The best of all worlds for algorithms. This class is typical of algorithms that can solve problems by *turning them into smaller problems at each step of the solution*.

Functions whose growth (cujo crescimento) is related to the logarithm of the input variable. For example:

![img](images/asymptotic-classes-02.png)

> **NOTE:**  
> In the example above:
> *"n"* is the input size.
> *"x"* is how many times multiplied by *2*.

---

<div id="intro-to-linear-approach"></div>

## Linear, O(n)

> Very efficient algorithm. The linear class occurs in algorithms that need to process *"n"* input elements and do small computations on those elements.

For example:

![img](images/asymptotic-classes-03.png)

---

<div id="intro-to-loglinear-approach"></div>

## Loglinear, O(n log n)

> Slightly less efficient than linear ones. This is a typical asymptotic class of algorithms that implement the **“Divide and Conquer”** paradigm.

Functions whose growth (cujo crescimento) is the ***product of a linear function and a logarithm***. This is often the case for many efficient sorting algorithms, such as *Merge Sort* and *Heap Sort*.

For examples:

![img](images/asymptotic-classes-04.png)

---

<div id="intro-to-quadratic-approach"></div>

## Quadratic, O(n^2)

> Quadratic order polynomials. This class occurs a lot in algorithms that process information in pairs. Usually in nested loops (one loop inside the other).

![img](images/asymptotic-classes-05.png)

---

<div id="intro-to-polynomial-approach"></div>

## Polynomial, O(n^k)

> They are more efficient than exponentials, but are **only suitable for solving small problems**. When the value of n grows a lot, the algorithm becomes very inefficient.

Functions whose growth (cujo crescimento) is a power of the input variable, where **"k" is a positive constant**.

For example:

![img](images/asymptotic-classes-06.png)

> **NOTE:**  
> See that the **exponent** is **always a positive constant**.

---

<div id="intro-to-exponential-approach"></div>

## Exponential, O(a^n) or O(b^n)

More efficient than factorial, but still **far from being an efficient algorithm (longe de ser um algoritmo eficiente)**. It also occurs in algorithms that use *Brute Force* to solve problems.

> **Exponential O(a^n) or O(b^n), where "a" and "b" are *constants*.**

Functions whose growth (cujo crescimento) is an exponential function of the input variable.

For example:

![img](images/asymptotic-classes-07.png)

> **NOTE:**
> See that difference of polynomial class here the base is always constant and the **exponent is always a positive variable (n)**.

---

<div id="intro-to-fatorial-approach"></div>

## Fatorial, O(n!)

> The worst class of algorithm. It usually occurs in some algorithms that use *Brute Force* technique to solve problems.

Functions whose growth (cujo crescimento) is related to the factorial of the input variable.

For example:

![img](images/asymptotic-classes-08.png)








































<!--- ( References ) -->

---

<div id="ref"></div>

## References

 - [[ED] Aula 101 - Análise de Algoritmos - Comportamento Assintótico](https://www.youtube.com/watch?v=SClFMUpBiaw&list=PL8iN9FQ7_jt6buW7SBD3yzjIp8NnJYrZl&index=3)
 - [How to Analyse Loops for Complexity Analysis of Algorithms](https://www.geeksforgeeks.org/analysis-of-algorithms-set-4-analysis-of-loops/)
 - [Worst, Average and Best Case Analysis of Algorithms](https://www.geeksforgeeks.org/worst-average-and-best-case-analysis-of-algorithms/)
 - [Time Complexity Analysis](https://log2base2.com/courses/time-complexity-analysis)
 - [Asymptotic classes](https://algol.dev/en/asymptotic-classes/)
 - [ChatGPT](https://chat.openai.com/)

---

Ro**drigo** **L**eite da **S**ilva - **drigols**
