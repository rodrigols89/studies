# Linked Lists

## Contents

 - **Basics:**
   - **Singly Linked List:**
     - [Singly Linked List class (+Explanation how to create Nodes)](#sll-class)
   - **Double Linked List:**
     - [Double Linked List class](#dll-class)
   - **Circular Linked List:**
     - [Circular Linked List approaches](#circular-linked-list-approaches)
     - [Circular Singly Linked List](#circular-singly-linked-list)
     - [Circular Doubly Linked List](#circular-doubly-linked-list)
 - **Length or Size:**
 - **Insertion:**
   - **Singly Linked List:**
     - [Add a new Node at the front (push)](#sll-push)
     - [Add a new Node at the end (append)](#sll-append)
 - **Traversal:**
   - **Singly Linked List:**
     - [Traversing in SinglyLinkedList from the Head until Tail](#sll-print-list-from-head)
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
   - [Advantages and Disadvantages](#ll-advantages-disadvantages)
 - [REFERENCES](#ref)








































---

<!--- ( Basics/Singly Linked List ) --->

<div id="sll-class"></div>

## Singly Linked List class (+Explanation how to create Nodes)

Before implementing a **Singly Linked List** first we need to understand and implement a Node.

To understand what's a Node see the image below:

![img](images/sll-01.png)  

To implement a Node class is very easy. See the code below:

**Python:** [singly_linked_list.py](src/python/singly_linked_list.py)
```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
```

See that the Node class has only two instance variables:

 - **data:**
   - Value to be stored.
 - **next:**
   - Pointer to the next *node*.

Now, let's understand what's a **Singly Linked List**. For example, see the image below:

![img](images/sll-02.png)

See that **Singly Linked List** is composed of many Nodes where:

 - Each Node contains a value stored.
 - And each Node contains a pointer to the next Node.
 - Finally, the last Node contains a pointer to NULL (None).

Let's see how to implement a **Singly Linked List**:

**Python:** [singly_linked_list.py](src/python/singly_linked_list.py)
```python
class SinglyLinkedList(Node):
    def __init__(self):
        self.head = None
```

See that the SinglyLinkedList class:

 - Inherits from the **Node** class:
   - That's, have access to the **"data"** and **"next"** instance variables.
 - Has only **head** instance variable.

Now, let's understand how to initialize the Nodes. Here we have two approaches:

 - ***Initialize* and *link* each Node manually.**
 - **Or using OOP concepts we can instance a SinglyLinkedList class and initialize the Nodes:**
   - Remember that the SinglyLinkedList class inherits from the Node class.
   - That's, have access to the Node class instance variables.

Let's see the first approach:

> ***Initialize* and *link* each Node manually.**

**Python:** [test_nodes_manually.py](src/python/test_nodes_manually.py)
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

    # You don't need to set the next of the last node.
    # By default the next always points to None.
    # third.next = None

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

 - We initialize the **"data"** instance variables using the Node class constructor.
 - We link each Node to the next Node using the **"next"** instance variable.

Now, let's see the second approach:

> ***Using OOP concepts we can instance a SinglyLinkedList class and initialize the Nodes:**

**Python:** [test_nodes_by_sll.py](src/python/test_nodes_by_sll.py)
```python
from singly_linked_list import SinglyLinkedList, Node

if __name__ == "__main__":

    # Singly Linked List instance.
    sll = SinglyLinkedList()

    # Assign data + Link the Nodes.
    sll.head = Node(10)  # 10
    sll.head.next = Node(20)  # 10->20
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

> **NOTE:**  
> - See that in the two approaches we always need to use the Node() class constructor to create new Nodes.
> - This creates a code repetition problem. To solve this we can create functions to create nodes, such as: [push()](#sll-push) and [append()](#sll-append).








































---

<!--- ( Basics/Double Linked List class ) --->

<div id="dll-class"></div>

## Double Linked List class

> A **Doubly Linked List** is composed of connected **"Nodes"**, where each **"Node"** has:

 - **"Data"** stored.
 - A pointer **"prev"** to the previous *Node*.
 - A pointer **"next"** to the next *Node*.

![img](images/dll-01.png)  

See that:

 - The **"prev"** point of the first Node is NULL.
 - The **"next"** point of the last Node also is NULL.

For example, see how represents a **"Node"** *class* for a **Doubly Linked List**:

**Python:** [doubly_linked_list.py](src/python/doubly_linked_list.py)
```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
```








































---

<!--- ( Basics/Circular Linked List ) --->

<div id="circular-linked-list-approaches"></div>

## Circular Linked List approaches

> There are generally two types of *Circular Linked Lists*.

 - **Circular Singly Linked List.**
 - **Circular Doubly Linked List.**

---

<div id="circular-singly-linked-list"></div>

### Circular Singly Linked List

 - In a *Circular Singly Linked List*, the last node of the list contains a pointer to the first node of the list.
 - We traverse the *Circular Singly Linked List* list until we reach the same node where we started.
 - The *Circular Singly Linked List* has no beginning or end.
 - No null value is present in the next part of any of the nodes.

See the image below to understand more easily:

![img](images/cll-01.png)  

**Circular Singly Linked Lists** are similar to *Single Linked Lists* with the exception of connecting the last node to the first node. For example, see the code below:

**Python:**
```python
# Initialize the Nodes.
first  = Node(3)
second = Node(5)
third  = Node(9)

# Connect nodes.
first.next  = second
second.next = third
third.next  = first
```

---

<div id="circular-doubly-linked-list"></div>

### Circular Doubly Linked List

**Circular Doubly Linked List** has properties of both *Doubly Linked List* and *Circular Linked List* in which two consecutive elements are linked or connected by the previous and next pointer and the last node points to the first node by the next pointer and also the first node points to the last node by the previous pointer.

See the image below to understand more easily:

![img](images/cll-02.png)  








































<!--- ( Insertion/Singly Linked List ) --->

---

<div id="sll-push"></div>

## Add a new Node at the front (push)

> Now let's, see how to insert a new Node in the **front of a Singly Linked List (Also called push)**.

For example, imagine we have the following **Singly Linked List**:

```
10->15->20->25
```

If we add item (element) **5** at the *front*, then the **Singly Linked List** becomes:

```
5->10->15->20->25
```

To understand more easily see the image below:

![img](images/sll-push-01.png)  

To apply these mechanics we need to:

 1. Allocate a new Node:
   1.1. Here, we can assign data.
 2. Make "next" of the "new_node" point to head (old first Node).
 3. Move the head to point to the "new_node".

Now, let's see how to implement the **push()** function:

**Python:** [singly_linked_list.py](src/python/singly_linked_list.py)
```python
def push(self, data):
    new_node = Node(data)
    new_node.next = self.head  # Do "new_node" point to old head.
    self.head = new_node  # Set head as "new_node".
```

> **Is this function work in an Empty List?**  
> Yes!

Finally, let's test the function **push()** in practice:

**Python:** [test_push.py](src/python/test_push.py)
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
    sll.push(5)   # 5 (head)->10->15->20->25

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

---

<div id="sll-append"></div>

## Add a new Node at the end (append)

> Now let's, see how to inser a new Node **at the end of a Singly Linked List (Also called append)**.

For example, imagine we have the following **Singly Linked List**:

```
5->10->15->20
```

And we add item (element) **25** at the end, then the **Singly Linked List** becomes:

```
5->10->15->20->25
```

See the image below to understand more easily:

![img](images/ssl-insert-append-01.png)  

The code to do this is:

**Python:** [singly_linked_list.py](src/python/singly_linked_list.py)
```python
def append(self, data):
    new_node = Node(data)
    if self.head is None:
        self.head = new_node
        return
    else:
        # Loop until the last Node (old last Node)
        # and save in the temp_node.
        temp_node = self.head
        while temp_node.next is not None:
            temp_node = temp_node.next
        # Do old last Node point to new last Node.
        temp_node.next = new_node
```

See that:

 - First, we allocate a new Node.
   - **NOTE:** How the "next" instance variable by default is set as *"None"* we don't need to do it manually.
 - Next, we need to check if the *Singly Linked List* is empty, this is because if the *Singly Linked List* is empty, then we need to make the "new_node" as head and stop the method (return).
 - Next, we need to find the last Node (old last Node). For it, let's create a "temp_node" to loop until the last Node (old last Node):
   - In this step we save the old last node in the "temp_node".
 - Finally, we need to set the old last Node to point to the new last Node.

Finally, let's test the **append()** function in practice:

**Python:** [test_append.py](src/python/test_append.py)
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








































---

<!--- ( Traversal/Singly Linked List ) --->

<div id="sll-print-list-from-head"></div>

## Traversing in SinglyLinkedList from the Head until Tail

> An approach to **traverse a Singly Linked List** is to start from the Head until the last Node (Tail).

The code to do this is the following:

[singly_linked_list.py](src/python/singly_linked_list.py)
```python
def print_list_from_head(self):
    if self.head is None:
        print("List is empty!")
        return
    else:
        current_node = self.head
        while current_node is not None:
            print(current_node.data)
            current_node = current_node.next
```

See that:

 - First, we need to check if the list is empty.
 - Next, we create a temporary Node starting from the "head node" until the last Node, printing your values.

Finally, let's test the **print_list_from_head()** function in practice:

**Python:** [test_print_list_from_head.py](src/python/test_print_list_from_head.py)
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

---

<div id="ll-advantages-disadvantages"></div>

## Advantages and Disadvantages

 - **General:**
   - **Advantages:**
     - Dynamic Array.
     - Ease of Insertion/Deletion.
     - Insertion at the beginning is a constant time operation and takes O(1) time:
       - As compared to arrays where inserting an element at the beginning takes **O(n)** time, where **"n"** is the number of elements in the array.
   - **Disadvantages (Drawbacks):**
     - Random access is not allowed. We have to access elements sequentially starting from the first node (head node):
       - So we cannot do a *binary search* with Linked Lists efficiently with its default implementation. 
     - Extra memory space for a *pointer* is required with each element of the list.
     - Not cache-friendly (Não compatível com cache):
     - Since array elements are contiguous locations, there is the locality of reference which is not there in the case of linked lists.
     - It takes a lot of time in traversing and changing the pointers.
     - Reverse traversing is not possible in singly linked lists.
     - It will be confusing when we work with pointers.
     - Direct access to an element is not possible in a linked list as in an array by index.
     - Searching for an element is costly and requires O(n) time complexity.
     - Sorting of linked lists is very complex and costly.
     - Appending an element to a linked list is a costly operation, and takes **O(n)** time, where **"n"** is the number of elements in the linked list:
       - As compared to arrays that take **O(1)** time.








































<!--- ( REFERENCES ) --->

---

<div id="ref"></div>

## REFERENCES

 - [Data Structures & Algorithms in Python](https://learning.oreilly.com/library/view/data-structures/9780134855912/)
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

Ro**drigo** **L**eite da **S**ilva - **drigols**
