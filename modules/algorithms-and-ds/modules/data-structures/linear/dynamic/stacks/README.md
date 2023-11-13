# Stacks (LIFO: Last-In, First-Out)

## Contents

 - **Basics:**
   - [Intro to Stacks](#intro-to-stacks)
   - [Stack class using Array (fixed size) approach](#stack-class-using-array)
   - [Stack class using Singly Linked List (dynamic size) approach](#stack-class-using-linked-list)
   - [Stack class using Python Build-in functions (append/pop)](#stack-class-using-python-build-in-functions)
 - **Reverse:**
   - [Intro to Reverse Stack problems (e.g. Undo/Redo Operations)](#reverse-stack-theory)
   - [Reversing a Word/Phrase](#reversing-word-phrase)
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

We have two approaches to implementing Stacks:

 - **Fixed Size Stack (Array implementation):**
   - As the name suggests, a fixed size stack has a fixed size and cannot grow or shrink dynamically.
   - If the stack is full and an attempt is made to add an element to it, an *Overflow error occurs*.
   - If the stack is empty and an attempt is made to remove an element from it, an *Underflow error occurs*.
   - **Advantages:**
     - Easy to implement.
     - Memory is saved as pointers are not involved.
   - **Disadvantages:**
     - It is not dynamic i.e., it doesn’t grow and shrink depending on needs at runtime. [But in case of dynamic sized arrays like vector in C++, list in Python, ArrayList in Java, stacks can grow and shrink with array implementation as well].
     - The total size of the stack must be defined beforehand.
 - **Dynamic Size Stack (Linked List implementation):**
   - A dynamic size stack can grow or shrink dynamically.
   - When the stack is full, it automatically increases its size to accommodate the new element, and when the stack is empty, it decreases its size.
   - This type of stack is implemented using a *Linked List*, as it allows for easy resizing of the stack.
   - **Advantages:**
     - The linked list implementation of a stack can grow and shrink according to the needs at runtime.
     - It is used in many virtual machines like JVM.
   - **Disadvantages:**
     - Requires extra memory due to the involvement of pointers.
     - Random accessing is not possible in stack.

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
```bash
Stack: [None, None, None, None, None]
```

To start let's implement the useful methods:

**Python:** [stacks.py](src/python/stacks.py)
```python
def __len__(self):
    return self.top + 1

def isEmpty(self):
    return self.top == -1

def isFull(self):
    return self.top + 1 == self.size
```

 - `__len__():`
   - The `__len__()` method returns the length of the Stack.
   - **NOTE:** Here *"self.top+1"* is used as count, not index.
 - **isEmpty():**
   - The *isEmpty()* method returns a verification if the Stack is empty.
 - **isFull():**
   - The *isEmpty()* method returns a verification if the Stack is full.

Now, let's see how to add a new item in the Stack, that's, implement **push()** method:

**Python:** [stacks.py](src/python/stacks.py)
```python
def push(self, item):
    if self.isFull():
        print("The Stack is full.")
        return None
    self.top += 1
    self.arr[self.top] = item
```

See that:

 - First, we need to check if the Stack is full.
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
```bash
The Stack is empty.

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

Now, let's implement a method to remove from the Stack. That's, implement the **pop()** method:

**Python:** [stacks.py](src/python/stacks.py)
```python
def pop(self):
    if self.isEmpty():
        print("The Stack is empty.")
        return None
    popped_item = self.arr[self.top]
    self.arr[self.top] = None
    self.top -= 1
    return popped_item
```

See that:

 - First, we need to check if the Stack is empty.
 - Next, we save the "top" item to return later.
 - Next, we set the last item (top) in the Stack as "None":
   - The last item in the Stack is **"arr[self.top]"**:
 - Next, we need to decrement the "top" (index) variable.
 - Finally, return the value of the old "top".

Now, let's test in the practice:

**Python:**
```python
from stacks import StackUsingArray

if __name__ == "__main__":

    myStack = StackUsingArray(5)

    popped_item = myStack.pop()
    print("Popped item: ", popped_item)

    myStack.push(10)
    myStack.push(20)
    myStack.push(30)
    myStack.push(40)
    myStack.push(50)
    print("\nStack Example (5/5):")
    myStack.traverse()
    print("")

    # 10->20->30->40
    popped_item = myStack.pop()
    print("Popped item: ", popped_item)
    myStack.traverse()
    print("")

    # 10->20->30
    popped_item = myStack.pop()
    print("Popped item: ", popped_item)
    myStack.traverse()
    print("")

    # 10->20
    popped_item = myStack.pop()
    print("Popped item: ", popped_item)
    myStack.traverse()
    print("")

    # 10
    popped_item = myStack.pop()
    print("Popped item: ", popped_item)
    myStack.traverse()
    print("")

    # Remove last item from the stack.
    popped_item = myStack.pop()
    print("Popped item: ", popped_item)
    myStack.traverse()
    print("")

    # Stack is empty.
    popped_item = myStack.pop()
    print("Popped item: ", popped_item)
    myStack.traverse()
    print("")
```

**OUTPUT:**  
```bash
The Stack is empty.
Popped item:  None

Stack Example (5/5):
Stack: [10, 20, 30, 40, 50]
Index: 0, Item: 10
Index: 1, Item: 20
Index: 2, Item: 30
Index: 3, Item: 40
Index: 4, Item: 50

Popped item:  50
Stack: [10, 20, 30, 40, None]
Index: 0, Item: 10
Index: 1, Item: 20
Index: 2, Item: 30
Index: 3, Item: 40

Popped item:  40
Stack: [10, 20, 30, None, None]
Index: 0, Item: 10
Index: 1, Item: 20
Index: 2, Item: 30

Popped item:  30
Stack: [10, 20, None, None, None]
Index: 0, Item: 10
Index: 1, Item: 20

Popped item:  20
Stack: [10, None, None, None, None]
Index: 0, Item: 10

Popped item:  10
The Stack is empty.

The Stack is empty.
Popped item:  None
The Stack is empty.
```

Sometimes we need to check which element is at the "top" of the Stack without deleting it. To do this, let's implement the **peek()** method:

**Python:** [stacks.py](src/python/stacks.py)
```python
def peek(self):
    if self.isEmpty():
        print("The Stack is empty.")
        return None
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
```bash
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

Like Linked Lists, it is interesting to know how to traverse a Stack. Let's implement the **traverse()** method to do this:

**Python:** [stacks.py](src/python/stacks.py)
```python
def traverse(self):
    if self.isEmpty():
        print("The Stack is empty.")
        return None
    print("Stack:", self.arr)  # Prin all Stack elements.
    for current_index in range(self.top + 1):
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
```bash
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

---

<div id="stack-class-using-linked-list"></div>

## Stack class using Singly Linked List (dynamic size) approach

To implement a **Stack** using the *Singly Linked List* concept, all the *Singly Linked List* operations should be performed based on Stack operations **LIFO (Last In, First Out)**.

Let's start by implementing the Node class that will be used in the Stack class:

**Python:** [stacks.py](src/python/stacks.py)
```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
```

Ok, now let's implement the Stack class and your constructor:

**Python:** [stacks.py](src/python/stacks.py)
```python
class StackUsingLinkedList(Node):
    def __init__(self):
        self.head = None
```

> **NOTE:**  
> - See that we inherit from the "Node" class.
> - As Linked Lists this class has only the "head" instance variable set by None.

Now, let's implement the useful method to use later:

**Python:** [stacks.py](src/python/stacks.py)
```python
def isEmpty(self):
    return self.head == None
```

> **NOTE:**  
> The method above just checks if the Stack is empty. That's, the head is equal None.

Now, to insert a new element in the Stack we need to implement a method to do this dynamically. Let's implement the **push()** method:

**Python:** [stacks.py](src/python/stacks.py)
```python
def push(self, item):
    if self.isEmpty():
        self.head = Node(item)
    else:
        new_node = Node(item)
        new_node.next = self.head
        self.head = new_node
```

See that:

 - First, we check if the Stack is empty:
   - If the head is None we only instance a new Node set by head.
   - That's, the head now is the new Node.
 - Else, we need to instance a new Node:
   - Make the "next" pointer of the new Node point to the old head.
   - Finally, we need to set the new Node as the head.


Now, let's test in the practice:

**Python:**
```python
from stacks import StackUsingLinkedList

if __name__ == "__main__":

    myStack = StackUsingLinkedList()
    
    # 10(head)
    myStack.push(10)
    print(myStack.head.item)

    # 20(head)->10
    myStack.push(20)
    print(myStack.head.item)

    # 30(head)->20->10
    myStack.push(30)
    print(myStack.head.item)

    # 40(head)->30->20->10
    myStack.push(40)
    print(myStack.head.item)

    # 50(head)->40->30->20->10
    myStack.push(50)
    print(myStack.head.item)
```

**OUTPUT:**  
```bash
10
20
30
40
50
```

> **NOTE:**  
> See that this approach insert a new element at the top (front) of the Stack/Linked List - **push()**.

Now, let's see how to remove (pop) an element from the Stack, that's, implement **pop()** method:

**Python:** [stacks.py](src/python/stacks.py)
```python
def pop(self):
    if self.isEmpty():
        print("The Stack is empty.")
        return None
    else:
        popped_item = self.head.item
        old_head = self.head
        self.head = self.head.next
        del old_head
        return popped_item
```

See that:

 - Again, first we need to check if the Stack is empty.
 - If the Stack is not empty:
   - We save the "popped" item to return in the method.
   - We save the old head to be deleted later.
     - This is interesting to avoid Memory Leaks.
   - And do the "next" pointer of the old head as the new head.
   - Delete the old head.
   - Finally, return the "popped" item.

Now, let's test in the practice:

**Python:**
```python
from stacks import StackUsingLinkedList

if __name__ == "__main__":
    myStack = StackUsingLinkedList()

    myStack.push(10)  # 10(head)
    myStack.push(20)  # 20(head)->10
    myStack.push(30)  # 30(head)->20->10
    myStack.push(40)  # 40(head)->30->20->10
    myStack.push(50)  # 50(head)->40->30->20->10

    popped_item = myStack.pop()  # 50(DELETED) | 40(head)->30->20->10
    print("Popped item:", popped_item)

    popped_item = myStack.pop()  # 40(DELETED) | 30(head)->20->10
    print("Popped item:", popped_item)

    popped_item = myStack.pop()  # 30(DELETED) | 20(head)->10
    print("Popped item:", popped_item)

    popped_item = myStack.pop()  # 20(DELETED) | 10(head)
    print("Popped item:", popped_item)

    popped_item = myStack.pop()  # 10(DELETED)
    print("Popped item:", popped_item)

    popped_item = myStack.pop()  # The Stack is empty.
```

**OUTPUT:**  
```bash
Popped item: 50
Popped item: 40
Popped item: 30
Popped item: 20
Popped item: 10
The Stack is empty.
```

Ok, now let's implement a method to check the item on the top of the Stack, that's, **peek()** method:

**Python:** [stacks.py](src/python/stacks.py)
```python
def peek(self):
    if self.isEmpty():
        print("The Stack is empty.")
        return None
    else:
        return self.head.item
```

See that:

 - First, we need to check if the Stack is empty.
 - If the Stack is not empty, we just return the item in the head.

Now, let's test in the practice:

**Python:** [stacks.py](src/python/stacks.py)
```python
from stacks import StackUsingLinkedList

if __name__ == "__main__":
    myStack = StackUsingLinkedList()
    myStack.peek()  # The Stack is empty.

    myStack.push(10)  # 10(head/top)
    print("TOP/HEAD->ITEM:", myStack.peek())

    myStack.push(20)  # 20(head/top)->10
    print("TOP/HEAD->ITEM:", myStack.peek())

    myStack.push(30)  # 30(head/top)->20->10
    print("TOP/HEAD->ITEM:", myStack.peek())

    myStack.push(40)  # 40(head/top)->30->20->10
    print("TOP/HEAD->ITEM:", myStack.peek())

    myStack.push(50)  # 50(head/top)->40->30->20->10
    print("TOP/HEAD->ITEM:", myStack.peek())
```

**OUTPUT:**  
```bash
The Stack is empty.
TOP/HEAD->ITEM: 10
TOP/HEAD->ITEM: 20
TOP/HEAD->ITEM: 30
TOP/HEAD->ITEM: 40
TOP/HEAD->ITEM: 50
```

---

<div id="stack-class-using-python-build-in-functions"></div>

## Stack class using Python Build-in functions (append/pop)

In Python, we can abuse of the **"object orientation"**, **"lists"**, and the **"Built-in Functions"** to create Stacks just by using the **append()** and **pop()** functions to implement the necessary mechanisms in a Stack.

![img](images/append-and-pop.png)  

Knowing this:

 - We need only to decide which end of the list will be considered the **"top"** of the stack.
 - And which will be the **"base (bottom)"**.

**NOTE:**  
Once that decision is made, the operations can be implemented using the list methods such as **append()** and **pop()**.

Let's start by implementing the class and your constructor:

**Python:** [stacks.py](src/python/stacks.py)
```python
class StackUsingPythonBuildIn:
    def __init__(self):
        self.stack = []
```

> **NOTE:**
> See that the constructor just creates an empty list.

To start let's implement the useful **isEmpty()** method to use later:

**Python:** [stacks.py](src/python/stacks.py)
```python
def isEmpty(self):
    return self.stack == []
```

Now, let's see how implement the **push()** method using the **append()** *Build-In* function:

**Python:** [stacks.py](src/python/stacks.py)
```python
def push(self, item):
    self.stack.append(item)
```

> **NOTE:**
> - See how easy it is, we just insert a new element at the end of the list using the **append()** function.
> - This item inserted always will be the **"top"**.

Now, let's test in the practice:

**Python:**
```python
from stacks import StackUsingPythonBuildIn

if __name__ == "__main__":
    myStack = StackUsingPythonBuildIn()
    print(myStack.stack)  # The Stack is empty = [].

    myStack.push(10)  # 10(top)
    print(myStack.stack)

    myStack.push(20)  # 10->20(top)
    print(myStack.stack)

    myStack.push(30)  # 10->20->30(top)
    print(myStack.stack)

    myStack.push(40)  # 10->20->30->40(top)
    print(myStack.stack)

    myStack.push(50)  # 10->20->30->40->50(top)
    print(myStack.stack)
```

**OUTPUT:**  
```bash
[]
[10]
[10, 20]
[10, 20, 30]
[10, 20, 30, 40]
[10, 20, 30, 40, 50]
```

Now, let's see how implement the **pop()** method using the **pop()** Build-In function:

**Python:** [stacks.py](src/python/stacks.py)
```python
def pop(self):
    if self.isEmpty():
        print("The Stack is empty.")
        return None
    return self.stack.pop()
```

Now, let's test in the practice:

**Python:**
```python
from stacks import StackUsingPythonBuildIn

if __name__ == "__main__":

    myStack = StackUsingPythonBuildIn()

    myStack.push(10)  # 10(top)
    myStack.push(20)  # 10->20(top)
    myStack.push(30)  # 10->20->30(top)
    myStack.push(40)  # 10->20->30->40(top)
    myStack.push(50)  # 10->20->30->40->50(top)

    print("Stack Items:", myStack.stack)  # 10->20->30->40->50(top)

    popped_item = myStack.pop()  # 10->20->30->40(top) | popped_item = 50
    print("\nPOPPED ITEM:", popped_item)
    print("Stack Items:", myStack.stack)

    popped_item = myStack.pop()  # 10->20->30(top) | popped_item = 40
    print("\nPOPPED ITEM:", popped_item)
    print("Stack Items:", myStack.stack)

    popped_item = myStack.pop()  # 10->20(top) | popped_item = 30
    print("\nPOPPED ITEM:", popped_item)
    print("Stack Items:", myStack.stack)

    popped_item = myStack.pop()  # 10(top) | popped_item = 20
    print("\nPOPPED ITEM:", popped_item)
    print("Stack Items:", myStack.stack)

    popped_item = myStack.pop()  # popped_item = 10
    print("\nPOPPED ITEM:", popped_item)
    print("Stack Items:", myStack.stack)
    print("")

    popped_item = myStack.pop()  # The Stack is empty = [].
    print("POPPED ITEM:", popped_item)
    print("Stack Items:", myStack.stack)
```

**OUTPUT:**  
```bash
Stack Items: [10, 20, 30, 40, 50]

POPPED ITEM: 50
Stack Items: [10, 20, 30, 40]

POPPED ITEM: 40
Stack Items: [10, 20, 30]

POPPED ITEM: 30
Stack Items: [10, 20]

POPPED ITEM: 20
Stack Items: [10]

POPPED ITEM: 10
Stack Items: []

The Stack is empty.
POPPED ITEM: None
Stack Items: []
```

Ok, to finalize let's implement the **peek()** method:

**Python:** [stacks.py](src/python/stacks.py)
```python
def peek(self):
    if self.isEmpty():
        print("The Stack is empty.")
        return None
    # "self.stack[-1]" get the last element of the list (Stack).
    return self.stack[-1]
```

> **NOTE:**  
> See that we use the index "self.stack[-1]" to get the last element of the list (Stack).

Now, let's test in the practice:

**Python:**
```python
from stacks import StackUsingPythonBuildIn

if __name__ == "__main__":

    myStack = StackUsingPythonBuildIn()

    peek = myStack.peek()
    print("TOP:", peek)

    print("")
    myStack.push(10)  # 10(top)
    peek = myStack.peek()
    print("TOP:", peek)

    myStack.push(20)  # 10->20(top)
    peek = myStack.peek()
    print("TOP:", peek)

    myStack.push(30)  # 10->20->30(top)
    peek = myStack.peek()
    print("TOP:", peek)

    myStack.push(40)  # 10->20->30->40(top)
    peek = myStack.peek()
    print("TOP:", peek)

    myStack.push(50)  # 10->20->30->40->50(top)
    peek = myStack.peek()
    print("TOP:", peek)
```

**OUTPUT:**  
```bash
The Stack is empty.
TOP: None

TOP: 10
TOP: 20
TOP: 30
TOP: 40
TOP: 50
```








































<!--- ( Reverse ) --->

---

<div id="reverse-stack-theory"></div>

## Intro to Reverse Stack problems (e.g. Undo/Redo Operations)

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

---

<div id="reversing-word-phrase"></div>

## Reversing a Word/Phrase

> Imagine we need to implement a function/method that receives a Word/Phrase and returns it reversed.

Let's get started implementing the **reverser_word_phrase()** method to do this by using a Stack approach:

**Python:** [stacks.py](src/python/stacks.py)
```python
class StackUsingArray:

    def reverser_word_phrase(self, string):
      for letter in string:
          self.push(letter)
      reverse = ''
      while self.__len__() > 0:
          popped_item = self.pop()
          reverse += popped_item
      return reverse




class StackUsingLinkedList(Node):

    def reverser_word_phrase(self, string):
        for letter in string:
            self.push(letter)
        reverse = ''
        while self.head is not None:
            popped_item = self.pop()
            reverse += popped_item
        return reverse




class StackUsingPythonBuildIn:

    def reverser_word_phrase(self, string):
        for letter in string:
            self.push(letter)
        reverse = ''
        while not self.isEmpty():
            popped_item = self.pop()
            reverse += popped_item
        return reverse
```

To test these codes you can use the following code:

```python
from stacks import *

if __name__ == "__main__":

    stack_one = StackUsingArray(100)
    stack_two = StackUsingLinkedList()
    stack_three = StackUsingPythonBuildIn()

    string = input("Word/Phrase to reverse: ")
    print("Passed Word/Phrase:", string)

    print("\nReversing Word/Phrase using StackUsingArray() class:")
    reversed_string = stack_one.reverser_word_phrase(string)
    print("Reversed Word/Phrase:", reversed_string)

    print("\nReversing Word/Phrase using StackUsingLinkedList() class:")
    reversed_string = stack_two.reverser_word_phrase(string)
    print("Reversed Word/Phrase:", reversed_string)


    print("\nReversing Word/Phrase using StackUsingPythonBuildIn() class:")
    reversed_string = stack_three.reverser_word_phrase(string)
    print("Reversed Word/Phrase:", reversed_string)
```

**OUTPUT:**
```bash
Word/Phrase to reverse: avlis ad etiel ogirdor
Passed Word/Phrase: avlis ad etiel ogirdor

Reversing Word/Phrase using StackUsingArray() class:
Reversed Word/Phrase: rodrigo leite da silva

Reversing Word/Phrase using StackUsingLinkedList() class:
Reversed Word/Phrase: rodrigo leite da silva

Reversing Word/Phrase using StackUsingPythonBuildIn() class:
Reversed Word/Phrase: rodrigo leite da silva
```

You can also use the **reverse()** method to reverse a word/phrase and join with the **string.join()** method. For example:

```python
string = input("Word/Phrase to reverse: ")
print("Passed Word/Phrase:", string)

reversed_string = ''.join(reversed(string))
print("Reversed Word/Phrase:",reversed_string)

```

**OUTPUT:**
```bash
Word/Phrase to reverse: avlis ad etiel ogirdor

Passed Word/Phrase: avlis ad etiel ogirdor
Reversed Word/Phrase: rodrigo leite da silva
```

Another approach to reversing a word/phrase is using *Python slicing mechanics*. For example:

**Python:**
```python
string = input("Word/Phrase to reverse: ")
print("Passed Word/Phrase:", string)

reversed_string = string[::-1]
print("Reversed Word/Phrase:", reversed_string)
```

**OUTPUT:**
```bash
Word/Phrase to reverse: avlis ad etiel ogirdor

Passed Word/Phrase: avlis ad etiel ogirdor
Reversed Word/Phrase: rodrigo leite da silva
```

 - `[::-1]` **- It creates a reversed copy of the sequence:**
   - **[start:stop:step]**
   - **start** is omitted, so it starts from the end of the sequence.
   - **stop** is omitted, so it goes until the beginning of the sequence.
   - **step** is -1, meaning it takes elements from back to front.








































<!--- ( REFERENCES ) --->

---

<div id="ref"></div>

## REFERENCES

 - [Problem Solving with Algorithms and Data Structures using Python](https://runestone.academy/ns/books/published/pythonds/index.html)
 - [Data Structures & Algorithms in Python](https://learning.oreilly.com/library/view/data-structures/9780134855912/)
 - [Introduction to Stack – Data Structure and Algorithm Tutorials](https://www.geeksforgeeks.org/introduction-to-stack-data-structure-and-algorithm-tutorials/)
 - [Implement a stack using singly linked list](https://www.geeksforgeeks.org/implement-a-stack-using-singly-linked-list/)

---

Ro**drigo** **L**eite da **S**ilva - **drigols**
