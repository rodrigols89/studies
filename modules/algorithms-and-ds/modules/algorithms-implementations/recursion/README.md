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

 - **1. A recursive algorithm must have a *base case*:**
   - Um algoritmo recursivo deve ter um *caso base*.
 - **2. A recursive algorithm must change its state and move toward the base case:**
   - Um algoritmo recursivo deve mudar seu estado e se mover em direção ao caso base.
 - **3. A recursive algorithm must call itself, recursively:**
   - Um algoritmo recursivo deve chamar a si mesmo, recursivamente.

To understand how to solve problems using *Recursion*, let's imagine that we need to sum all the elements of a given list, like this below:

```bash
[1, 3, 5, 7, 9]
```

If you think mathematically you can parenthesize this list, making an add algebraic expression.

For example:

![img](images/recursion-01.png)  

> **NOTE:**  
> Notice that the innermost (mais interno) set of parentheses, *(7 + 9)*, is a problem that we can solve without a loop or any special constructs.

In fact, we can use the following sequence of simplifications to compute a final sum:

![img](images/recursion-02.png)  

Another approach to solve this is using iterative programming (using a loop). For example, see the function implementation below:

**Python:** [iterative_sum.py](src/python/iterative_sum.py)
```python
def sumElements(myList):
    sum = 0                 # O(1)
    for element in myList:  # O(n)
        sum += element      # O(1)    
    return sum              # O(1)


if __name__ == "__main__":
    myList = [1, 3, 5, 7, 9]
    print("The sum of all element is:", sumElements(myList))
```

**OUTPUT:**
```bash
The sum of all element is: 25
```

$f(n) = O(1) + O(n) + O(1) + O(1) = O(n)$
$f(n) = O(n)$

### Complexity Explanation

 - `sum = 0`
   - Assigning a value to a variable is a constant-time operation, O(1).
 - `for element in myList:`
   - The for() loop iterates over the elements of myList, which has "n" elements. The loop body executes once for each element, resulting in a total of "n" iterations. Therefore, the complexity of this line is **O(n)**.
 - `sum += element`
   - The addition operation `(sum += element)` is also a constant-time operation, **O(1)**.
 - `return sum`
   - Returning a value from a function is typically a constant-time operation, **O(1)**.
 - **NOTE:**  So, the *Time Complexity* in the *Worst Case* is **O(n)**:
   - That's, *Linear Time Complexity*.

> **Now, how we can solve that using Recursion?**

First, we need to consider the ***"Three Laws of Recursion"***.

 - **1. A recursive algorithm must have (deve ter) a *base case*:**
   - First, a *base case* is the condition that allows the algorithm to stop recursing.
   - In the sumElements() algorithm (function) the base case is a list of length 1.
 - **2. A recursive algorithm must change (deve mudar) its state and move toward the base case:**
   - To obey (para obedecer) the second law, we must arrange (devemos providenciar) for a change of state that moves the algorithm toward the base case.
   -  A change of state means that some data that the algorithm is using is modified.
   - Usually the data that represents our problem gets smaller (ficam menores) in some way (de alguma forma).
   - In the sumElements() algorithm (function) our primary data structure is a *list*, so we must focus our state-changing efforts on the list.
   - Since (como) the *base case* is a *list of length 1*, a natural progression toward the base case is to shorten the list.
 - **3. A recursive algorithm must call itself, recursively:**
   - The final law is that the algorithm (function) must call itself (deve chamar ela mesmo).

Let's see this in practice:

**Python:**
```python
def sumElementsRecursive(myList):
    if len(myList) == 1:                                   # O(1)
        return myList[0]                                   # O(1)
    else:
        lastElement = myList[-1]                           # O(1)
        newList = myList[:-1]                              # O(n)
        sum = lastElement + sumElementsRecursive(newList)  # O(n)
        return sum                                         # O(1)


if __name__ == "__main__":
    myList = [1, 3, 5, 7, 9]
    print("The sum of all element is:", sumElementsRecursive(myList))
```

$f(n) = O(1) + O(1) + O(1) + O(n) + O(n) + O(1)$
$f(n) = O(n)$

### Complexity Explanation

 - **The *recursive* function above sums all the elements in a list:**
   - In each recursive call, the function removes the last element from the list and adds it to the "sum" variable.
   - This process continues until the list has only one element.
   - Since the function makes a recursive call for each element in the list, the time complexity is **O(n)**, where **"n"** is the number of elements in the list.
 - `if len(myList) == 1:`
   - Checking the length of the list is a constant-time operation *O(1)*. It involves a simple comparison and doesn't depend on the size of the list.
 - `return myList[0]`
   - Returning the first element of the list is a constant-time operation O(1). It directly accesses a known memory location.
 - `lastElement = myList[-1]`
   - Accessing the last element of the list is a constant-time operation O(1). It involves index-based access.
 - `newList = myList[:-1]`
   - Creating a new list without the last element is a linear time operation *O(n)*, where "n" is the length of the original list. It creates a new list and copies elements.
 - `sum = lastElement + sumElementsRecursive(newList)`
   - Recursively summing elements has a time complexity that depends on the size of the list. In the worst case, it is *O(n)*, where "n" is the length of the list.
 - `return sum`
   - Returning the sum is a constant-time operation O(1). It involves a simple return statement and doesn't depend on the size of the list.

Now, let's test in the practice:

**Python:** [recursive_sum.py](src/python/recursive_sum.py)
```python
def sumElementsRecursive(myList):
    if len(myList) == 1:  # Base case.
        return myList[0]
    else:
        lastElement = myList[-1]  # Get the last element.
        newList = myList[:-1]  # Remove the last element from the list.
        sum = lastElement + sumElementsRecursive(newList)  # Recursive call.
        return sum


if __name__ == "__main__":
    myList = [1, 3, 5, 7, 9]
    print("The sum of all element is:", sumElementsRecursive(myList))
```

**OUTPUT:**
```bash
The sum of all element is: 25
```

> **NOTE:**  
> However, this approach has to be used with caution for large "n" data sets. This is because it can overflow the call stack.

![img](images/stackoverflow-01.png)  




































































































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
