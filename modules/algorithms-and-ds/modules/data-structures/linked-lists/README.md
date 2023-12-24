# Linked Lists

## Contents

 - **Singly Linked List:**
   - [Singly Linked List class (+Explanation how to create Nodes)](#sll-class)
   - [Add a new Node at the front (push) | O(1)](#sll-push)
   - [Add a new Node at the end (append) | O(n)](#sll-append)
   - [Add a new Node at the end (append) with constant Time Complexity | O(1)](#sll-append-constant)
   - [Traversing in SinglyLinkedList from the Head until last Node (Tail) | O(n)](#sll-print-list-from-head)
 - **Double Linked List:**
   - [Double Linked List class](#dll-class)
 - **Circular Linked List:**
   - [Circular Linked List approaches](#circular-linked-list-approaches)
 - **Tips & Tricks:**
   - [Linked-Lists: Advantages and Disadvantages](#ll-advantages-disadvantages)
   - [The duplicates items issue](#the-duplicates-issue)
 - [REFERENCES](#ref)





































































































<!--- ( Singly Linked List ) --->

---

<div id="sll-class"></div>

## Singly Linked List class (+Explanation how to create Nodes)

> To start **Singly Linked List** studies first, let's understand what's a **Node**.

See the image below to understand more easily:

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
 - Finally, the last Node contains a pointer to NULL.

Let's see how to implement a **Singly Linked List**:

**Python:** [singly_linked_list.py](src/python/singly_linked_list.py)
```python
class SinglyLinkedList(Node):
    def __init__(self):
        self.head = None
```

See that the **SinglyLinkedList** class:

 - Inherits from the **Node** class:
   - That's, have access to the **"data"** and **"next"** instance variables.
 - Has only **head** instance variable.

Now, let's understand how to initialize the Nodes. Here we have two approaches:

 - ***Initialize* and *link* each Node manually.**
 - **Or using OOP concepts we can instance a SinglyLinkedList class and initialize the Nodes:**
   - Remember that the *SinglyLinkedList* class inherits from the Node class.
   - That's, have access to the Node class instance variables.

Let's see the first approach:

> ***Initialize* and *link* each Node manually.**

**Python:**
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

> **NOTE:**  
> - See that in the two approaches we always need to use the Node() class constructor to create new Nodes.
> - This creates a code repetition problem. To solve this we can create methods to create nodes, such as: [push()](#sll-push) and [append()](#sll-append).

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

Let's, see the code to do this:

**Python:** [singly_linked_list.py](src/python/singly_linked_list.py)
```python
def push(self, data):
    new_node = Node(data)      # O(1)
    new_node.next = self.head  # O(1)
    self.head = new_node       # O(1)
```

$$f(n) = O(1) + O(1) + O(1)$$
$$f(n) = O(1)$$

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

**Python:**
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

Let's, see the code to do this:

**Python:** [singly_linked_list.py](src/python/singly_linked_list.py)
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

$$f(n) = O(1) + O(1) + O(1) + O(1) + O(1) + O(n) + O(1) + O(1)$$
$$f(n) = O(n)$$


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

**Python:**
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

---

<div id="sll-append-constant"></div>

## Add a new Node at the end (append) with constant Time Complexity | O(1)

> Here, let's see how to implement the **append()** method with **constant Time Complexity O(1)**.

First, we need to modify the **SinglyLinkedList()** class to have the *tail attribute (reference)*. This is because the *tail attribute* is used to save the last node in the linked list.

**Python:** [singly_linked_list.py](src/python/singly_linked_list.py)
```python
class SinglyLinkedList(Node):
    def __init__(self):
        self.head = None
        self.tail = None
```

Now, let's see how to implement the **append_constant()** method with **constant Time Complexity O(1)** using the **tail** attribute:

**Python:** [singly_linked_list.py](src/python/singly_linked_list.py)
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

$$f(n) = O(1) + O(1) + O(1) + O(1) + O(1) + O(1)$$
$$f(n) = O(1)$$

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

**Python**
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

---

<!--- ( Traversal/Singly Linked List ) --->

<div id="sll-print-list-from-head"></div>

## Traversing in SinglyLinkedList from the Head until last Node (Tail) | O(n)

> An approach to **traverse a Singly Linked List** is to start from the Head until the last Node (Tail).

The code to do this is the following:

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

$$f(n) = O(1) + O(1) + O(1) + O(1) + O(n) + O(1) + O(1)$$
$$f(n) = O(n)$$

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

**Python:**
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

<!--- ( Double Linked List class ) --->

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

For example, see how to represent a **"Node"** class for a **Doubly Linked List**:

**Python:** [doubly_linked_list.py](src/python/doubly_linked_list.py)
```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
```




































































































---

<!--- ( Circular Linked List ) --->

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

For example, see the code below:

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

### Circular Doubly Linked List

**Circular Doubly Linked List** has properties of both *Doubly Linked List* and *Circular Linked List* in which two consecutive elements are linked or connected by the previous and next pointer and the last node points to the first node by the next pointer and also the first node points to the last node by the previous pointer.

See the image below to understand more easily:

![img](images/cll-02.png)  




































































































---

<!--- ( Tips & Tricks ) --->

<div id="ll-advantages-disadvantages"></div>

## Linked-Lists: Advantages and Disadvantages

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

---

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

Ro**drigo** **L**eite da **S**ilva - **drigols**
