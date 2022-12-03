# Counting Statements

## Contents

 - [Statement (simple) Counting](#statement-counting)
 - [Worst Case Approach](#worst-case)

<div id="statement-counting"></div>

## Statement (simple) Counting

To analyze an Algorithm we need count how many statements the Algorithm run. Knowing this, let's start counting **simple statements**:

> **A simple statements is an statements that can be run directly by the CPU or something close to that.**

 - **Statements types:**
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
   - The statements have the same cost.
   - The *selections command* has zero (0) cost.

For example, imagine we have an Algorithm that receive an **Array "A"** with **"n"** elements and store the higher element into **"M"** variable:

```cpp
01 int M = A[0];
02 for(int i = 0; i < n; i++)
03     if (A[i] >= M)
04         M = A[i];
```

Now, let's count how many **simple statements** the Algorithm above running:

**Line 01:**
```cpp
                                Cost:     Times:
01 int M = A[0];                c1        1
02 for(int i = 0; i < n; i++)
03     if (A[i] >= M)
04         M = A[i];
```

**Cost to INITIALIZE the for() (line2) statements is 2:**
 - The **for()** statements need be initialized:
   - 1 statements: **int i = 0**.
 - And same that the **Array A** have size zero (0) at least (ao menos) one comparison will be run:
   - **i < n**; That is, more 1 statements.
```cpp
                                Cost:     Times:
01 int M = A[0];                c1        1
02 for(int i = 0; i < n; i++)   c2        2
03     if (A[i] >= M)
04         M = A[i];
```

**Cost to RUN the for() (line 2) statements is 2n:**
 - At the end (ao final) of each iteration of the *for() loop*, we need:
   - Increment:
     - **"i++"**
   - And an statements to compare if the loop will continue:
     - **"i < n"**
 - The loop will be run **"n"** time, that is, the **2 statements** above will be run **"n"** times:
   - **+ 2n (statements)**.
```cpp
                                Cost:     Times:
01 int M = A[0];                c1        1
02 for(int i = 0; i < n; i++)   c2        2 + 2n
03     if (A[i] >= M)
04         M = A[i];
```

**NOTE:**  
Ignoring commands inside **for()** statement, the algorithm has **3 +2n** statements.

 - **3** statements before initialize **for()** statements.
 - **2** Statements at the end of each **for()** loop, which will be executed **"n"** times.

Thus, considering an *empty loop (for)*, we can define a mathematical function that represents the cost of the Algorithm in relation to the size of the input array as:

![image](images/tn-01.png)  

Ok, but what about the statements inside the **for() loop** how do we count?

 - The **if()** statement has 1 comparison statement: **(A[i] >= M)**;
 - And inside the **if()** we have 1 more assignment statement: **M = A[i]**.

```cpp
                                     Cost:     Times:
01 int M = A[0];                     c1        1
02 for(int i = 0; i < n; i++)        c2        2 + 2n
03     if (A[i] >= M)                c3        1 (How many times?)
04         M = A[i];                 c4        1 (How many times?)
```

> **PROBLEM:**  
> Well, now we have a little problem, how many times will these statements be executed?

 - statements seen previously were always executed;
 - However, the statements inside *for()* may or may not be executed.

That is, before it was enough to know the size of array **A**, **"n"**, to define the cost function **T(n)**. Now we also need to consider the contents of the array. For example, look at the two arrays below:


```cpp
01 A1 = [1, 2, 3, 4]
02 A2 = [4, 3, 2, 1]
```

 - Array **A1** will have more statements, because the **if()** will always be true;
 - And the **A2** array will have less statements because the **if()** will always be false.

---

<div id="worst-case"></div>

## Worst Case Approach

When analyzing an Algorithm, it is very common to consider the **worst case possible**.

> **The *Worst Case* is when the Algorithm executes as many statements as possible.**

In our Algorithm **Worst Case** occurs when the array has values in *ascending order*:

 - The value of **"M"** is always substituted;
 - And the **for() loop** always executes the 2 inside statements **"n"** times.

Thus, the cost function of the Algorithm will be:

![image](images/tn-02.png)  

**NOTE:**  
This function represents the cost of the Algorithm in relation to the size of the array **A ("n")** in the **Worst case**.

---

**REFERENCES:**  
[]()  

---

Ro**drigo** **L**eite da **S**ilva - **drigols**
