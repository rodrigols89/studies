# Recursion

## Contents

 - **Concepts:**
   - [Intro to Recursion](#intro-to-recursion)
   - [The problem of summing elements of a list](#initial-problem)
   - [The three laws of Recursion](#recursion-laws)
 - [References](#ref)

<!--- ( Concepts ) --->

---

<div id="intro-to-recursion"></div>

## Intro to Recursion

 - **EN -** The *Recursion* is a method of solving problems that involves breaking a problem down into smaller and smaller subproblems until you get to a small enough problem that it can be solved trivially:
   - Usually recursion involves a function calling itself.
 - **PT -** A *Recursão* é um método de resolver problemas que envolve dividir um problema em subproblemas cada vez menores até chegar a um problema pequeno o suficiente para que possa ser resolvido trivialmente:
   - Normalmente, a recursão envolve uma função chamando a si mesma.

---

<div id="initial-problem"></div>

## The problem of summing elements of a list

To understand how to solve problems using Recursion, let's imagine that we need to sum all the elements of a given list, like this below:

```bash
[1, 3, 5, 7, 9]
```

If you think mathematically you can parenthesize this list, making an add algebraic expression. For example:

![img](images/recursion-01.png)  

Notice that the innermost (mais interno) set of parentheses, *(7 + 9)*, is a problem that we can solve without a loop or any special constructs. In fact, we can use the following sequence of simplifications to compute a final sum:

![img](images/recursion-02.png)  

Another approach to solve this is using iterative programming (using a loop). For example, see the function implementation below:

**C++:** [driver_sumElements_iterative_approach.cpp](src/cpp/driver_sumElements_iterative_approach.cpp)
```cpp
#include <iostream>
#include <vector>

int sumElements(std::vector<int> list)
{
    int sum = 0;
    for (int element : list)
        sum += element;
    return sum;
}

int main()
{
    std::vector<int> myList = {1, 3, 5, 7, 9};
    std::cout << "The sum of all element is: " << sumElements(myList);
    return 0;
}
```

**COMPILATION AND RUN:**
```bash
g++ driver_sumElements_iterative_approach.cpp -o test.out && ./test.out
```

**OUTPUT:**
```bash
The sum of all element is: 25
```

**Python:** [driver_sumElements_iterative_approach.py](src/python/driver_sumElements_iterative_approach.py)
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

**INTPUT:**
```bash
python driver_sumElements_iterative_approach.py
```

**OUTPUT:**
```bash
The sum of all element is: 25
```

The **Time Complexity** of the **sumElements()** function is:

 - **Time Complexity:**
   - **[Worst Case] - Big O(O)** 
     - **O(n):** In the *worst case*, the time complexity of this function is **O(n)**, where **"n"** is the number of elements in the vector. This happens when the vector is completely filled, and we need to iterate over all the elements to perform the sum. In this case, the function has to iterate over each element of the vector once, adding them to the total sum.
   - **[Best Case] - Omega (Ω)**
     - **Ω(1):** In the *best case*, the time complexity is O(1), which occurs when the vector:
       - The list empty.
       - The list has only 1 element.
       - In these two cases, we have a constant *Time Complexity*.
   - **[Average Case] - Theta (Θ)**
     - **Θ(n):** In the *average case*, the time complexity is also **O(n)**, assuming that the distribution of elements in the vector is random. The function still needs to iterate over each element of the vector once, adding them to the total sum.

---

<div id="recursion-laws"></div>

## The three laws of Recursion

Like the robots of Asimov, all recursive algorithms must obey (devem obedecer) three important laws:

 - **1. A recursive algorithm must have (deve ter) a *base case*:**
   - Um algoritmo recursivo deve ter um *caso base*.
 - **2. A recursive algorithm must change (deve mudar) its state and move toward the base case:**
   - Um algoritmo recursivo deve mudar seu estado e se mover em direção ao caso base.
 - **3. A recursive algorithm must call itself (deve chamar a si mesmo), recursively:**
   - Um algoritmo recursivo deve chamar a si mesmo, recursivamente.

Back to our [**Problem of calculating the sum of a list of numbers**](#initial-problem) we can use the *"The three laws of Recursion"* to try to solve using Recursion.

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

**C++:**
```cpp
int sumElementsRecursive(std::vector<int> list)
{
    if (list.size() == 1) {  // Base case.
        return list[0];
    }
}
```

**Python:**
```python
def sumElementsRecursive(myList: list[int]) -> int:
    if len(myList) == 1:  # Base case.
        return myList[0]
```

Following the second law, now we need to **change the state to go toward (para ir em direção)** the base **case**:

> **NOTE:**  
> Remember, that, a change of state means that some data that the algorithm is using is modified. For our case, the list is modified toward the base.

**C++:**
```cpp
int sumElementsRecursive(std::vector<int> list)
{
    if (list.size() == 1) {  // Base case.
        return list[0];
    } else {
        int lastElement = list.back();  // Get the last element.
        list.pop_back();  // Remove the last element from the list.
    }
}
```

**Python:**
```python
def sumElementsRecursive(myList: list[int]) -> int:
    if len(myList) == 1:  # Base case.
        return myList[0]
    else:
        lastElement = myList[-1]  # Get the last element.
        newList = myList[:-1]  # Remove the last element from the list.
```

**NOTE:**  
See that we are removing the last element, that's, we are changing the state to go toward (para ir em direção) the base case, list size = 1.

Finally, following the third law, we need to call the algorithm (function) itself.

**C++:**
```cpp
int sumElementsRecursive(std::vector<int> list)
{
    if (list.size() == 1) {  // Base case.
        return list[0];
    } else {
        int lastElement = list.back();  // Get the last element.
        list.pop_back();  // Remove the last element from the list.
        int sum = lastElement + sumElementsRecursive(list);  // Recursive call.
        return sum;
    }
}
```

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

See, the complete code to **sumElementsRecursive()** algorithms (function) below:

**C++:** [driver_sumElements_recursive_approach.cpp](src/cpp/driver_sumElements_recursive_approach.cpp)
```cpp
#include <iostream>
#include <vector>

int sumElementsRecursive(std::vector<int> list)
{
    if (list.size() == 1) {  // Base case.
        return list[0];
    } else {
        int lastElement = list.back();  // Get the last element.
        list.pop_back();  // Remove the last element from the list.
        int sum = lastElement + sumElementsRecursive(list);  // Recursive call.
        return sum;
    }
}

int main()
{
    std::vector<int> myList = {1, 3, 5, 7, 9};
    std::cout << "The sum of all element is: " << sumElementsRecursive(myList);
    return 0;
}
```

**COMPILATION AND RUN:**
```bash
g++ driver_sumElements_recursive_approach.cpp -o test.out && ./test.out
```

**OUTPUT:**
```bash
The sum of all element is: 25
```

**Python:** [driver_sumElements_recursive_approach.py](src/python/driver_sumElements_recursive_approach.py)
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

**INTPUT:**
```bash
python driver_sumElements_recursive_approach.py
```

**OUTPUT:**
```bash
The sum of all element is: 25
```

The **Time** and **Space complexity** of the **sumElementsRecursive()** algorithm (function) is:

 - **Time Complexity:**
   - **[Worst Case] - Big O(O)** 
     - **O(n):** The *worst-case time complexity* occurs when the function needs to iterate through all the elements of the list. In this case, the function will make a recursive call for each element of the list, resulting in complete recursion. Therefore, the worst-case time complexity is **O(n)**, where **"n"** is the number of elements in the list.
   - **[Best Case] - Omega (Ω)**
     - **Ω(1):** The *best-case time complexity* occurs when the function reaches (atinge) the base case immediately, i.e., when the list has only one element. In this case, the function returns the value of the single element without the need for recursive calls. Therefore, the *best-case time complexity* is **O(1)**, as the execution time is *constant*.
   - **[Average Case] - Theta (Θ)**
     - **Θ(n):** The *average-case time complexity* depends on the distribution of input list sizes. If we assume a uniform distribution of input lists, each list size has an equal probability of occurrence. In this case, the *average time complexity* will be a weighted average of the time complexities for different list sizes. Therefore, the average time complexity is **O(n)**, where **"n"** is the average size of the input list.








































<!--- ( References ) --->

---

<div id="ref"></div>

## References

 - [Problem Solving with Algorithms and Data Structures using Python](https://runestone.academy/ns/books/published/pythonds/index.html)

---

Ro**drigo** **L**eite da **S**ilva - **drigols**
