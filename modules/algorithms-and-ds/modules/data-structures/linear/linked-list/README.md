# Linked List

## Contents

 - **Singly Linked List:**
   - ["Node" class representation for Singly a Linked List](#node-class-for-sll)
   - ["Linked List" class representation for a Singly Linked List](#ll-class-for-sll)
   - Singly Linked List Operations:
     - [Traversing in Singly Linked List (printListFromNodeN vs. printListFromHead)](#traversing-sll)
   - Singly Linked List Standard Template Library (STL):
   - [Singly Linked List: Advantages and Disadvantages](#singly-adv-disadv)
   - [Singly Linked List Real Examples](#singly-examples)
 - **Doubly Linked List:**
   - Doubly Linked List Operations:
   - Doubly Linked List Standard Template Library (STL):
   - [Doubly Linked List: Advantages and Disadvantages](#doubly-adv-disadv)
   - [Doubly Linked List Real Examples](#doubly-examples)
 - **Circular Linked List:**
   - Circular Linked List Operations:
   - Circular Linked List Standard Template Library (STL):
   - [Circular Linked List: Advantages and Disadvantages](#circular-adv-disadv)
   - [Circular Linked List Real Examples](#circular-examples)
 - **General:**
   - [Linked List: Advantages and Disadvantages](#adv-disadv)

---

<div id="node-class-for-sll"></div>

## "Node" class representation for a Singly Linked List

How we know a **Linked List** is composed of connected **"Nodes"**, where each **"Node"** has:

 - A **"data"** stored.
 - And a pointer **"next"** to the next *Node*.

![img](images/linked-list-single-in-c.png)  

For example, see how represents a "Node" Data Structure in **C++**:

**C++:**  
[Node.h](src/cpp/singly-linked-list/Node.h)
```cpp
#ifndef NODE_H_
#define NODE_H_

class Node
{
public:
    int data;
    Node *next;

    Node(int data = 0); // Constructor prototype.
};

#endif // NODE_H_
```

**C++:**  
[Node.cpp](src/cpp/singly-linked-list/Node.cpp)
```cpp
#include "Node.h"

// Constructor implementation (definition).
Node::Node(int data)
{
    this->data = data;
    this->next = nullptr;
}
```

---

Now, let's see how represents a "Node" Data Structure in **Python**:

**Python:**  
[Node.py](src/python/singly-linked-list/Node.py)
```python
class Node:

    # Constructor to initialize the node object.
    def __init__(self, data=0):
        self.data = data
        self.next = None  # Initialize "next" reference (pointer).
```

---

<div id="ll-class-for-sll"></div>

## "Linked List" class representation for a Singly Linked List

> How we know a **Linked List** is composed of connected **"Nodes"**.

![img](images/sll-01.png)  

Now, let's see how to implement a **Singly Linked List** in **C++** in practice:

**C++:**  
[SinglyLinkedList.h](src/cpp/singly-linked-list/SinglyLinkedList.h)
```cpp
#ifndef LINKEDLIST_H_
#define LINKEDLIST_H_

#include "Node.h"

class SinglyLinkedList
{
public:
    Node *head;

    SinglyLinkedList(); // Constructor prototype.
};

#endif // LINKEDLIST_H_
```

**C++:**  
[SinglyLinkedList.cpp](src/cpp/singly-linked-list/SinglyLinkedList.cpp)
```cpp
#include "SinglyLinkedList.h"

// Constructor implementation (definition).
SinglyLinkedList::SinglyLinkedList()
{
    this->head = nullptr;
}
```

To test our example, let's use a driver file:

[driver_sinly_linked_list.cpp](src/cpp/singly-linked-list/driver_sinly_linked_list.cpp)
```cpp
#include "SinglyLinkedList.h"
#include <iostream>

int main()
{
    // Node pointers
    Node *head   = nullptr;
    Node *second = nullptr;
    Node *third  = nullptr;

    // Allocate 3 Nodes in the Heap.
    head   = new Node(10); // Assigns data from the constructor.
    second = new Node(20); // Assigns data from the constructor.
    third  = new Node(30); // Assigns data from the constructor.

    // Assign data manually to the Nodes.
    // head->data   = 10;  // assign data in first node.
    // second->data = 20;  // assign data to second node.
    // third->data  = 30;  // assign data to third node

    head->next   = second;  // Link first node with second
    second->next = third;   // Link second node with the first.
    third->next  = nullptr; // Set last Node (tail) as NULL.

    std::cout << "Value in the First Node (head): " << head->data << "\n";
    std::cout << "Value in the Second Node: " << second->data << "\n";
    std::cout << "Value in the Third Node (tail): " << third->data << "\n";

    return 0;
}
```

**COMPILATION AND RUN:**
```cpp
g++ Node.cpp SinglyLinkedList.cpp driver_sinly_linked_list.cpp -o test.out && ./test.out
```

**OUTPUT:**  
```cpp
Value in the First Node (head): 10
Value in the Second Node: 20
Value in the Third Node (tail): 30
```

See that we use two approaches to init data in the "Nodes":

 - Using the constructor of "Node".
 - Set manually.

**NOTE:**  
Another approach to create new "Nodes" is use "next" reference (pointer) in the **Singly Linked List**. For example:

**C++:**
[driver_next_sinly_linked_list.cpp](src/cpp/singly-linked-list/driver_next_sinly_linked_list.cpp)
```cpp
#include "SinglyLinkedList.h"
#include <iostream>

int main()
{
    SinglyLinkedList list;
    list.head = new Node(10);
    list.head->next = new Node(20);
    list.head->next->next = new Node(30);

    // Assign data manually to the Nodes.
    // list.head->data              = 1;  // assign data in first node.
    // list.head->next->data        = 2;  // assign data to second node.
    // list.head->next->next->data  = 3;  // assign data to third node

    std::cout << "Value in the First Node (head): " << list.head->data << "\n";
    std::cout << "Value in the Second Node: " << list.head->next->data << "\n";
    std::cout << "Value in the Third Node (tail): " << list.head->next->next->data << "\n";

    return 0;
}
```

**COMPILATION AND RUN:**
```cpp
g++ Node.cpp SinglyLinkedList.cpp driver_next_sinly_linked_list.cpp -o test.out && ./test.out
```

**OUTPUT:**  
```cpp
Value in the First Node (head): 10
Value in the Second Node: 20
Value in the Third Node (tail): 30
```

---

Now, let's see how implement a **Singly Linked List** in Python:

**Python:**  
[SinglyLinkedList.py](src/python/singly-linked-list/SinglyLinkedList.py)
```python
from Node import Node

class SinglyLinkedList:

    # Constructor to initialize the Node head.
    def __init__(self):
        self.head = None
```

Now, let's test in a drive file:

**Python:**  
[driver_sinly_linked_list.py](src/python/singly-linked-list/driver_sinly_linked_list.py)
```python
from SinglyLinkedList import SinglyLinkedList
from Node import Node

# Node pointers
head = None
second = None
third = None

# Allocate 3 Nodes in the Heap.
head = Node(10)  # Assigns data from the constructor.
second = Node(20)  # Assigns data from the constructor.
third = Node(30)  # Assigns data from the constructor.

# Assign data manually to the Nodes.
# head.data = 10  # assign data in first node.
# second.data = 20  # assign data to second node.
# third.data = 30  # assign data to third node

head.next = second  # Link first node with second
second.next = third  # Link second node with the first.
third.next = None  # Set last Node (tail) as NULL.

print(f"Value in the First Node (head): {head.data}")
print(f"Value in the Second Node: {second.data}")
print(f"Value in the Third Node (tail): {third.data}")
```

**OUTPUT:**  
```
Value in the First Node (head): 10
Value in the Second Node: 20
Value in the Third Node (tail): 30
```

**NOTE:**  
Now, let's use "next" reference (pointer) in the **Singly Linked List** to create new "Nodes". For example:

**Python:**  
[driver_next_sinly_linked_list.py](src/python/singly-linked-list/driver_next_sinly_linked_list.py)
```python
from SinglyLinkedList import SinglyLinkedList
from Node import Node

list = SinglyLinkedList()
list.head = Node(10)
list.head.next = Node(20)
list.head.next.next = Node(30)

# Assign data manually to the Nodes.
# list.head.data = 1  # assign data in first node.
# list.head.next.data = 2  # assign data to second node.
# list.head.next.next.data = 3  # assign data to third node

print("Value in the First Node (head):", list.head.data)
print("Value in the Second Node:", list.head.next.data)
print("Value in the Third Node (tail):", list.head.next.next.data)
```

**OUTPUT:**  
```
Value in the First Node (head): 10
Value in the Second Node: 20
Value in the Third Node (tail): 30
```

---

<div id="traversing-sll"></div>

## Traversing in Singly Linked List (printListFromNodeN vs. printListFromHead)

> Now, let's see how to **traverse a Singly Linked List**.

First, let's create a method (or function) to **traverse a Singly Linked List** *printing* all elements in each node in C++:

[SinglyLinkedList.h](src/cpp/singly-linked-list/SinglyLinkedList.h)
```cpp
class SinglyLinkedList
{
public:

  //...

    void printListFromNodeN(Node* n); // Method prototype.

  //...
};
```

[SinglyLinkedList.cpp](src/cpp/singly-linked-list/SinglyLinkedList.cpp)
```cpp
//...

void SinglyLinkedList::printListFromNodeN(Node *n)
{
    if (n == nullptr)
    {
        std::cout << "Node is empty!"
                  << "\n";
    }
    else
    {
        Node *current_node = n;
        while (current_node != NULL)
        {
            std::cout << current_node->data << " ";
            current_node = current_node->next;
        }
        std::cout << "\n";
    }
}

//...
```

[driver_printListFromNodeN.cpp](src/cpp/singly-linked-list/driver_printListFromNodeN.cpp)
```cpp
#include "SinglyLinkedList.h"
#include <iostream>

int main()
{
    SinglyLinkedList list;

    list.printListFromNodeN(list.head);

    list.head = new Node(10);
    list.head->next = new Node(20);
    list.head->next->next = new Node(30);

    list.printListFromNodeN(list.head);
    list.printListFromNodeN(list.head->next);
    list.printListFromNodeN(list.head->next->next);
    list.printListFromNodeN(list.head->next->next->next);

    return 0;
}
```



**COMPILATION AND RUN:**
```cpp
g++ Node.cpp SinglyLinkedList.cpp driver_printListFromNodeN.cpp -o test.out && ./test.out
```

**OUTPUT:**  
```cpp
Node is empty!
10 20 30 
20 30 
30 
Node is empty!
```

**NOTE:**  
See that we are *print* the list from (a partir) the Node **"n"**:

 - **First, we try to print the list without init a Node "head":**
   - That's, we have a NULL pointer in the *head*.
   - The return was *"Node is empty!"*.
 - **Next, we inited value to three Nodes.**
 - **Next, we try print the values from (a partir) the "head" Node:**
   - The return was *"10 20 30"*.
 - **Next, we try to print the values from (a partir) Node after the "head" Node:**
   - The return was *"20 30"*.
 - **Next, we try to print the values from  (a partir) de last Node:**
   - The return was *"30"*.
 - **Finally, we try to print the value from a NULL Node, that's, next=nullptr:**
   - The return was *"Node is empty!"*.

> **Ok, but how do I print always the Node elements from (a partir) de "head" Node?**

For it, let's create a method (function) **printListFromHead()**:

[SinglyLinkedList.h](src/cpp/singly-linked-list/SinglyLinkedList.h)
```cpp
class SinglyLinkedList
{
public:

  //...

    void printListFromHead(SinglyLinkedList list); // Method prototype.

  //...
};
```

[SinglyLinkedList.cpp](src/cpp/singly-linked-list/SinglyLinkedList.cpp)
```cpp
//...

void SinglyLinkedList::printListFromHead(SinglyLinkedList list)
{
    if (this->head == nullptr)
    {
        std::cout << "List is empty!"
                  << "\n";
    }
    else
    {
        Node *current_node = this->head;
        while (current_node != NULL)
        {
            std::cout << current_node->data << " ";
            current_node = current_node->next;
        }
        std::cout << "\n";
    }
}

//...
```

[driver_printListFromHead.cpp](src/cpp/singly-linked-list/driver_printListFromHead.cpp)
```cpp
#include "SinglyLinkedList.h"
#include <iostream>

int main()
{
    SinglyLinkedList list;
    list.printListFromHead(list);

    list.head = new Node(10);
    list.printListFromHead(list);

    list.head->next = new Node(20);
    list.printListFromHead(list);

    list.head->next->next = new Node(30);
    list.printListFromHead(list);

    return 0;
}
```

**COMPILATION AND RUN:**
```cpp
g++ Node.cpp SinglyLinkedList.cpp driver_printListFromHead.cpp -o test.out && ./test.out
```

**OUTPUT:**  
```cpp
List is empty!
10 
10 20 
10 20 30 
```

**NOTE:**  
See that now we always pass a **Singly Linked List** object and the method prints all Node values from (a partir) the **"head"** node.

---

Now, let's see how to **traverse a Singly Linked List** in Python.

[SinglyLinkedList.py](src/python/singly-linked-list/SinglyLinkedList.py)
```python
#...

# Method to print the Linked List starting from a given node.
def printListFromNodeN(self, n):
    if n is None:
        print("Node is empty!")
    else:
        current_node = n
        while current_node is not None:
            print(current_node.data, end=" ")
            current_node = current_node.next
        print()

# Method to print the entire Linked List starting from the "head".
def printListFromHead(self):
    if self.head is None:
        print("List is empty!")
    else:
        current_node = self.head
        while current_node is not None:
            print(current_node.data, end=" ")
            current_node = current_node.next
        print()

#...
```

[driver_traversing_in_singly_linked_list.py](src/python/singly-linked-list/driver_traversing_in_singly_linked_list.py)
```python
from SinglyLinkedList import SinglyLinkedList
from Node import Node

print("########## (Print values from Node 'n') ##########")

list = SinglyLinkedList()

list.printListFromNodeN(list.head)

list.head = Node(10)
list.head.next = Node(20)
list.head.next.next = Node(30)

list.printListFromNodeN(list.head)
list.printListFromNodeN(list.head.next)
list.printListFromNodeN(list.head.next.next)
list.printListFromNodeN(list.head.next.next.next)

print("\n####### (Print values from the 'head' Node) ######")

list = SinglyLinkedList()

list.printListFromHead()

list.head = Node(40)
list.printListFromHead()

list.head.next = Node(50)
list.printListFromHead()

list.head.next.next = Node(60)
list.printListFromHead()
```

**OUTPUT:**  
```
########## (Print values from Node 'n') ##########
Node is empty!
10 20 30 
20 30 
30 
Node is empty!

####### (Print values from the 'head' Node) ######
List is empty!
40
40 50
40 50 60
```

---

<div id="adv-disadv"></div>

## Linked List: Advantages and Disadvantages

 - **Advantages:**
   - Dynamic Array.
   - Ease of Insertion/Deletion.
   - Insertion at the beginning is a constant time operation and takes O(1) time:
     - As compared to arrays where inserting an element at the beginning takes **O(n)** time, where **"n"** is the number of elements in the array.
 - **Disadvantages (Drawbacks):**
   - Random access is not allowed. We have to access elements sequentially starting from the first node (head node):
     - So we cannot do a binary search with Linked Lists efficiently with its default implementation. 
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

**REFERENCES:**  
[What is Linked List](https://www.geeksforgeeks.org/what-is-linked-list//)  

---

Ro**drigo** **L**eite da **S**ilva - **drigols**
