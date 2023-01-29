# Linked List

## Contents

 - **Theory:**
   - [Intro to Linked List](#intro-to-ll)
   - ["Node" representation in the Linked List](#node-representation)
 - **Singly Linked List:**
   - [Intro to Singly Linked List](#intro-to-sll)
 - **Doubly Linked List:**
   - [Intro to Doubly Linked List](#intro-to-dll)
 - **Circular Linked List:**
   - [Intro to Circular Linked List](#intro-to-cll)

---

<div id="intro-to-ll"></div>

## Intro to Linked List

> A **Linked List** is a *linear data structure* that includes a series of connected **nodes**.

Here, each **node**:

 - Stores the **data**;
 - And the **address** of the next node.

For example,

![img](images/intro-linked-list.png)  

 - You have to start somewhere, so we give the address of the first node a special name called **HEAD**.
 - Also, the last node in the linked list can be identified because its next portion points to **NULL**.

---

<div id="node-representation"></div>

## "Node" representation in the Linked List

Let's see how each **node** of the **linked list** is represented. Each **node** consists:

 - A data item;
 - An address of another node.

We wrap both the data item and the next node reference in a struct as:

**C++ representation:**  
```cpp
// Creating a node
class Node {
public:
    int data;
    Node* next;
};
```

**Python representation:**  
```python
class Node:

    def __init__(self, data):
        self.data = data  # Assign data.
        self.next = None  # Initialize.
```

---

<div id="intro-to-sll"></div>

## Intro to Singly Linked List

**Singly Linked List** is the most common. Each **node** has *data* and a *pointer* to the next **node**:

![img](images/intro-linked-list.png)

For example, see the **Singly Linked List** code below:

**C++:**  
[singly_linked_list.cpp](src/singly_linked_list.cpp)
```cpp
#include <iostream>
using namespace std;

// Node class representation.
class Node
{
public:
    int data;
    Node *next;
};

void printList(Node* n); // Function prototype.

// Driver's code.
int main()
{
    Node *head = NULL;
    Node *second = NULL;
    Node *third = NULL;

    // allocate 3 nodes in the heap.
    head = new Node();
    second = new Node();
    third = new Node();

    head->data = 1;       // assign data in first node.
    head->next = second;  // Link first node with second.

    second->data = 2;     // assign data to second node.
    second->next = third; // Link second node with third.

    third->data = 3;      // assign data to third node.
    third->next = NULL;   // Pointer next to NULL.

    // Function call
    printList(head);

    return 0;
}

// This function prints contents of linked list
void printList(Node* node_n)
{
    while (node_n != NULL)
    {
        cout << node_n->data << " ";
        node_n = node_n->next;
    }
}
```

**Python:**  
[singly_linked_list.py](src/singly_linked_list.py)
```python
class Node:

	# Function (constructor) to initialise the node object.
	def __init__(self, data):
		self.data = data # Assign data.
		self.next = None # Initialize next as NULL (None in Python).


# Linked List class contains a Node object.
class LinkedList:

	# Function (constructor) to initialize the head.
	def __init__(self):
		self.head = None

	# This function prints contents of linked list
	# starting from head
	def printList(self):
		temp = self.head
		while (temp):
			print(temp.data)
			temp = temp.next


# Driver's code.
if __name__ == '__main__':

	# Start with the empty list
	llist = LinkedList()

	llist.head = Node(1) # assign data to first node.
	second = Node(2)     # assign data to second node.
	third = Node(3)      # assign data to third node.

	llist.head.next = second # Link first node with second.
	second.next = third      # Link second node with the third node.

	llist.printList() # Print Node's values.
```

---

<div id="intro-to-dll"></div>

## Intro to Doubly Linked List

> In a **Doubly Linked List** we add a pointer to the *previous* node. Thus, we can go in either direction: **forward** or **backward**.

![img](images/DLL1.png)  

For example, see the **Doubly Linked List** code below:

**C++:**  
[doubly_linked_list_node.cpp](src/doubly_linked_list_node.cpp)
```cpp
#include <iostream>
using namespace std;

// Node of a doubly linked list
class Node {
public:
    int data;
    Node *next; // Pointer to next node in DLL.
    Node *prev; // Pointer to previous node in DLL.
};
```

**Python:**  
[doubly_linked_list_node.py](src/doubly_linked_list_node.py)
```python
class Node:

  # Node constructor.
	def __init__(self, data=None, next=None, prev=None):
		self.data = data
		self.next = next # reference to next node in DLL.
		self.prev = prev # reference to previous node in DLL.
```

---

<div id="intro-to-cll"></div>

## Intro to Circular Linked List

> A **Circular Linked List** is a variation of a *Linked List* in which the last element is linked to the first element. **This forms a circular loop**.

![img](images/circular-linked-list.webp)  

A **Circular Linked List** can be either *Singly Linked* or *Doubly Linked*:

 - For *Singly Linked List*, next pointer of last item points to the first item.
 - In the *Doubly Linked List*, prev pointer of the first item points to the last item as well.

---

**REFERENCES:**  
[Types of Linked List - Singly linked, doubly linked and circular](https://www.programiz.com/dsa/linked-list-types)  
[Linked list Data Structure](https://www.programiz.com/dsa/linked-list)  
[What is Linked List](https://www.geeksforgeeks.org/what-is-linked-list//)  

---

Ro**drigo** **L**eite da **S**ilva - **drigols**
