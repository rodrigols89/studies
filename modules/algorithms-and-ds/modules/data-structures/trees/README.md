# Trees

## Contents

 - **Basics:**
   - [Tree Terminology](#tree-terminology)
 - [**Binary Tree (+Node class implementation)**](#intro-to-binary-tree)
   - Basic operations on Binary Tree:
     - [Tree Traversal Techniques:](#ttt)
       - [Depth First Search (DFS):](#depth-first-search)
         - [Preorder Traversal (current-left-right)](#preorder-traversal)
         - [Inorder Traversal (left-current-right)](#inorder-traversal)
         - [Postorder Traversal (left-right-current)](#postorder-traversal)
       - Breadth-First Search (BFS):
         - Level Order Traversal
     - Inserting
     - Searching
     - Removing
     - Deletion
   - Auxiliary operations on Binary Tree:
     - Finding the height of the tree
     - Find the level of the tree
     - Finding the size of the entire tree
   - Special types of Binary Tree:
     - [Binary Search Tree (+Class implementation)](#intro-to-binary-search-tree)
       - Inserting:
         - [Inserting in a Binary Search Tree (Recursive Approach)](#insert-bst-recursive-approach)
         - [Inserting in a Binary Search Tree (Iterative Approach)](#insert-bst-iterative-approach)
 - [**REFERENCES**](#ref)








































<!--- ( Basics ) --->

---

<div id="tree-terminology"></div>

## Tree Terminology

A Tree consists of **"Nodes"** connected by **"Edges"**.

![img](images/trees-01.jpg)  

In such a picture of a tree:

 - The **"Nodes"** are represented as circles.
 - And the **"Edges"** as lines connecting the circles.

Many terms are used to describe particular aspects of trees. For example, see the image below:

![img](images/trees-02.png)  








































<!--- ( Binary Tree ) --->

---

<div id="intro-to-binary-tree"></div>

## Binary Tree (+Node class implementation)

> A **Binary Tree** is a *tree* data structure in which each parent node can have at most two children.

Each node of a binary tree consists of three items:

 - Data *item (or key)*.
 - Address of *left child*.
 - Address of *right child*.

For example:

![img](images/binary-tree-00.png)  

A common approach to work with ***Binary Trees*** is to create a ***Node*** class to represent our nodes in the Tree.

For example:

[trees.py](src/python/trees.py)
```python
class Node:
    def __init__(self, key):
        self.leftChild = None
        self.rightChild = None
        self.key = key
```

Now, let's test in the practice:

```python
from trees import Node

if __name__ == "__main__":

    #     1 (root)
    #    / \
    # None None
    root = Node(1)
    print(root.key)

    #         1 (root)
    #        /  \
    #       /    \
    #      /      \
    #     2         3
    #    / \       / \
    # None None None None
    root.left = Node(2)
    root.right = Node(3)
    print(root.left.key)
    print(root.right.key)

    #         1 (root)
    #        /  \
    #       /    \
    #      /      \
    #     2         3
    #    / \       / \
    #   4  None  None None
    #  / \
    # None None
    root.left.left = Node(4)
    print(root.left.left.key)
```

**OUTPUT:**
```bash
1
2
3
4
```








































<!--- ( Binary Tree/Basic operations on Binary Tree/Traversing ) --->

---

<div id="ttt"></div>

## Tree Traversal Techniques

> Unlike **Linear Data Structures (Array, Strings, Vectors, Linked Lists, Queues, Stacks)** which have only one logical way to traverse them, *Trees* can be traversed in different ways.

 - **Depth First Search (DFS):**
   - Preorder Traversal (current-left-right)
   - Inorder Traversal (left-current-right)
   - Postorder Traversal (left-right-current)
 - **Breadth First Search (BFS):**
   - Level Order Traversal
 - **Boundary Traversal**
 - **Diagonal Traversal**

**NOTE:**  
To remember the **Depth First Search (DFS)** approaches see that:

 - **Preorder -** The *current (root)* is the *first*.
 - **Inorder -** The *current (root)* is the *second*.
 - **Postorder -** The *current (root)* is the *third*.
 - **NOTE:** The "left" is always the first node visited before the "right" node.

---

<div id="depth-first-search"></div>

## Depth First Search (DFS)

> **Depth-First Search (DFS)** is an algorithm used for *searching* or *traversing* **Tree** or **Graph** data structures.

We have two approaches to implementing the **Depth First Search (DFS)** Algorithm:

 - **Recursive Implementation:**
   - The recursive approach does not explicitly rely (depende) on a stack for tree traversal since (pois) *the stack is implicitly managed by the programming language's* **call stack**.
 - **Iterative Implementation:**
   - The iterative approach uses a **Stack (Last In, First Out (LIFO))** to store the visited Nodes.
   - *Stack* also is used to maintain (manter) control of the tree traversal process.
   - The *stack* also is used to store the nodes that still need to be processed.
   - The use of the *stack* in the iterative approach allows for a non-recursive tree traversal and is particularly useful in situations where recursion can lead (levar) to a *stack overflow* in **very large** or **deep trees**.
   - Additionally, the iterative approach can be more efficient in terms of resource consumption compared to the recursive approach in certain cases.

---

<div id="preorder-traversal"></div>

## Preorder Traversal (current-left-right)

> This technique follows the **'CURRENT->LEFT->RIGHT'** policy.

 - It means that, *first root (current) node* is visited.
 - After that, the *left subtree* is traversed recursively.
 - Finally, *right subtree* is recursively traversed.

To understand more easily, imagine we have the following *Tree*:

![img](images/tree-example-01.png)  

**NOTE:**  
If you pay attention you can see that the Tree has another subtrees:

![img](images/tree-example-02.png)  

> **NOTE:**  
> All subtree (and all the Tree) follow the **Preorder** policy - **'CURRENT->LEFT->RIGHT'**.

Until all nodes of the *Tree* are not visited:

 - **Step 1 -** Visit the root (current) node.
 - **Step 2 -** Traverse the left subtree recursively.
 - **Step 3 -** Traverse the right subtree recursively.

![img](images/visual-preorder-01.gif)

> **NOTE:**  
> See that here we start from the root and next follow the **'CURRENT->LEFT->RIGHT'** policy.

Now, let's see how to implement the **preorder** method using **Recursive approach** to do this:

[trees.py](src/python/trees.py)
```python
def preorder(self):
    if self.isEmpty():
        print("Tree is empty.")
        return
    result = []
    self._preorder_recursive(self.root, result)
    return result

def _preorder_recursive(self, current_node, result):
    if current_node:
        result.append(current_node.key)
        self._preorder_recursive(current_node.leftChild, result)
        self._preorder_recursive(current_node.rightChild, result)
```

See that:

 - We have two functions `preorder()` and `_preorder_recursive()`:
 - `preorder():`
   - First this function checks if the Tree is empty.
   - If the Tree is not empty, then:
     - Create an empty list.
     - Next, call the `_preorder_recursive()` function and pass as argument the Tree root and the empty list.
     - Finally, return the recursion result as a list.
 - `_preorder_recursive():`
   - First, the `_preorder_recursive()` function checks if the current_node is empty (We could ignore this check because we passed the root Node as the argument that was checked in the preorder() function):
   - If the current_node is not empty (None):
     - Append (add at the end of the list) the value of the current_node to the list (result).
     - Call recursively the `_preorder_recursive()` function and pass as argument the left Node (current_node.leftChild) and the list (result):
       - That's, append (add at the end of the list) the current value/key and move to the left subtree recursively.
     - Call recursively the `_preorder_recursive()` function and pass as argument the right Node (current_node.rightChild) and the list (result):
       - That's, append (add at the end of the list) the current value/key and move to the right subtree recursively.

Now, let's test in the practice:

```python
from trees import BinarySearchTree

if __name__ == "__main__":

    bst = BinarySearchTree()

    bst.insert(25, approach="iterative")
    bst.insert(20, approach="iterative")
    bst.insert(36, approach="iterative")
    bst.insert(10, approach="iterative")
    bst.insert(30, approach="iterative")
    bst.insert(40, approach="iterative")
    bst.insert(22, approach="iterative")
    bst.insert(28, approach="iterative")
    bst.insert(5, approach="iterative")
    bst.insert(1, approach="iterative")
    bst.insert(8, approach="iterative")
    bst.insert(12, approach="iterative")
    bst.insert(30, approach="iterative")
    bst.insert(15, approach="iterative")
    bst.insert(36, approach="iterative")
    bst.insert(48, approach="iterative")
    bst.insert(36, approach="iterative")
    bst.insert(50, approach="iterative")

    print("Preorder:", bst.preorder())
```

**OUTPUT:**
```bash
Preorder: [25, 20, 10, 5, 1, 8, 12, 15, 22, 36, 30, 28, 30, 36, 36, 40, 48, 50]
```

---

<div id="inorder-traversal"></div>

## Inorder Traversal (left-current-right)

> This technique follows the **'LEFT->CURRENT->RIGHT'** policy.

 - It means that first *left subtree is visited*.
 - After, the *root (current) node is traversed*.
 - Finally, the *right subtree is traversed*.

To understand more easily, imagine we have the following *Tree*:

![img](images/tree-example-01.png)  

**NOTE:**  
If you pay attention you can see that the Tree has another subtrees:

![img](images/tree-example-02.png)  

> **NOTE:**  
> All subtrees (and all the Tree) follow the **Inorder** policy - **'LEFT->CURRENT->RIGHT'**.

Until all nodes of the *Tree* are not visited:

  - **Step 1 -** Traverse the *left subtree* recursively.
  - **Step 2 -** Visit the *root (current) node*.
  - **Step 3 -** Traverse the *right subtree* recursively.

![img](images/visual-inorder-01.gif)

> **NOTE:**  
> See that here we start from the last left subtree (two sides) following the **'LEFT->CURRENT->RIGHT'** policy.

Now, let's see how to implement the **inorder** method using **Recursive approach** to do this:

[trees.py](src/python/trees.py)
```python
def inorder(self):
    if self.isEmpty():
        print("Tree is empty.")
        return
    result = []
    self._inorder_recursive(self.root, result)
    return result

def _inorder_recursive(self, current_node, result):
    if current_node:
        self._inorder_recursive(current_node.leftChild, result)
        result.append(current_node.key)
        self._inorder_recursive(current_node.rightChild, result)
```

See that:

 - We have two functions `inorder()` and `_inorder_recursive()`:
 - `inorder():`
   - First this function checks if the Tree is empty.
   - If the Tree is not empty, then:
     - Create an empty list.
     - Next, call the `_inorder_recursive()` function and pass as argument the Tree root and the empty list.
     - Finally, return the recursion result as a list.
 - `_inorder_recursive():`
   - First, the `_inorder_recursive()` function checks if the current_node is empty (We could ignore this check because we passed the root Node as the argument that was checked in the preorder() function):
   - If the current_node is not empty (None):
     - Call recursively the `_inorder_recursive()` function and pass as argument the left Node (current_node.leftChild) and the list (result):
       - That's, move to the left subtree recursively.
     - Append (add at the end of the list) the value of the current_node to the list (result).
     - Call recursively the `_inorder_recursive()` function and pass as argument the right Node (current_node.rightChild) and the list (result):
       - That's, append (add at the end of the list) the current value/key and move to the right subtree recursively.

Now, let's test in the practice:

```python
from trees import BinarySearchTree

if __name__ == "__main__":

    bst = BinarySearchTree()

    bst.insert(25, approach="iterative")
    bst.insert(20, approach="iterative")
    bst.insert(36, approach="iterative")
    bst.insert(10, approach="iterative")
    bst.insert(30, approach="iterative")
    bst.insert(40, approach="iterative")
    bst.insert(22, approach="iterative")
    bst.insert(28, approach="iterative")
    bst.insert(5, approach="iterative")
    bst.insert(1, approach="iterative")
    bst.insert(8, approach="iterative")
    bst.insert(12, approach="iterative")
    bst.insert(30, approach="iterative")
    bst.insert(15, approach="iterative")
    bst.insert(36, approach="iterative")
    bst.insert(48, approach="iterative")
    bst.insert(36, approach="iterative")
    bst.insert(50, approach="iterative")

    print("Inorder:", bst.inorder())
```

**OUTPUT:**
```bash
Inorder: [1, 5, 8, 10, 12, 15, 20, 22, 25, 28, 30, 30, 36, 36, 36, 40, 48, 50]
```

---

<div id="postorder-traversal"></div>

## Postorder Traversal (left-right-current)

> This technique follows the **'LEFT->RIGHT->CURRENT'** policy.

 - It means that the first *left subtree* of the *root node is traversed*.
 - After that, recursively traverses the *right subtree*.
 - Finally, the *root node* is traversed.

To understand more easily, imagine we have the following *Tree*:

![img](images/tree-example-01.png)  

**NOTE:**  
If you pay attention you can see that the Tree has another subtrees:

![img](images/tree-example-02.png)  

> **NOTE:**  
> All subtrees (and all the Tree) follow the **Postorder** policy - **'LEFT->RIGHT->CURRENT'**.

Until all nodes of the *Tree* are not visited:

 - **Step 1 -** Traverse the *left subtree* recursively.
 - **Step 2 -** Traverse the *right subtree* recursively.
 - **Step 3 -** Visit the *root node*.

![img](images/visual-postorder-01.gif)

> **NOTE:**  
> - See that here we start from the last left Node of the Tree, then follow the **'LEFT->RIGHT->CURRENT'** policy.
> - Start from the last left Node of the Tree because is the last left Node of all the Tree and all the Tree follow the **'LEFT->RIGHT->CURRENT'** policy.

Now, let's see how to implement the **postorder** method using **Recursive approach** to do this:

[trees.py](src/python/trees.py)
```python
def postorder(self):
    if self.isEmpty():
        print("Tree is empty.")
        return
    result = []
    self._postorder_recursive(self.root, result)
    return result

def _postorder_recursive(self, current_node, result):
    if current_node:
        self._postorder_recursive(current_node.leftChild, result)
        self._postorder_recursive(current_node.rightChild, result)
        result.append(current_node.key)
```

See that:

 - We have two functions `postorder()` and `_postorder_recursive()`:
 - `postorder():`
   - First this function checks if the Tree is empty.
   - If the Tree is not empty, then:
     - Create an empty list.
     - Next, call the `_postorder_recursive()` function and pass as argument the Tree root and the empty list.
     - Finally, return the recursion result as a list.
 - `_postorder_recursive():`
   - First, the `_postorder_recursive()` function checks if the current_node is empty (We could ignore this check because we passed the root Node as the argument that was checked in the preorder() function):
   - If the current_node is not empty (None):
     - Call recursively the `_postorder_recursive()` function and pass as argument the left Node (current_node.leftChild) and the list (result):
       - That's, move to the left subtree recursively.
     - Call recursively the `_postorder_recursive()` function and pass as argument the right Node (current_node.rightChild) and the list (result):
       - That's, move to the right subtree recursively.
     - Append (add at the end of the list) the value of the current_node to the list (result).

Now, let's test in the practice:

```python
from trees import BinarySearchTree

if __name__ == "__main__":

    bst = BinarySearchTree()

    bst.insert(25, approach="iterative")
    bst.insert(20, approach="iterative")
    bst.insert(36, approach="iterative")
    bst.insert(10, approach="iterative")
    bst.insert(30, approach="iterative")
    bst.insert(40, approach="iterative")
    bst.insert(22, approach="iterative")
    bst.insert(28, approach="iterative")
    bst.insert(5, approach="iterative")
    bst.insert(1, approach="iterative")
    bst.insert(8, approach="iterative")
    bst.insert(12, approach="iterative")
    bst.insert(30, approach="iterative")
    bst.insert(15, approach="iterative")
    bst.insert(36, approach="iterative")
    bst.insert(48, approach="iterative")
    bst.insert(36, approach="iterative")
    bst.insert(50, approach="iterative")

    print("Postorder:", bst.postorder())
```

**OUTPUT:**
```bash
Postorder: [1, 8, 5, 15, 12, 10, 22, 20, 30, 28, 36, 36, 30, 50, 48, 40, 36, 25]
```








































<!--- ( Binary Tree/Special types of Binary Tree/Binary Search Tree ) --->

---

<div id="intro-to-binary-search-tree"></div>

## Binary Search Tree (+Class implementation)

**Binary Search Tree** is a *node-based binary tree* data structure that has the following properties:

 - All nodes of the **left subtree** are `less than` the **root node**.
 - All nodes of **right subtree** are `more than` the **root node**.
 - Both subtrees of each node are also **Binary Search Tree**.
   - In other words, they have the above two properties

For example:

![img](images/bst-01.png)  

To implement the ***Binary Search Tree class*** let's get started by implementing the class *constructor*:

[trees.py](src/python/trees.py)
```python
class Node:
    def __init__(self, key):
        self.leftChild = None
        self.rightChild = None
        self.key = key


class BinarySearchTree(Node):
    def __init__(self):
        self.root = None
```

Now, let's implement the **isEmpty()** method to check if the **Binary Search Tree** is empty:

[trees.py](src/python/trees.py)
```python
def isEmpty(self):
    return self.root is None
```

Now, let's test in the practice:

```python
from trees import BinarySearchTree

if __name__ == '__main__':

    bst = BinarySearchTree()

    print("The Binary Search Tree is empty? ", bst.isEmpty())
```

**OUTPUT:**
```bash
The Binary Search Tree is empty? True
```

---

<div id="insert-bst-recursive-approach"></div>

## Inserting in a Binary Search Tree (Recursive Approach)

> A **new key** is always inserted at the *leaf (folha)* by maintaining the *property* of the Binary Search Tree.

![img](images/inserting-bst.gif)  

For example, let's see how to insert a new node (data/key) in the ***Binary Search Tree*** using a *recursive approach*:

[trees.py](src/python/trees.py)
```python
def insert(self, key, approach="recursive"):
    if self.isEmpty():
        self.root = Node(key)
    else:
        if approach == "recursive":
            self._insert_recursive(self.root, key)
        elif approach == "iterative":
            self._insert_iterative(self.root, key)
        else:
            print("Invalid approach. Please use 'recursive' or 'iterative'.")

def _insert_recursive(self, current_node, key):
    if key <= current_node.key:
        if current_node.leftChild is None:
            current_node.leftChild = Node(key)
        else:
            self._insert_recursive(current_node.leftChild, key)
    elif key >= current_node.key:
        if current_node.rightChild is None:
            current_node.rightChild = Node(key)
        else:
            self._insert_recursive(current_node.rightChild, key)
```

See that:

 - We have two methods `"insert() public"` and `"_insert_recursive() private"`:
 - `insert():`
   - This method first checks if the *Binary Search Tree* is empty:
     - If the Tree is empty, it creates a new Node (value/key) as root.
   - If it's not empty, it calls the private method `"_insert_recursive()"`:
     - That's, we need to insert a new value (key) into the Tree with existing values.
 - `_insert_recursive() - This is the real method to insert a new value into the not empty Tree:`
   - This method receives the following arguments:
     - **current_node:** The first time, the "current_node" will be the "root" and loop Node by Node when necessary.
     - **key:** The "key" is the value to be inserted at the new Node.
   - Inside of the `_insert_recursive()` method the first thing to check is the side to move, left or right:
     - `"if key <= current_node.key"`:
       - If the *"key"* `is less or equal` to *"the key of the current_node"*, we move to the left subtree.
       - **NOTE:** This approach allows the insertion of *duplicate values*. If you don't wish allow change `"<="` to `"<"`.
     - `"elif key >= current_node.key"`:
       - If the *"key"* `is greater or equal` to *"the key of the current_node"*, we move to the right subtree.
       - **NOTE:** This approach allows the insertion of *duplicate values*. If you don't wish allow change `">="` to `">"`.
   - Next, we need to check if the *"current_node.left/right"* are empty (`"if current_node.leftChild is None" | "if current_node.rightChild is None"`):
     - If the *"current_node.left/right"* `is empty (None)`, then we must insert the new Node (value/key) here.
     - If the *"current_node.left/right"* `is not empty`, then we need to move recursively to the next Node (left or right):
       - `"self._insert_recursive(current_node.leftChild, key)"`
       - `"self._insert_recursive(current_node.rightChild, key)"`
       - **NOTE:** See that here we pass the *"current_node.left/right"* to the `_insert_recursive()` method, not the *root* Node.
       - **Base case (condiction to stop the recursion):**
         - The new Node (value/key) was created.
         - When the new Node (value/key) is created we don't call the `_insert_recursive()` method again recursively.

Now, let's test in the practice:

```python
from trees import BinarySearchTree

if __name__ == "__main__":

    bst = BinarySearchTree()

    bst.insert(25, approach="recursive")
    bst.insert(20, approach="recursive")
    bst.insert(36, approach="recursive")
    bst.insert(10, approach="recursive")
    bst.insert(30, approach="recursive")
    bst.insert(40, approach="recursive")
    bst.insert(22, approach="recursive")
    bst.insert(28, approach="recursive")
    bst.insert(5, approach="recursive")
    bst.insert(1, approach="recursive")
    bst.insert(8, approach="recursive")
    bst.insert(12, approach="recursive")
    bst.insert(30, approach="recursive")
    bst.insert(15, approach="recursive")
    bst.insert(36, approach="recursive")
    bst.insert(48, approach="recursive")
    bst.insert(36, approach="recursive")
    bst.insert(50, approach="recursive")

    result = bst.inorder()
    print(result)
```

**OUTPUT:**
```bash
[1, 5, 8, 10, 12, 15, 20, 22, 25, 28, 30, 30, 36, 36, 36, 40, 48, 50]
```

---

<div id="insert-bst-iterative-approach"></div>

## Inserting in a Binary Search Tree (Iterative Approach)

> A **new key** is always inserted at the *leaf (folha)* by maintaining the *property* of the Binary Search Tree.

![img](images/inserting-bst.gif)  

For example, let's see how to insert a new node (data/key) in the ***Binary Search Tree*** using a *Iterative Approach*:

[trees.py](src/python/trees.py)
```python
def _insert_iterative(self, current_node, key):
    while True:
        if key <= current_node.key:
            if current_node.leftChild is None:
                current_node.leftChild = Node(key)
                break
            else:
                current_node = current_node.leftChild
        elif key >= current_node.key:
            if current_node.rightChild is None:
                current_node.rightChild = Node(key)
                break
            else:
                current_node = current_node.rightChild
```

See that:

 - **Again we have two function:**
   - `inser():` To check if the *Binary Search Tree* is empty and select the appropriate approach (recursive or iterative).
   - `_insert_iterative():` To insert a new value (key) into the Tree with existing values.
 - `_insert_iterative():`
   - Inside the `_insert_iterative() function` we have a `loop "while" (infinite loop)` to through (percorrer) the Tree:
     - Inside the `"while" loop`:
       - `"if key <= current_node.key"`:
         - If the *"key"* `is less or equal` to *"the key of the current_node"*, we move to the left subtree.
         - **NOTE:** This approach allows the insertion of *duplicate values*. If you don't wish allow change `"<="` to `"<"`.
       - `"elif key >= current_node.key"`:
         - If the *"key"* `is greater or equal` to *"the key of the current_node"*, we move to the right subtree.
         - **NOTE:** This approach allows the insertion of *duplicate values*. If you don't wish allow change `">="` to `">"`.
       - Next, we need to check if the *"current_node.left/right"* are empty (`"if current_node.leftChild is None" | "if current_node.rightChild is None"`):
         - If the *"current_node.left/right"* `is empty (None)`, then we must insert the new Node (value/key) here and `"break"` the `"while" loop`.
         - If the *"current_node.left/right"* `is not empty`, then we need to move to the next Node (left or right):
           - `"current_node = current_node.leftChild"`
           - `"current_node = current_node.rightChild"`

Now, let's test in the practice:

```python
from trees import BinarySearchTree

if __name__ == "__main__":

    bst = BinarySearchTree()

    bst.insert(25, approach="iterative")
    bst.insert(20, approach="iterative")
    bst.insert(36, approach="iterative")
    bst.insert(10, approach="iterative")
    bst.insert(30, approach="iterative")
    bst.insert(40, approach="iterative")
    bst.insert(22, approach="iterative")
    bst.insert(28, approach="iterative")
    bst.insert(5, approach="iterative")
    bst.insert(1, approach="iterative")
    bst.insert(8, approach="iterative")
    bst.insert(12, approach="iterative")
    bst.insert(30, approach="iterative")
    bst.insert(15, approach="iterative")
    bst.insert(36, approach="iterative")
    bst.insert(48, approach="iterative")
    bst.insert(36, approach="iterative")
    bst.insert(50, approach="iterative")

    result = bst.inorder()
    print(result)
```

**OUTPUT:**
```bash
[1, 5, 8, 10, 12, 15, 20, 22, 25, 28, 30, 30, 36, 36, 36, 40, 48, 50]
```








































<!--- ( REFERENCES ) --->

---

<div id="ref"></div>

## REFERENCES

 - [Data Structures & Algorithms in Python](https://learning.oreilly.com/library/view/data-structures/9780134855912/)
 - [Introduction to Binary Tree – Data Structure and Algorithm Tutorials](https://www.geeksforgeeks.org/introduction-to-binary-tree-data-structure-and-algorithm-tutorials/)
 - [Types of Binary Tree](https://www.geeksforgeeks.org/types-of-binary-tree/)
 - [Applications, Advantages and Disadvantages of Binary Tree](https://www.geeksforgeeks.org/applications-advantages-and-disadvantages-of-binary-tree/)
 - [Applications, Advantages and Disadvantages of Binary Search Tree](https://www.geeksforgeeks.org/applications-advantages-and-disadvantages-of-binary-search-tree/)
 - [Insertion in Binary Search Tree (BST)](https://www.geeksforgeeks.org/insertion-in-binary-search-tree/)
 - [Depth-First Search: Conceptual](https://www.codecademy.com/article/depth-first-search-conceptual)
 - [Depth-first search - wikipedia](https://en.wikipedia.org/wiki/Depth-first_search)
 - [Learn Depth-First Search(DFS) Algorithm From Scratch](https://www.simplilearn.com/tutorials/data-structure-tutorial/dfs-algorithm)
 - [Tree traversal (Inorder, Preorder an Postorder)](https://www.javatpoint.com/tree-traversal)
 - [Tree Traversal: Breadth-First Search vs Depth-First Search](https://www.codecademy.com/article/tree-traversal)
 - [Boundary Traversal of Binary Tree](https://www.codingninjas.com/studio/problems/boundary-traversal_790725)
 - [Perform boundary traversal on a binary tree](https://www.techiedelight.com/boundary-traversal-binary-tree/)
 - [Boundary Traversal of a Binary Tree](https://takeuforward.org/data-structure/boundary-traversal-of-a-binary-tree/)
 - [Diagonal Traversal of Binary Tree](https://www.geeksforgeeks.org/diagonal-traversal-of-binary-tree/)

---

Ro**drigo** **L**eite da **S**ilva - **drigols**
