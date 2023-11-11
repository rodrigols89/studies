# Stacks (LIFO: Last-In, First-Out)

## Contents

 - **Basics:**
   - [Intro to Stacks](#intro-to-stacks)
   - [Stack class using Array (fixed size) approach](#stack-class-using-array)
   - [x](#)
   - [x](#)
   - [x](#)
   - [x](#)
   - [x](#)
   - [Reverse Stack (e.g. Undo/Redo Operations)](#reverse-stack)
 - **Length or Size:**
 - **Insertion:**
 - **Traversal:**
 - **Deletion:**
 - **Sorting:**
 - **Search:**
 - **Operations by Index:**
 - **Reverse:**
 - **Split:**
 - **Clone or Copy:**
 - **Intersection and Union:**
 - **Detect Loops:**
 - **Concatenation:**
 - **Merge:**
 - **Tips & Tricks:**
   - [The duplicates items issue](#the-duplicates-issue)
 - [REFERENCES](#ref)








---

<!--- ( Basics ) --->

<div id="intro-to-stacks"></div>

## Intro to Stacks

> A **Stack (sometimes called a “push-down stack”)** is a collection of items where the *addition* and *removal* of items always take the *same place*.

See the image below to understand more easily:

![img](images/stack-01.png)  

See that:

 - **The "addition" and "removal" are in the same place**.
 - **The "last item" to enter is referred to as "top":**
   - This item (top) is the first to leave from the Stack.
 - **The "first item" to enter is referred to as "base (or bottom)":**
   - This item (base/bottom) is the last to leave from the Stack.
 - **NOTE: The Stack data structure uses a "LIFO (Last-In, First-Out)" ordering principle.**

Let's see another example of the Stack, however, using animation visualization:

![img](images/stack-gif-01.gif)  

See that:

 - The **"last item"** to enter *(last in)*;
 - Is the **"first item"** to out *(first out)*.
























---

<div id="stack-class-using-array"></div>

## Stack class using Array (fixed size) approach

Here, let's see how to implement a Stack class using an Array (fixed size) approach.

Let's start by understanding the constructor:

**Python:** [stacks.py](src/python/stacks.py)
```python
def __init__(self, size):
    self.size = size
    self.arr = [None] * size
    self.top = -1
```

See that:

 - Here we have instance variables similar (parecidas) to Array class implementation:
   - However, here let's use them to apply Stack concepts (LIFO).
 - The "size" variable is used later to check if the Stack is full or not.
 - The **"top variable"** **represent the index** of the **top item in the Stack**:
   - Knowing that, we start with -1, and when is incremented "+1" is 0.
   - This approach is interesting when we want a variable that needs to represent an index of the array/list.
   - **NOTE: However, we need pay attention:**
     - When we need the index of the element in the Stack use just the "top" variable.
     - When we need to count elements in the Stack we can use **"top+1"**.

Now, let's test in the practice:

**Python:**
```python
from stacks import StackUsingArray

if __name__ == "__main__":

    myStack = StackUsingArray(5)
    myStack.traverse()
```

**OUTPUT:**  
```python
Stack: [None, None, None, None, None]
```

Now, let's see how to add a new item in the Stack, that's, implement **push()** function:

**Python:** [stacks.py](src/python/stacks.py)
```python
def push(self, item):
    # "self.top+1" is used as count, not index.
    if self.top+1 >= self.size:
        print("The Stack is full.")
        return None
    self.top += 1
    self.arr[self.top] = item
```

See that:

 - First, we check if the Stack is full.
 - Next, how do we set the "top variable" as "-1" we need to first increment "+1":
   - This is because if the list (stack) is empty we can't insert at index "-1".
 - Finally, we just need to insert a new element at index "top", **"arr[self.top]"**.

Now, let's test in the practice:

**Python:**
```python
from stacks import StackUsingArray

if __name__ == "__main__":

    myStack = StackUsingArray(5)
    myStack.traverse()
    print("")

    myStack.push(10)
    myStack.traverse()
    print("")

    myStack.push(20)
    myStack.traverse()
    print("")

    myStack.push(30)
    myStack.traverse()
    print("")

    myStack.push(40)
    myStack.traverse()
    print("")

    myStack.push(50)
    myStack.traverse()
```

**OUTPUT:**  
```python
Stack: [None, None, None, None, None]

Stack: [10, None, None, None, None]
Index: 0, Item: 10

Stack: [10, 20, None, None, None]
Index: 0, Item: 10
Index: 1, Item: 20

Stack: [10, 20, 30, None, None]
Index: 0, Item: 10
Index: 1, Item: 20
Index: 2, Item: 30

Stack: [10, 20, 30, 40, None]
Index: 0, Item: 10
Index: 1, Item: 20
Index: 2, Item: 30
Index: 3, Item: 40

Stack: [10, 20, 30, 40, 50]
Index: 0, Item: 10
Index: 1, Item: 20
Index: 2, Item: 30
Index: 3, Item: 40
Index: 4, Item: 50
```

> **NOTE:**  
> - Looking at the output, we need to think that the "top" of the Stack is the higher index of the Array.
> - In other words, the end of the Array (Stack).

Now, let's implement the function to remove from the Stack. That's, implement the **pop()** function:

**Python:** [stacks.py](src/python/stacks.py)
```python
def pop(self):
    self.arr[self.top] = None
    self.top -= 1
```

See that:

 - First, we set the last item in the Stack as "None":
   - The last item in the Stack is **"arr[self.top]"**:
 - Next, we need to decrement the "top" (index) variable.

Now, let's test in the practice:

**Python:**
```python
from stacks import StackUsingArray

if __name__ == "__main__":

    myStack = StackUsingArray(5)

    myStack.push(10)
    myStack.push(20)
    myStack.push(30)
    myStack.push(40)
    myStack.push(50)
    print("Example Stack (5/5):")
    myStack.traverse()

    print("\nPOP...")
    myStack.pop()
    myStack.traverse()

    print("\nPOP...")
    myStack.pop()
    myStack.traverse()

    print("\nPOP...")
    myStack.pop()
    myStack.traverse()

    print("\nPOP...")
    myStack.pop()
    myStack.traverse()

    print("\nPOP...")
    myStack.pop()
    myStack.traverse()
```

**OUTPUT:**  
```python
Example Stack (5/5):
Stack: [10, 20, 30, 40, 50]
Index: 0, Item: 10
Index: 1, Item: 20
Index: 2, Item: 30
Index: 3, Item: 40
Index: 4, Item: 50

POP...
Stack: [10, 20, 30, 40, None]
Index: 0, Item: 10
Index: 1, Item: 20
Index: 2, Item: 30
Index: 3, Item: 40

POP...
Stack: [10, 20, 30, None, None]
Index: 0, Item: 10
Index: 1, Item: 20
Index: 2, Item: 30

POP...
Stack: [10, 20, None, None, None]
Index: 0, Item: 10
Index: 1, Item: 20

POP...
Stack: [10, None, None, None, None]
Index: 0, Item: 10

POP...
Stack: [None, None, None, None, None]
```

Sometimes we need to check which element is at the "top" of the Stack without deleting it. To do this, let's implement the **peek()** function:

**Python:** [stacks.py](src/python/stacks.py)
```python
def peek(self):
    return self.arr[self.top]
```

> **NOTE:**  
> See that we just need to return the element in the array at index "top".

Now, let's test in the practice:

**Python:**
```python
from stacks import StackUsingArray

if __name__ == "__main__":

    myStack = StackUsingArray(5)

    myStack.push(10)
    myStack.traverse()
    print("Item at top:", myStack.peek())
    print("")

    myStack.push(20)
    myStack.traverse()
    print("Item at top:", myStack.peek())
    print("")

    myStack.push(30)
    myStack.traverse()
    print("Item at top:", myStack.peek())
    print("")

    myStack.push(40)
    myStack.traverse()
    print("Item at top:", myStack.peek())
    print("")

    myStack.push(50)
    myStack.traverse()
    print("Item at top:", myStack.peek())
```

**OUTPUT:**  
```python
Stack: [10, None, None, None, None]
Index: 0, Item: 10
Item at top: 10

Stack: [10, 20, None, None, None]
Index: 0, Item: 10
Index: 1, Item: 20
Item at top: 20

Stack: [10, 20, 30, None, None]
Index: 0, Item: 10
Index: 1, Item: 20
Index: 2, Item: 30
Item at top: 30

Stack: [10, 20, 30, 40, None]
Index: 0, Item: 10
Index: 1, Item: 20
Index: 2, Item: 30
Index: 3, Item: 40
Item at top: 40

Stack: [10, 20, 30, 40, 50]
Index: 0, Item: 10
Index: 1, Item: 20
Index: 2, Item: 30
Index: 3, Item: 40
Index: 4, Item: 50
Item at top: 50
```

Ok, we know how to **insert (push)**, **remove (pop)**, and **check the item at the top of the Stack (peek)**, but how to see how many elements are on the Stack?

Do to it, let's implement the `__len__()` function:

**Python:** [stacks.py](src/python/stacks.py)
```python
def __len__(self):
    return self.top + 1
```

> **NOTE:**  
The **"+1"** is added because *"self.top"* is *the index of the last element in the Stack*, and the length of the Stack should be one more than the index of the last element. So, **"self.top+1"** gives the correct length of the Stack.

Now, let's test in the practice:

**Python:**
```python
from stacks import StackUsingArray

if __name__ == "__main__":

    myStack = StackUsingArray(5)

    myStack.push(10)
    myStack.traverse()
    print("Stack length:", myStack.__len__())
    print("")

    myStack.push(20)
    myStack.traverse()
    print("Stack length:", myStack.__len__())
    print("")

    myStack.push(30)
    myStack.traverse()
    print("Stack length:", myStack.__len__())
    print("")

    myStack.push(40)
    myStack.traverse()
    print("Stack length:", myStack.__len__())
    print("")

    myStack.push(50)
    myStack.traverse()
    print("Stack length:", myStack.__len__())
```

**OUTPUT:**  
```python
Stack: [10, None, None, None, None]
Index: 0, Item: 10
Stack length: 1

Stack: [10, 20, None, None, None]
Index: 0, Item: 10
Index: 1, Item: 20
Stack length: 2

Stack: [10, 20, 30, None, None]
Index: 0, Item: 10
Index: 1, Item: 20
Index: 2, Item: 30
Stack length: 3

Stack: [10, 20, 30, 40, None]
Index: 0, Item: 10
Index: 1, Item: 20
Index: 2, Item: 30
Index: 3, Item: 40
Stack length: 4

Stack: [10, 20, 30, 40, 50]
Index: 0, Item: 10
Index: 1, Item: 20
Index: 2, Item: 30
Index: 3, Item: 40
Index: 4, Item: 50
Stack length: 5
```

Like Arrays and Linked Lists, it is interesting to know how to traverse a Stack. Let's implement the **traverse()** function to do this:

**Python:** [stacks.py](src/python/stacks.py)
```python
def traverse(self):
    print("Stack:", self.arr)  # Prin all Stack elements.
    for current_index in range(self.top + 1):
        # Print current element and index.
        print(f"Index: {current_index}, Item: {self.arr[current_index]}")
```

Now, let's test in the practice:

**Python:**
```python
from stacks import StackUsingArray

if __name__ == "__main__":

    myStack = StackUsingArray(5)
    myStack.traverse()
    print("")

    myStack.push(10)
    myStack.traverse()
    print("")

    myStack.push(20)
    myStack.traverse()
    print("")

    myStack.push(30)
    myStack.traverse()
    print("")

    myStack.push(40)
    myStack.traverse()
    print("")

    myStack.push(50)
    myStack.traverse()
```

**OUTPUT:**  
```python
Stack: [None, None, None, None, None]

Stack: [10, None, None, None, None]
Index: 0, Item: 10

Stack: [10, 20, None, None, None]
Index: 0, Item: 10
Index: 1, Item: 20

Stack: [10, 20, 30, None, None]
Index: 0, Item: 10
Index: 1, Item: 20
Index: 2, Item: 30

Stack: [10, 20, 30, 40, None]
Index: 0, Item: 10
Index: 1, Item: 20
Index: 2, Item: 30
Index: 3, Item: 40

Stack: [10, 20, 30, 40, 50]
Index: 0, Item: 10
Index: 1, Item: 20
Index: 2, Item: 30
Index: 3, Item: 40
Index: 4, Item: 50
```

Ok, now let's check if the Stack is full or not. To do this, let's implement the **check_stack()** function.

**Python:** [stacks.py](src/python/stacks.py)
```python
def check_stack(self):
    # Here "self.top+1" is used as count, not index.
    if self.top + 1 < self.size:
        # Here "self.top+1" is used as count, not index.
        print(f"The Stack is not full: {self.top+1}/{self.size}")
        return True
    else:
        # Here "self.top+1" is used as count, not index.
        print(f"The Stack is full: ({self.top+1}/{self.size})")
        return False
```

See that:

 - If the Stack is **not full**, then the return is **True**.
 - If the Stack if **full**, then the return is **False**.

> **NOTE:**
> This approach is interesting to use the **check_stack()** function with the "while" statement to check if the Stack is full or not.

Now, let's test in the practice:

**Python:**
```python
from stacks import StackUsingArray

if __name__ == "__main__":

    myStack = StackUsingArray(5)
    stack_return = myStack.check_stack()
    print("Return:", stack_return)
    myStack.traverse()
    print("")

    myStack.push(10)
    stack_return = myStack.check_stack()
    print("Return:", stack_return)
    myStack.traverse()
    print("")

    myStack.push(20)
    stack_return = myStack.check_stack()
    print("Return:", stack_return)
    myStack.traverse()
    print("")

    myStack.push(30)
    stack_return = myStack.check_stack()
    print("Return:", stack_return)
    myStack.traverse()
    print("")

    myStack.push(40)
    stack_return = myStack.check_stack()
    print("Return:", stack_return)
    myStack.traverse()
    print("")

    myStack.push(50)
    stack_return = myStack.check_stack()
    print("Return:", stack_return)
    myStack.traverse()
```

**OUTPUT:**  
```python
The Stack is not full: 0/5
Return: True
Stack: [None, None, None, None, None]

The Stack is not full: 1/5
Return: True
Stack: [10, None, None, None, None]
Index: 0, Item: 10

The Stack is not full: 2/5
Return: True
Stack: [10, 20, None, None, None]
Index: 0, Item: 10
Index: 1, Item: 20

The Stack is not full: 3/5
Return: True
Stack: [10, 20, 30, None, None]
Index: 0, Item: 10
Index: 1, Item: 20
Index: 2, Item: 30

The Stack is not full: 4/5
Return: True
Stack: [10, 20, 30, 40, None]
Index: 0, Item: 10
Index: 1, Item: 20
Index: 2, Item: 30
Index: 3, Item: 40

The Stack is full: (5/5)
Return: False
Stack: [10, 20, 30, 40, 50]
Index: 0, Item: 10
Index: 1, Item: 20
Index: 2, Item: 30
Index: 3, Item: 40
Index: 4, Item: 50
```

**NOTE:**  
You can see the complete code to do all this below:

**Python:** [stacks.py](src/python/stacks.py)
```python
class StackUsingArray:
    def __init__(self, size):
        self.size = size
        self.arr = [None] * size
        self.top = -1

    def __len__(self):
        return self.top + 1

    def push(self, item):
        # Here "self.top+1" is used as count, not index.
        if self.top + 1 >= self.size:
            print("The Stack is full.")
            return None
        self.top += 1
        self.arr[self.top] = item

    def pop(self):
        self.arr[self.top] = None
        self.top -= 1

    def peek(self):
        return self.arr[self.top]

    def traverse(self):
        print("Stack:", self.arr)  # Prin all Stack elements.
        for current_index in range(self.top + 1):
            # Print current element and index.
            print(f"Index: {current_index}, Item: {self.arr[current_index]}")

    def check_stack(self):
        # Here "self.top+1" is used as count, not index.
        if self.top + 1 < self.size:
            # Here "self.top+1" is used as count, not index.
            print(f"The Stack is not full: {self.top+1}/{self.size}")
            return True
        else:
            # Here "self.top+1" is used as count, not index.
            print(f"The Stack is full: ({self.top+1}/{self.size})")
            return False
```














































Now, let's test in the practice:

**Python:** [stacks.py](src/python/stacks.py)
```python

```

**OUTPUT:**  
```python

```











































































---

<div id=""></div>

## Stack implementation using Python mechanics (append() and pop() functions)

In Python, we can abuse "object orientation" and "lists" to create Stacks just by using the **append()** and **pop()** functions to implement the necessary mechanisms in a Stack.

![img](images/append-and-pop.png)  

Knowing this:

 - We need only to decide which end of the list will be considered the **"top"** of the stack.
 - And which will be the **"base (bottom)"**.

**NOTE:**  
Once that decision is made, the operations can be implemented using the list methods such as **append()** and **pop()**.

For example, let's see the code that implements this:

**Python:** [stacks.py](src/python/stacks.py)
```python
class StackUsingPythonList:
    def __init__(self):
        self.items = []
```


































---

<div id="reverse-stack"></div>

## Reverse Stack (e.g. Undo/Redo Operations)

Consider what happens when you reverse objects in a Stack. The order in which they are removed is exactly the reverse of the order in which they were placed.

For example, see the image below:

![img](images/simplereversal.png)  

See that in the above image, we **reversed Python objects**:

 - **Before reverse:**
   - The "4" is the *base (or bottom)*.
   - The "8.4" is the *top*.
 - **After reverse:**
   - The "8.4" is the *base (or bottom)*.
   - The "4" is the *top*.

> **Ok, but when reverse stack is needed?**

 - **WEB BROWSER:**
   - For example, *every web browser* has a *Back button*;
   - As you navigate from web page to web page, those pages are placed on a stack *(actually it is the URLs that are going on the stack)*;
   - The current page that you are viewing is on the *top* and the first page you looked at is at the *base (or bottom)*;
   - If you click on the *Back button*, you begin to move in reverse order through the pages.
 - **A TEXT EDITOR (UNDO/REDO):**
   - A text editor that allows undo and redo operations can use a reserve stack to store undone operations. When the user clicks "undo", the last operation is popped from the reserve stack and pushed onto a redo stack.
 - **UNDO SYSTEM IN GAMES:**
   - In games, it is common to have an *undo system* to allow the player to undo their last actions. A reserve stack can be used to store undone actions, and when the player clicks "redo," the corresponding action is popped from the reserve stack and pushed onto a redo stack.
 - **FUNCTION CALL MANAGEMENT:**
   - A reserve stack can be used to manage function calls in a program. When a function is called, its arguments are pushed onto the reserve stack, and when the function returns, the arguments are popped.





























































<!--- ( Length or Size ) --->
<!--- ( Insertion ) --->
<!--- ( Traversal ) --->
<!--- ( Deletion ) --->
<!--- ( Sorting ) --->
<!--- ( Search ) --->
<!--- ( Operations by Index ) --->
<!--- ( Reverse ) --->
<!--- ( Split ) --->
<!--- ( Clone or Copy ) --->
<!--- ( Intersection and Union ) --->
<!--- ( Detect Loops ) --->
<!--- ( Concatenation ) --->
<!--- ( Merge ) --->
<!--- ( Tips & Tricks ) --->
<!--- ( REFERENCES ) --->




























































































































---

<!--- ( Tips & Tricks ) --->

<div id="the-duplicates-issue"></div>

## The duplicates items issue

> To understand **"the duplicates items issue"** see the two examples below.

### Searching without Duplicates

When you design a data storage structure, you need to decide whether items with duplicate keys will be allowed.

 - If you’re writing a data storage program in which duplicates are not allowed, you may need to guard against human error during an insertion.
 - Checking all the data items in the array to ensure (garantir) that not one of them already has the same key value as the item being inserted.
 - **NOTE:** This check increases the steps required for an insertion from *1* to *N*:
   - This is because the Algorithm now needs to check all elements, that's, "N" times.

### Searching with Duplicates

 - Allowing duplicates complicates the search algorithm. Even if the search finds a match, it must continue looking for possible additional matches until the last occupied cell.
 - At least, this is one approach; you could also stop after the first match and perform subsequent searches after that.
 - How you proceed depends on whether the question is:
   - “Find me everyone with the family name of Smith”.
   - “Find me someone with the family name of Smith”.
   - “Find how many entries have the family name Smith”.
 - Finding all items matching a search key is an exhaustive search.
 - **NOTE:** Exhaustive searches require *N* steps because the algorithm must go all the way to the last occupied cell, regardless of what is being sought.

> **NOTE:**
> You need to worry about duplicate items to **Insertion**, **Deletion**, **Traversal**, and **Search**.

The table below shows the **average (here the focus is the average)** number of comparisons and moves for the four operations.

|               | **No Duplicates**          | **Duplicates OK**                  |
|---------------|----------------------------|------------------------------------|
| **Insertion** | <sup>N</sup>/<sub>2</sub> comparisons            | N comparisons                      |
| **Deletion**  | No comparisons, one move   | No comparisons, one move           |
| **Traversal** | <sup>N</sup>/<sub>2</sub> comparisons, <sup>N</sup>/<sub>2</sub> moves | N comparisons, more than <sup>N</sup>/<sub>2</sub> moves |
| **Search**    | N processing steps         | N processing steps                 |

 - First where no duplicates are allowed and then where they are allowed.
 - **N** is the number of items in the array.
 - Inserting a new item counts as one move.












































































































<!--- ( REFERENCES ) --->

---

<div id="ref"></div>

## REFERENCES

 - [Problem Solving with Algorithms and Data Structures using Python](https://runestone.academy/ns/books/published/pythonds/index.html)
 - [Data Structures & Algorithms in Python](https://learning.oreilly.com/library/view/data-structures/9780134855912/)

---

Ro**drigo** **L**eite da **S**ilva - **drigols**
