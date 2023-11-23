# Recursion

## Contents

 - **Basics:**
   - [Intro to Recursion (Laws of Recursion + Example of sum numbers in a list)](#intro-and-recursion-laws)
 - [References](#ref)








































<!--- ( Basics ) --->

---

<div id="intro-and-recursion-laws"></div>

## Intro to Recursion (Laws of Recursion + Example of sum numbers in a list)

Like the robots of Asimov, all recursive algorithms must obey (devem obedecer) three important laws:

 - **1. A recursive algorithm must have (deve ter) a *base case*:**
   - Um algoritmo recursivo deve ter um *caso base*.
 - **2. A recursive algorithm must change (deve mudar) its state and move toward (em direção) the base case:**
   - Um algoritmo recursivo deve mudar seu estado e se mover em direção ao caso base.
 - **3. A recursive algorithm must call itself (deve chamar a si mesmo), recursively:**
   - Um algoritmo recursivo deve chamar a si mesmo, recursivamente.

To understand how to solve problems using Recursion, let's imagine that we need to sum all the elements of a given list, like this below:

```bash
[1, 3, 5, 7, 9]
```

If you think mathematically you can parenthesize this list, making an add algebraic expression. For example:

![img](images/recursion-01.png)  

> **NOTE:**  
> Notice that the innermost (mais interno) set of parentheses, *(7 + 9)*, is a problem that we can solve without a loop or any special constructs.

In fact, we can use the following sequence of simplifications to compute a final sum:

![img](images/recursion-02.png)  

Another approach to solve this is using iterative programming (using a loop). For example, see the function implementation below:

**Python:**
```python
def sumElements(myList: list[int]) -> int:
    sum = 0
    for element in myList:
        sum += element
    return sum


if __name__ == "__main__":
    myList: list[int] = [1, 3, 5, 7, 9]
    print("The sum of all element is:", sumElements(myList))
```

**OUTPUT:**
```bash
The sum of all element is: 25
```

> **Now, how we can solve that using Recursion?**

First, we need to consider the ***"Three Laws of Recursion"***.

 - **1. A recursive algorithm must have (deve ter) a *base case*:**
   - First, a *base case* is the condition that allows the algorithm to stop recursing.
   - In the sumElements() algorithm (function) the base case is a list of length 1.
 - **2. A recursive algorithm must change (deve mudar) its state and move toward the base case:**
   - To obey (para obedecer) the second law, we must arrange (devemos providenciar) for a change of state that moves the algorithm toward (em direção) the base case.
   -  A change of state means that some data that the algorithm is using is modified.
   - Usually the data that represents our problem gets smaller (ficam menores) in some way (de alguma forma).
   - In the sumElements() algorithm (function) our primary data structure is a *list*, so we must focus our state-changing efforts on the list.
   - Since (como) the *base case* is a *list of length 1*, a natural progression toward (em direção) the base case is to shorten the list.
 - **3. A recursive algorithm must call itself (deve chamar a si mesmo), recursively:**
   - The final law is that the algorithm (function) must call itself (deve chamar ela mesmo).

Following these laws, let's get started with the **base case (first law)**, that's, the recursion stop when the *list size = 1*:

**Python:**
```python
def sumElementsRecursive(myList: list[int]) -> int:
    if len(myList) == 1:  # Base case.
        return myList[0]
```

Following the second law, now we need to **change the state to go toward (para ir em direção)** the base **case**:

> **NOTE:**  
> Remember, that, a change of state means that some data that the algorithm is using is modified. For our case, the list is modified toward the base.

**Python:**
```python
def sumElementsRecursive(myList: list[int]) -> int:
    if len(myList) == 1:  # Base case.
        return myList[0]
    else:
        lastElement = myList[-1]  # Get the last element.
        newList = myList[:-1]  # Remove the last element from the list.
```

> **NOTE:**  
> See that we are removing the last element, that's, we are changing the state to go toward (para ir em direção) the *base case*, list size = 1.

Finally, following the third law, we need to call the algorithm (function) itself.

**Python:**
```python
def sumElementsRecursive(myList: list[int]) -> int:
    if len(myList) == 1:  # Base case.
        return myList[0]
    else:
        lastElement = myList[-1]  # Get the last element.
        newList = myList[:-1]  # Remove the last element from the list.
        sum = lastElement + sumElementsRecursive(newList)  # Recursive call.
        return sum
```

Now, let's test in the practice:

**Python:**
```python
def sumElementsRecursive(myList: list[int]) -> int:
    if len(myList) == 1:  # Base case.
        return myList[0]
    else:
        lastElement = myList[-1]  # Get the last element.
        newList = myList[:-1]  # Remove the last element from the list.
        sum = lastElement + sumElementsRecursive(newList)  # Recursive call.
        return sum


if __name__ == "__main__":
    myList: list[int] = [1, 3, 5, 7, 9]
    print("The sum of all element is:", sumElementsRecursive(myList))
```

**OUTPUT:**
```bash
The sum of all element is: 25
```








































<!--- ( References ) --->

---

<div id="ref"></div>

## References

 - [Problem Solving with Algorithms and Data Structures using Python](https://runestone.academy/ns/books/published/pythonds/index.html)
 - [Difference between Recursion and Iteration](https://www.geeksforgeeks.org/difference-between-recursion-and-iteration/)
 - [Finite and Infinite Recursion with examples](https://www.geeksforgeeks.org/finite-and-infinite-recursion-with-examples/)
 - [Difference Between Recursion and Induction](https://www.geeksforgeeks.org/difference-between-recursion-and-induction/)
 - [How to analyse Complexity of Recurrence Relation](https://www.geeksforgeeks.org/how-to-analyse-complexity-of-recurrence-relation/)
 - [What is Recursion?](https://www.geeksforgeeks.org/what-is-recursion/)

---

Ro**drigo** **L**eite da **S**ilva - **drigols**
