# Design and Analysis of Algorithms

## Contents

 - [Asymptotic Analysis (+Example)](#intro-to-aa)
 - **Types of Asymptotic Notations:**
   - [Big(O), Worst-Case](#big-o-notation)
   - [Omega(Ω), Best Case](#omega-notation)
   - [Theta(Θ), Average Case](#theta-notation)
 - **Math for Algorithms:**
   - **Logarithms:**
     - [Intro to Logarithms](#intro-to-log)
 - [**References**](#ref)








































<!--- ( Asymptotic Analysis (+Example) ) -->

---

<div id="intro-to-aa"></div>

## Asymptotic Analysis (+Example)

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








































<!--- ( Math for Algorithms ) -->

---

<div id="intro-to-log"></div>

## Intro to Logarithms

> **Logarithms are the opposite of exponentials.**

 - Just as *subtraction* is the opposite of *addiction*;
 - And *division* is the opposite of *multiplication*;
 - **Logarithms** is the *opposite* of **exponentials**.

> Technically speaking (tecnicamente falando), `log functions are the inverses of exponential functions`.

For example, see the image below to understand more easily:

![img](images/log-gif-01.gif)

> **NOTE:**  
> We read the formula above as **"Log of x in base b", log<sub>b</sub>(x)**.








































<!--- ( References ) -->

---

<div id="ref"></div>

## References

 - **Asymptotic Analysis and Notations (Based on input size):**
   - [[ED] Aula 101 - Análise de Algoritmos - Comportamento Assintótico](https://www.youtube.com/watch?v=SClFMUpBiaw&list=PL8iN9FQ7_jt6buW7SBD3yzjIp8NnJYrZl&index=3)
   - [How to Analyse Loops for Complexity Analysis of Algorithms](https://www.geeksforgeeks.org/analysis-of-algorithms-set-4-analysis-of-loops/)
   - [Worst, Average and Best Case Analysis of Algorithms](https://www.geeksforgeeks.org/worst-average-and-best-case-analysis-of-algorithms/)
   - [Time Complexity Analysis](https://log2base2.com/courses/time-complexity-analysis)
 - **Math for Algorithms:**
   - ["The Relationship" for Logarithms](https://www.purplemath.com/modules/logs.htm)
   - [Logarithms](https://www.interviewcake.com/article/java/logarithms)
   - [Intro to Maths for CS: Logarithms](https://www.cs.bham.ac.uk/~jdk/Modules/LecSlides/logs.pdf)
   - [Logarithmic Time Complexity](https://www.baeldung.com/cs/logarithmic-time-complexity)
   - [Logarithms and Exponents in Complexity Analysis](https://towardsdatascience.com/logarithms-exponents-in-complexity-analysis-b8071979e847)
   - [7.14. Search Tree Analysis](https://runestone.academy/ns/books/published/pythonds/Trees/SearchTreeAnalysis.html)
   - [Analysis of Recursion in Programming](https://afteracademy.com/blog/analysis-of-recursion-in-programming/)
   - [Deeply Understanding Logarithms In Time Complexities & Their Role In Computer Science](https://www.youtube.com/watch?v=M4ubFru2O80)
   - [O(log n) – Logarithmic time complexity explained](https://www.youtube.com/shorts/IvkgJR_5PkQ)
   - [Big O Notation Series #4: The Secret to Understanding O (log n)!](https://www.youtube.com/watch?v=wjDY5RbILno)
   - [Big O Notation Series #5: O (n log n) explained for beginners](https://www.youtube.com/watch?v=K3NluEdHkao)
   - [Big O Notation Series #9: Understanding Merge Sort](https://www.youtube.com/watch?v=HrCPqJHQSxY)
   - [Big O Notation Series #10: Log n Complexity Explained With An Iterative Function [Logarithmic time]](https://www.youtube.com/watch?v=SfygqfMVSgw)
   - [Big O Notation Series (Coding): Merge Sort Made Easy](https://www.youtube.com/watch?v=PRoqMgTcVGs&list=PL7g1jYj15RUPVZDU9C276SZvlJjf4hzqV&index=13)
   - [Big O Notation Series (Coding): O(log n) Time Complexity Analysis (Recursive Binary Search)](https://www.youtube.com/watch?v=0js3mqa9ChA&list=PL7g1jYj15RUPVZDU9C276SZvlJjf4hzqV&index=15)
   - [Big O Notation Series (Coding): Hands On With O(n) and O(1) Time Complexity Analysis](https://www.youtube.com/watch?v=H03eIiYMc6w)
   - [Big O Notation Series #2: Visualizing Big O of N Squared](https://www.youtube.com/watch?v=0eCT74f5hGA)
   - [Big O Notation Series #3: Visualizing O of N Cubed](https://www.youtube.com/watch?v=IBddtmZBSEA)
   - [Big O Notation Series #7: Time Complexity Visualization of Recursive Fibonacci](https://www.youtube.com/watch?v=AQp1OG7aSwg)
   - [Big O Notation Series #6: Big O of N Factorial](https://www.youtube.com/watch?v=vbh8t-ok_4E)
   - [Logarithms in Time Complexity Data Structure Video-9](https://www.youtube.com/watch?v=FDgjwbAu3Ig)
   - [Big O Notation Series #8: Space Complexity and Big O Gotchas](https://www.youtube.com/watch?v=rHM3zWgnPVA&list=PL7g1jYj15RUPVZDU9C276SZvlJjf4hzqV&index=10)

---

Ro**drigo** **L**eite da **S**ilva - **drigols**
