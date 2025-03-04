# Linked Lists

## Contents

 - **Node:**
   - [Node class for a Singly Linked List](#node-class-sll)
   - [Node class for a Double Linked List](#node-class-dll)
 - **Singly Linked List:**
   - [Singly Linked List class](#sll-class)
   - [How to link and initialize a Singly Linked List manually](#link-initialize-sll-manually)
   - [How to link and initialize a Singly Linked List using OOP (instance)](#link-initialize-sll-using-oop)
   - **Operations:**
     - [Add a new Node at the front (push) | O(1)](#sll-push)
     - [Add a new Node at the end (append) | O(n)](#sll-append)
     - [Add a new Node at the end (append) with constant Time Complexity | O(1)](#sll-append-constant)
     - [Traversing in SinglyLinkedList from the Head until last Node (Tail) | O(n)](#sll-print-list-from-head)
 - **Double Linked List:**
 - **Circular Linked List:**
   - [Circular Linked List approaches](#circular-linked-list-approaches)
 - [**REFERENCES**](#ref)
<!---
[WHITESPACE RULES]
- Same topic = "20" Whitespace character.
- Different topic = "100" Whitespace character.
--->






































































































<!--- ( Node ) --->

---

<div id="node-class-sll"></div>

## Node class for a Singly Linked List

Here, let's see how to implement a **Node** class for a **Singly Linked List**:

![img](images/sll-01.png)  

<!--- ( Python) --->
<details>

<summary>Python</summary>

</br>

[singly_linked_list.py](src/python/singly_linked_list.py)
```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
```

</details>




















---

<div id="node-class-dll"></div>

## Node class for a Double Linked List

A **Doubly Linked List** is composed of connected **"Nodes"**, where each **"Node"** has:

 - **"Data"** stored.
 - A pointer **"prev"** to the previous *Node*.
 - A pointer **"next"** to the next *Node*.

![img](images/dll-01.png)  

See that:

 - The **"prev"** point of the first Node is NULL.
 - The **"next"** point of the last Node also is NULL.

Now, let's implement a **"Node"** class for a **Doubly Linked List**:

<details>
<summary>Python</summary>

</br>

[doubly_linked_list.py](src/python/doubly_linked_list.py)
```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
```

</details>







































































































<!--- ( Singly Linked List ) --->

---

<div id="sll-class"></div>

## Singly Linked List class

Here, let's see how to implement a **Singly Linked List** *class*:

<!--- ( Python ) --->
<details>

<summary>Python</summary>

</br>

[singly_linked_list.py](src/python/singly_linked_list.py)
```python
class SinglyLinkedList(Node):
    def __init__(self):
        self.head = None
```

See that the **SinglyLinkedList** class:

 - Inherits from the **Node** class:
   - That's, have access to the **"data"** and **"next"** instance variables.
 - Has only **head** instance variable.

</details>




















---

<div id="link-initialize-sll-manually"></div>

## How to link and initialize a Singly Linked List manually

Here, let's see how to `link` and `initialize` a **Singly Linked List** *manually*:

<!--- ( Python ) --->
<details>

<summary>Python</summary>

</br>

```python
from singly_linked_list import Node

if __name__ == "__main__":

    # Create nodes.
    head = Node(10)
    second = Node(20)
    third = Node(30)

    # Connect nodes.
    head.next = second
    second.next = third

    """
    You don't need to set the next of the last node.
    By default the next always points to None.
    > third.next = None
    """

    print(f"Value in the First Node (head): {head.data}")
    print(f"Value in the Second Node: {second.data}")
    print(f"Value in the Third Node (tail): {third.data}")
```

**OUTPUT:**
```bash
Value in the First Node (head): 10
Value in the Second Node: 20
Value in the Third Node (tail): 30
```

See that using this approach:

 - We `initialize` the **"data"** instance variables using the Node class constructor.
 - We `link` each Node to the next Node using the **"next"** instance variable.

</details>




















---

<div id="link-initialize-sll-using-oop"></div>

## How to link and initialize a Singly Linked List using OOP (instance)

Here, let's see how to link and initialize a **Singly Linked List** *using OOP (instance)* concept:

<!--- ( Python ) --->
<details>

<summary>Python</summary>

</br>

```python
from singly_linked_list import SinglyLinkedList, Node

if __name__ == "__main__":

    # Singly Linked List instance.
    sll = SinglyLinkedList()

    # Assign data + Link the Nodes.
    sll.head = Node(10)            # 10
    sll.head.next = Node(20)       # 10->20
    sll.head.next.next = Node(30)  # 10->20->30

    print("Value in the First Node (head):", sll.head.data)
    print("Value in the Second Node:", sll.head.next.data)
    print("Value in the Third Node (tail):", sll.head.next.next.data)
```

**OUTPUT:**
```bash
Value in the First Node (head): 10
Value in the Second Node: 20
Value in the Third Node (tail): 30
```

 - See that in the two approaches (manually and using OOP) we always need to use the **Node()** class constructor to create new Nodes.
 - **NOTE:** This creates a code repetition problem. To solve this we can create methods to create nodes, such as: [push()](#sll-push) and [append()](#sll-append).

</details>




















---


<div id="sll-push"></div>

## Add a new Node at the front (push) | O(1)

> Now let's, see how to insert a new Node in the **front of a Singly Linked List (also called push)**.

For example, imagine we have the following **Singly Linked List**:

```
10->15->20->25
```

If we add item (element) **5** at the *front*, then the **Singly Linked List** becomes:

```
5->10->15->20->25
```

<!--- ( Python ) --->
<details>

<summary>Python</summary>

</br>

[singly_linked_list.py](src/python/singly_linked_list.py)
```python
def push(self, data):
    new_node = Node(data)      # O(1)
    new_node.next = self.head  # O(1)
    self.head = new_node       # O(1)
```

$f(n) = O(1) + O(1) + O(1)$

### Complexity Explanation

 - **Time Complexity: O(1)**
   - The *Time Complexity* of the *push()* method is **O(1)** because it takes a constant amount of time to create a new node and update the head pointer.
 - **Space Complexity: O(1)**
   - The *Space Complexity* is also **O(1)** because the function only creates a single new node and does not use any additional data structures that grow with the size of the input.

### Code Explanation

 - **Is this method work in an Empty List?**
   - Yes!
 - `new_node = Node(data)`
   - This line creates a new node object using the Node class.
 - `new_node.next = self.head`
   - This line sets the "next" attribute of the new node to the current value of "self.head".
   - "self.head" likely stores a reference to the first node in the linked list.
   - By doing this, the new node is now linked to the beginning of the list, effectively becoming the new head.
 - `self.head = new_node`
   - This line updates the "self.head" attribute of the list to point to the newly created node.
   - This ensures that the list now starts with the newly added node, effectively pushing it to the front of the list.

Now, let's test the **push()** method in practice:

```python
from singly_linked_list import SinglyLinkedList

if __name__ == "__main__":

    # Singly Linked List instance.
    sll = SinglyLinkedList()

    # Remember, we are using the push() approach, that's,
    # the new Node is added in the front of the Singly Linked List.
    sll.push(25)  # 25(head)
    sll.push(20)  # 20(head)->25
    sll.push(15)  # 15(head)->20->25
    sll.push(10)  # 10(head)->15->20->25
    sll.push(5)   #  5(head)->10->15->20->25

    print("Data in the first (head) Node:", sll.head.data)
    print("Data in the second Node:", sll.head.next.data)
    print("Data in the third Node:", sll.head.next.next.data)
    print("Data in the fourth Node:", sll.head.next.next.next.data)
    print("Data in the fifth Node:", sll.head.next.next.next.next.data)
```

**OUTPUT:**  
```bash
Data in the first (head) Node: 5
Data in the second Node: 10
Data in the third Node: 15
Data in the fourth Node: 20
Data in the fifth Node: 25
```

</details>




















---


<div id="sll-append"></div>

## Add a new Node at the end (append) | O(n)

> Now let's, see how to inser a new Node **at the end of a Singly Linked List (also called append)**.

For example, imagine we have the following **Singly Linked List**:

```
5->10->15->20
```

And we add the item (element) **25** at the end, then the **Singly Linked List** becomes:

```
5->10->15->20->25
```

<!--- ( Python ) --->
<details>

<summary>Python</summary>

</br>

[singly_linked_list.py](src/python/singly_linked_list.py)
```python
def append(self, data):
    new_node = Node(data)                  # O(1)
    if self.head is None:                  # O(1)
        self.head = new_node               # O(1)
        return                             # O(1)
    else:
        temp_node = self.head              # O(1)
        while temp_node.next is not None:  # O(n)
            temp_node = temp_node.next     # O(1)
        temp_node.next = new_node          # O(1)
```

$f(n) = O(1) + O(1) + O(1) + O(1) + O(1) + O(n) + O(1) + O(1)$

### Complexity Explanation

 - **Time Complexity: O(n)**
   - The *Time Complexity* of this function is **O(n)**, where **"n"** is the number of nodes in the linked list. This is because in the worst case scenario, we need to traverse the entire linked list to find the last node and append the new node to it.
   - `while temp_node.next is not None:`
     - The while() loop iterates over the linked list until it reaches the last node. In the worst case, it iterates over all **"n"** nodes, resulting in a time complexity of **O(n)**.
 - **Space Complexity: O(1)**
   - The *Space Complexity* is also **O(1)** because the function only creates a single new node and does not use any additional data structures that grow with the size of the input.

### Code Explanation

**Handle Empty List:**
```python
if self.head is None:
    self.head = new_node
    return
```

 - This if statement checks if the list is currently empty (i.e., self.head is None).
 - If it's empty, the new node directly becomes the head of the list, and the method returns.

**Traverse to the End:**
```python
else:
    temp_node = self.head
    while temp_node.next is not None:
        temp_node = temp_node.next
```

 - If the list is not empty, this else block executes:
   - A temporary variable temp_node is initialized to the head of the list.
   - A while loop iterates through the list until it finds the last node (where temp_node.next is None).

**Append the New Node:**
```python
temp_node.next = new_node
```

 - Once the loop finds the last node, this line sets the "next" attribute of the last node to point to the newly created node.
 - This effectively appends the new node to the end of the linked list.

Finally, let's test the **append()** function in practice:

```python
from singly_linked_list import SinglyLinkedList, Node

if __name__ == "__main__":

    List1 = SinglyLinkedList()  # First list instance.
    print("List1 = 5->10->15->20->25 + append(30):")
    List1.head = Node(5)
    List1.head.next = Node(10)
    List1.head.next.next = Node(15)
    List1.head.next.next.next = Node(20)
    List1.head.next.next.next.next = Node(25)
    List1.append(30)
    List1.print_list_from_head()

    List2 = SinglyLinkedList()  # Second list instance.
    print("\nList2 = append(30):")
    List2.append(30)
    List2.print_list_from_head()

    list3 = SinglyLinkedList()  # Third list instance.
    print("\nList3 = append(1) + append(2) + append(3):")
    list3.append(1)
    list3.append(2)
    list3.append(3)
    list3.print_list_from_head()
```

**OUTPUT:**  
```bash
List1 = 5->10->15->20->25 + append(30):
5
10
15
20
25
30

List2 = append(30):
30

List3 = append(1) + append(2) + append(3):
1
2
3
```

> **NOTE:**  
> See that this approach is linear Time Complexity O(n).

</details>




















---

<div id="sll-append-constant"></div>

## Add a new Node at the end (append) with constant Time Complexity | O(1)

Here, let's see how to implement the **append()** method with **constant Time Complexity O(1)**.

**But, first, we need to modify the *SinglyLinkedList()* class to have the *tail attribute (reference)***:  
This is because the *tail attribute* is used to save the last node in the linked list.

<details>
<summary>Python</summary>

</br>

[singly_linked_list.py](src/python/singly_linked_list.py)
```python
class SinglyLinkedList(Node):
    def __init__(self):
        self.head = None
        self.tail = None
```

Now, let's see how to implement the **append_constant()** method with **constant Time Complexity O(1)** using the **tail** attribute:

[singly_linked_list.py](src/python/singly_linked_list.py)
```python
def append_constant(self, data):
    new_node = Node(data)          # O(1)
    if self.head is None:          # O(1)
        self.head = new_node       # O(1)
        self.tail = self.head      # O(1)
    else:
        self.tail.next = new_node  # O(1)
        self.tail = new_node       # O(1)
```

$f(n) = O(1) + O(1) + O(1) + O(1) + O(1) + O(1)$

### Complexity Explanation

 - **Time Complexity: O(1)**
   - The *Time Complexity* of this function is **O(1)** because it only performs a constant number of operations, regardless of the size of the linked list. 
 - **Space Complexity: O(1)**
   - The *Space Complexity* is also **O(1)** because the function only creates a single new node and does not use any additional data structures that grow with the size of the input.

### Code Explanation

**Handle Empty List:**
```python
if self.head is None:
    self.head = new_node
    self.tail = self.head
```

 - Checks if the list is empty (i.e., self.head is None).
   - If the list is empty, the "head" and "tail" are set as the same Node (reference).
   - `self.head = new_node`
     - Sets the *"head"* attribute of the list to the *"new_node"*, as it becomes the first and only node.
   - `self.tail = self.head`
     - Also sets the *"tail"* attribute to the *"new_node"*.

**Handle Non-Empty List:**
```python
else:
    self.tail.next = new_node
    self.tail = new_node
```

 - If the list is not empty, this block executes:
   - `self.tail.next = new_node`
     - Sets the *"next"* attribute of the *old tail* node to point to the *"new_node"*, linking it to the end of the list.
   - `self.tail = new_node`
     - Updates the tail attribute of the list to point to the newly added node, making it the new tail.

See the abstraction below to understand more easily:

```bash
> self.tail.next = new_node

 Old tail
+---+------+     +--------------+
|   | next ----> |   | new_node |
+---+------+     +--------------+

> self.tail = new_node

 Old tail            New tail
+---+------+     +--------------+
|   | next ----> |   | new_node |
+---+------+     +--------------+
```

**NOTE:**  
However, this approach doesn't work for the code below:

```python
List = SinglyLinkedList()
List.head = Node(5)
List.head.next = Node(10)
List.head.next.next = Node(15)
List.head.next.next.next = Node(20)
List.head.next.next.next.next = Node(25)

List.append_constant(30)  # AttributeError: 'NoneType' object has no attribute 'next'
```

**NOTE:**  
This is because the *"tail"* attribute is not set to use the *"next"* attribute. Just the "head" is set here.

### Disadvantage

 - The main *disadvantage* of this approach is that it requires a small amount of additional space in memory. This is because the LinkedList class now needs to store a tail attribute to track the last node in the list.
 - Another *disadvantage* is that the implementation may be a bit more complex than the original approach. This is because the **append_constant()** function now needs to track the *"tail"* and update the *"tail"* attribute.
 - **NOTE:** However, these disadvantages are generally *offset* by the time efficiency of the approach. **O(1)** complexity for the append operation is ideal for scenarios where elements are frequently added.

</details>




















---

<div id="sll-print-list-from-head"></div>

## Traversing in SinglyLinkedList from the Head until last Node (Tail) | O(n)

Here, let's see how to **traverse a Singly Linked List** from the Head until the last Node (Tail).

<details>
<summary>Python</summary>

</br>

**Python** [singly_linked_list.py](src/python/singly_linked_list.py)
```python
def print_list_from_head(self):
    if self.head is None:                     # O(1)
        print("List is empty!")               # O(1)
        return                                # O(1)
    else:
        current_node = self.head              # O(1)
        while current_node is not None:       # O(n)
            print(current_node.data)          # O(1)
            current_node = current_node.next  # O(1)
```

$f(n) = O(1) + O(1) + O(1) + O(1) + O(n) + O(1) + O(1)$

### Complexity Explanation

 - **Time Complexity: O(n)**
   - `while current_node is not None:`
     - The while() loop iterates over the linked list, potentially visiting all *"n"* nodes, resulting in a time complexity of **O(n)**.
     - The other instructions have **O(1)** time complexity.
     - **NOTE:** So, the Time Complexity in the Worst Case is **O(n)**.
 - **Space Complexity: O(1)**
   - The *Space Complexity* of this function is **O(1)**, because we are not using any additional space that grows with the input size. We only need a constant amount of space to store the current_node variable.

### Code Explanation

 - First, we need to check if the list is empty.
 - Next, we create a temporary Node starting from the "head node" until the last Node, printing your values.

Finally, let's test the print_list_from_head() function in practice:

```python
from singly_linked_list import SinglyLinkedList, Node

if __name__ == "__main__":

    sll = SinglyLinkedList()

    print("####### ( Print values from the 'head' until 'tail' ) ######")
    sll.print_list_from_head()  # Empty list case.

    sll.head = Node(40)  # 40(head)
    sll.print_list_from_head()

    sll.head.next = Node(50)  # 40(head)->50
    sll.print_list_from_head()

    sll.head.next.next = Node(60)  # 40(head)->50->60
    sll.print_list_from_head()
```

**OUTPUT:** 
```bash
###### ( Print values from the 'head' until 'tail' ) ######
List is empty!
40 
40 50 
40 50 60
```

> **NOTE:**  
> See that here we are using the while statement. This is because we don't know how many items are printed.

</details>







































































































<!--- ( Double Linked List ) --->







































































































<!--- ( Circular Linked List ) --->

---

<div id="circular-linked-list-approaches"></div>

## Circular Linked List approaches

> There are generally two types of *Circular Linked Lists*.

 - **Circular Singly Linked List**
 - **Circular Doubly Linked List**

### Circular Singly Linked List

 - In a *Circular Singly Linked List*, the last node of the list contains a pointer to the first node of the list.
 - We traverse the *Circular Singly Linked List* list until we reach the same node where we started.
 - The *Circular Singly Linked List* has no beginning or end.
 - No null value is present in the next part of any of the nodes.

See the image below to understand more easily:

![img](images/cll-01.png)  

**Circular Singly Linked Lists** are similar to *Single Linked Lists* with the exception of connecting the last node to the first node.

### Circular Doubly Linked List

**Circular Doubly Linked List** has properties of both *Doubly Linked List* and *Circular Linked List* in which two consecutive elements are linked or connected by the previous and next pointer and the last node points to the first node by the next pointer and also the first node points to the last node by the previous pointer.

See the image below to understand more easily:

![img](images/cll-02.png)  







































































































<!--- ( REFERENCES ) --->

---

<div id="ref"></div>

## REFERENCES

 - **General:**
   - [Data Structures & Algorithms in Python](https://learning.oreilly.com/library/view/data-structures/9780134855912/)
   - [Runtime Calculator](https://www.timecomplexity.ai/)
   - [Big O Calc](https://www.bigocalc.com/)
   - [ChatGPT](https://chat.openai.com/)
   - [Bard](https://bard.google.com/)
 - **Singly Linked List:**
   - [What is Linked List](https://www.geeksforgeeks.org/what-is-linked-list//)
   - [Insertion in Linked List](https://www.geeksforgeeks.org/insertion-in-linked-list/)
   - [Delete a Linked List node at a given position](https://www.geeksforgeeks.org/delete-a-linked-list-node-at-a-given-position/)
 - **Doubly Linked List:**
   - [Introduction to Doubly Linked List – Data Structure and Algorithm Tutorials](https://www.geeksforgeeks.org/data-structures/linked-list/doubly-linked-list/?ref=appendix)
 - **Circular Linked List:**
   - [Introduction to Circular Linked List](https://www.geeksforgeeks.org/circular-linked-list/)
 - **Standard Template Library (STL):**
   - [List in C++ Standard Template Library (STL)](https://www.geeksforgeeks.org/list-cpp-stl/)
   - [Forward List in C++ | Set 1 (Introduction and Important Functions)](https://www.geeksforgeeks.org/forward-list-c-set-1-introduction-important-functions/)
   - [Forward List in C++ | Set 2 (Manipulating Functions)](https://www.geeksforgeeks.org/forward-list-c-set-2-manipulating-functions/)
   - [C++ boost::circular_buffer](https://cppsecrets.com/users/982115114100104114114971091071171099711464103109971051084699111109/C00-boostcircularbuffer.php)
   - [Circular buffer](https://en.wikipedia.org/wiki/Circular_buffer)

---

**Rodrigo** **L**eite da **S**ilva - **rodrigols89**

<!---
<!--- ( Python ) ->
<details>

<summary>Python</summary>

</br>

[]()
```python

```

**OUTPUT:**  
```bash

```

</details>
--->
