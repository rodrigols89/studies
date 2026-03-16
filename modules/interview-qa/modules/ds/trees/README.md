# Trees

## Contents

 - **Fundamentals:**
   - [`What are the components of a tree?`](#tree-terminology)
   - [`How do you determine the height (altura) and depth (profundidade) of a tree "node"?`](#tree-height-depth)
   - [`How do I create a class to represent a Node in a tree?`](#node-class-for-bt)
 - **Types of Trees:**
   - **Binary Tree based on the number of children:**
     - [`When is a tree considered a "Full Binary Tree"?`](#intro-to-full-binary-tree)
     - [`When is a tree considered a "Degenerate (or pathological) Binary Tree"?`](#intro-to-degenerate-binary-tree)
     - [`When is a tree considered a "Skewed Binary Tree"?`](#intro-to-skewed-binary-tree)
   - **Binary Tree based on completion of levels:**
     - [`When is a tree considered a "Complete Binary Tree"?`](#intro-to-complete-binary-tree)
     - [`When is a tree considered a "Perfect Binary Tree"?`](#intro-to-perfect-binary-tree)
     - [`When is a tree considered a "Balanced Binary Tree (Also known as Height Balanced Tree)"?`](#intro-to-balanced-binary-tree)
   - **Special Types of Trees:**
     - [`Binary Search Tree (BST)`](#intro-to-binary-search-tree)
     - AVL Tree
     - Red Black Tree
     - B Tree
     - B+ Tree
     - Segment Tree
 - [**Tree Traversal Techniques:**](#ttt)
   - [**Depth First Search (DFS):**](#depth-first-search)
     - [**Preorder Traversal**](#preorder-traversal)
       - [`How do I implement a preorder traversal function?`](#preorder-implementation)
     - [**Inorder Traversal**](#inorder-traversal)
       - [`How do I implement a inorder traversal function?`](#inorder-implementation)
     - [**Postorder Traversal**](#postorder-traversal)
       - [`How do I implement a postorder traversal function?`](#postorder-implementation)
   - **Breadth-First Search (BFS):**
     - Level Order Traversal
 - [**REFERENCES**](#ref)
<!---
[WHITESPACE RULES]
- Same topic = "10" Whitespace character.
- Different topic = "100" Whitespace character.
--->





































































































<!--- ( Fundamentals ) --->

---

<div id="tree-terminology"></div>

## `What are the components of a tree?`

<details>

<summary>ANSWER</summary>

<br/>

A Tree consists of **"Nodes"** connected by **"Edges"**.

![img](images/trees-01.jpg)  

In such a picture of a tree:

 - The **"Nodes"** are represented as circles.
 - And the **"Edges"** as lines connecting the circles.

Many terms are used to describe particular aspects of trees. For example, see the image below:

![img](images/trees-02.png)  

</details>










---

<div id="tree-height-depth"></div>

## `How do you determine the height (altura) and depth (profundidade) of a tree "node"?`

<details>

<summary>ANSWER</summary>

<br/>

> To know the *Tree's Height* and *Depth*, **we need to focus on each Node** ➔ **not the entire tree**.

For each *node* in a tree, we can define two features:

 - **Height:**
   - A **"node height"** is the number of edges from the *current Node* to the most distant *leaf* node.
 - **Depth:**
   - A **"node depth"** is the number of edges from the *current node* to the *root*.

For example, see the image below to understand more easily:

![img](images/tree-height-depth.png)  

</details>










---

<div id="node-class-for-bt"></div>

## `How do I create a class to represent a Node in a tree?`

<details>

<summary>Python</summary>

<br/>

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

</details>






































































































<!--- ( Types of Trees/Binary Tree based on the number of children ) --->

---

<div id="intro-to-full-binary-tree"></div>

## `When is a tree considered a "Full Binary Tree"?`

<details>

<summary>ANSWER</summary>

<br/>

A **Binary Tree** is a **Full Binary Tree** if every node has **0** or **2 children**.

For example:

![img](images/full-binary-tree-01.png)  

</details>










---

<div id="intro-to-degenerate-binary-tree"></div>

## `When is a tree considered a "Degenerate (or pathological) Binary Tree"?`

<details>

<summary>ANSWER</summary>

<br/>

A **Binary Tree** is a **Degenerate (or pathological) Binary Tree** when every internal node has **one child**.

![img](images/degenerate-binary-tree-01.png)  

> **NOTE:**  
> A degenerate or pathological tree is a tree having a single child either left or right.

</details>










---

<div id="intro-to-skewed-binary-tree"></div>

## `When is a tree considered a "Skewed Binary Tree"?`

<details>

<summary>ANSWER</summary>

<br/>

We have two ways to implement a **Skewed Binary Tree**:

 - **Left-Skewed Binary Tree:**
   - All the nodes are having a left child or no child at all.
   - It is a *left side dominated* tree.
   - All the right children remain as *null*.
 - **Right-Skewed Binary Tree:**
    - All the nodes are having a right child or no child at all.
    - It is a *right side dominated* tree.
    - All the left children remain as *null*.

See the image below to understand more easily:

![img](images/skewed-binary-tree-01.png)  

</details>






































































































<!--- ( Types of Trees/Binary Tree based on completion of levels ) --->

---

<div id="intro-to-complete-binary-tree"></div>

## `When is a tree considered a "Complete Binary Tree"?`

<details>

<summary>ANSWER</summary>

<br/>

>  A **Binary Tree** is a **Complete Binary Tree** if all the levels are completely filled except possibly the last level and the last level has all keys as left as possible.

A **Complete Binary Tree** is just like a **Full Binary Tree**, but with two major differences:

 - Every level except the last level must be completely filled.
 - All the leaf elements must lean towards the left.
 - The last leaf element might not have a right sibling i.e. a complete binary tree doesn’t have to be a full binary tree.

For example, see the image below to understand more easily:

![img](images/complete-binary-tree-01.png)  

</details>










---

<div id="intro-to-perfect-binary-tree"></div>

## `When is a tree considered a "Perfect Binary Tree"?`

<details>

<summary>ANSWER</summary>

<br/>

A **Binary tree** is a **Perfect Binary Tree** when:

 - All the internal nodes have two children.
 - And all leaf nodes are at the same level. 

For example, see the image below to understand more easily:

![img](images/perfect-binary-tree-01.png)  

</details>










---

<div id="intro-to-balanced-binary-tree"></div>

## `When is a tree considered a "Balanced Binary Tree (Also known as Height Balanced Tree)"?`

<details>

<summary>ANSWER</summary>

<br/>

To understand what's a **Balanced Binary Tree (Also known as Height Balanced Tree)**, let's get started by seeing a **Degenerate Binary Tree**:

![img](images/degenerate-binary-tree-02.png)  

See that:

 - This Degenerate Binary Tree is similar to:
   - Linked-List
   - Linked-List Queue
   - Linked-List Stack
   - Vector

See also our **Degenerate Binary Tree** is a **Binary Search Tree (That is, follow the BST properties)**. For example, imagine we need to search the key 500:

![img](images/degenerate-binary-tree-03.png)  

If you pay attention:

 - To discover that the key 500 is not in the tree, we need to traverse the tree node by node like a Linked List traversing.
 - That is, all operations insertion, removing, and searching are **O(n) (or O(h) where "h" is the tree height)**:
   - This can be slow for tasks we need to repeat many times. E.g. *search*.

> This type of Tree is known as **Unbalanced Binary Tree**.

### Ok, but what's a Balanced Binary Tree?

A Tree is *balanced* if the **"balance factor of each node"** is between *-1* to *1*, otherwise (caso contrário), the Tree will be *unbalanced* and needs to be *balanced*.

> Ok, but what's a **"balance factor of a node"**?

For example, let's see a **formula of a "balance factor of a node"** of the **AVL Tree**:

![img](images/balanced-binary-tree-01.png)  

Where:

 - **Balance Factor(k):**
   - The *current node* **Balance Factor result**.
 - **height(left(k)):**
   - The number of edges from the *current Node* to the most distant *left leaf node (k)*.
 - **height(right(k)):**
   - The number of edges from the *current Node* to the most distant *right leaf node (k)*.

To understand more easily, see the **Binary Tree** below:

![img](images/balanced-binary-tree-02.png)  

 - If the **Balance Factor** is *1* or *-1*, then the node is **balanced**.
 - If the **Balance Factor** is *above 1 (e.g. 2, 3, 4, etc.)* or below -1 (e.g. -2, -3, -4, etc.), then the node is **unbalanced**.
 - **NOTE:** For the *Tree to be balanced*, the *Balance Factor* of each node must be between **-1** and **1**.

</details>






































































































<!--- ( Types of Trees/Special Types of Trees/Binary Search Tree (BST) ) --->

---

<div id="intro-to-binary-search-tree"></div>

## `Binary Search Tree (BST)`

> **What is a Binary Search Tree (BST) and how do you implement a class for it?**

<details>

<summary>ANSWER</summary>

<br/>

**Binary Search Tree** is a *node-based binary tree* data structure that has the following properties:

 - All nodes of the **left subtree** are `less than` the **root node**.
 - All nodes of **right subtree** are `more than` the **root node**.
 - Both subtrees of each node are also **Binary Search Tree**.
   - In other words, they have the above two properties

For example:

![img](images/bst-01.png)  

To implement the ***Binary Search Tree class*** let's get started by implementing the class *constructor*:

**Python:** [trees.py](src/python/trees.py)
```python
class Node:
    def __init__(self, key):
        self.leftChild = None
        self.rightChild = None
        self.key = key


class BinarySearchTree(Node):
    def __init__(self):
        self.root = None
        self.size = 0
```

</details>






































































































<!--- ( Tree Traversal Techniques ) --->

---

<div id="ttt"></div>

## Tree Traversal Techniques

> **What are the "Tree Traversal "Techniques?**

<details>

<summary>ANSWER</summary>

<br/>

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

</details>










---

<div id="depth-first-search"></div>

## Depth First Search (DFS)

> **What is Depth First Search (DFS)?**

<details>

<summary>ANSWER</summary>

<br/>

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

</details>










---

<div id="preorder-traversal"></div>

## Preorder Traversal

> **What is *"Preorder Traversal"* technique?**

<details>

<summary>ANSWER</summary>

<br/>

> This technique follows the **'CURRENT->LEFT->RIGHT'** policy.

 - It means that, *first root (current) node* is visited.
 - After that, the *left subtree* is traversed recursively.
 - Finally, *right subtree* is recursively traversed.

To understand more easily, imagine we have the following *Tree*:

![img](images/tree-example-01.png)  

**NOTE:**  
If you pay attention you can see that the *Tree* has another subtrees:

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

</details>

---

<div id="preorder-implementation"></div>

## `How do I implement a preorder traversal function?`

<details>

<summary>Python</summary>

<br/>

Before creating functions to *traverse* a *Tree* first, let's create the useful method **traverse()**:

**Python:** [trees.py](src/python/trees.py)
```python
def traverse(self, approach="inorder"):
    if self.isEmpty():
        print("Tree is empty.")
        return
    else:
        result = []
        if approach == "preorder":
            self._preorder_recursive(self.root, result)
            return result
        elif approach == "inorder":
            self._inorder_recursive(self.root, result)
            return result
        elif approach == "postorder":
            self._postorder_recursive(self.root, result)
            return result
        else:
            print(
                "Invalid approach. Please use 'preorder', 'inorder', or 'postorder'."
            )
            return
```

 - **Time and Space Complexity:**
   - Here, the focus is method goals, not Complexities.
 - **Code Explanation:**
   - First, the method check if the *Tree* is empty.
   - Next, if the list is not empty (else block) we create an empty list `"result = []"`:
     - It is interesting to create the list before selecting the approach to avoid repeating the same code.
   - Next, we need to select the method *(preorder, inorder, or postorder)* to be used.
   - The selected method will append() the Node values following your approach.
   - Finally, we return the "result" variable (list).

### Recurvive Approach

Now, let's see how to implement the **preorder** method using **Recursive approach** to do this:

[trees.py](src/python/trees.py)
```python
def _preorder_recursive(self, current_node, result):
    if current_node:                                               # O(1)
        result.append(current_node.key)                            # O(1)
        self._preorder_recursive(current_node.leftChild, result)   # O(n)
        self._preorder_recursive(current_node.rightChild, result)  # O(n)
```

$f(n) = O(1) + O(1) + O(n) + O(n)$

#### Complexity Explanation

 - **Time Complexity: O(n)**
   - The *Time Complexity* of this function is **O(n)**, where **"n"** is the number of nodes in the tree. This is because the function visits each node exactly once.
 - **Space Complexity: O(n)**
   - The *Space Complexity* of this function is **O(n)**, where **"n"** is the number of nodes in the tree. This is because the function uses recursion, and each recursive call adds a new frame to the call stack. In the worst case, the call stack can have a depth of **"n"**, resulting in **O(n)** *Space complexity*.

#### Code Explanation

 - `if current_node:`
   - Checks if *current_node* is not *None* (empty). If it's not empty, it means there's a node to process.
 - If the current_node is not empty (None) we follow the preorder policy: **'CURRENT->LEFT->RIGHT'**:
   - `result.append(current_node.key)`
     - Appends the key of the *current_node* to the *"result"* list, storing it in the preorder sequence.
   - `self._preorder_recursive(current_node.leftChild, result)`
     - Recursively calls `_preorder_recursive` on the *leftChild* of the *current_node*, traversing the *left subtree* first.
   - `self._preorder_recursive(current_node.rightChild, result)`
     - Recursively calls `_preorder_recursive` on the *rightChild* of the *current_node*, traversing the *right subtree* after the left subtree.

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

    preorder_result = bst.traverse(approach="preorder")
    print(f"Preorder: {preorder_result}")
```

**OUTPUT:**
```bash
Preorder: [25, 20, 10, 5, 1, 8, 12, 15, 22, 36, 30, 28, 30, 36, 36, 40, 48, 50]
```

</details>










---

<div id="inorder-traversal"></div>

## Inorder Traversal

> **What is *"Inorder Traversal"* technique?**

<details>

<summary>ANSWER</summary>

<br/>

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

</details>

---

<div id="inorder-implementation"></div>

## `How do I implement a inorder traversal function?`

<details>

<summary>Python</summary>

<br/>

Before creating methods to *traverse* a *Tree* first, let's create the useful method **traverse()**:

**Python:** [trees.py](src/python/trees.py)
```python
def traverse(self, approach="inorder"):
    if self.isEmpty():
        print("Tree is empty.")
        return
    else:
        result = []
        if approach == "preorder":
            self._preorder_recursive(self.root, result)
            return result
        elif approach == "inorder":
            self._inorder_recursive(self.root, result)
            return result
        elif approach == "postorder":
            self._postorder_recursive(self.root, result)
            return result
        else:
            print(
                "Invalid approach. Please use 'preorder', 'inorder', or 'postorder'."
            )
            return
```

 - **Time and Space Complexity:**
   - Here, the focus is method goals, not Complexities.
 - **Code Explanation:**
   - First, the method check if the *Tree* is empty.
   - Next, if the list is not empty (else block) we create an empty list `"result = []"`:
     - It is interesting to create the list before selecting the approach to avoid repeating the same code.
   - Next, we need to select the method *(preorder, inorder, or postorder)* to be used.
   - The selected method will append() the Node values following your approach.
   - Finally, we return the "result" variable (list).

### Recurvive Approach

Now, let's see how to implement the **inorder** method using **Recursive approach** to do this:

[trees.py](src/python/trees.py)
```python
def _inorder_recursive(self, current_node, result):
    if current_node:                                              # O(1)
        self._inorder_recursive(current_node.leftChild, result)   # O(n)
        result.append(current_node.key)                           # O(1)
        self._inorder_recursive(current_node.rightChild, result)  # O(n)
```

$f(n) = O(1) + O(n) + O(1) + O(n)$

#### Complexity Explanation

 - **Time Complexity: O(n)**
   - The *Time Complexity* of this function is **O(n)**, where **"n"** is the number of nodes in the tree. This is because the function visits each node exactly once in an inorder traversal.
 - **Space Complexity: O(n)**
   - The *Space Complexity* of this function is **O(n)**, where **"n"** is the number of nodes in the tree. This is because the function uses recursion, and each recursive call adds a new frame to the call stack. In the worst case, the call stack can have a depth of **"n"**, resulting in **O(n)** space complexity.

#### Code Explanation

 - `if current_node:`
   - Checks if *current_node* is not *None* (empty). If it's not empty, it means there's a node to process.
 - If the current_node is not empty (None) we follow the inorder policy: **'LEFT->CURRENT->RIGHT'**:
   - `self._inorder_recursive(current_node.leftChild, result)`
     - Recursively calls `_inorder_recursive` on the *leftChild* of the *current_node*, traversing the left subtree first. This ensures the *inorder* traversal pattern.
   - `result.append(current_node.key)`
     - Appends the key of the *current_node* to the result list, storing it in the *inorder* sequence.
   - `self._inorder_recursive(current_node.rightChild, result)`
     - Recursively calls `_inorder_recursive` on the *rightChild* of the *current_node*, traversing the right subtree after the left subtree and the current node, following the *inorder* pattern.

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

    inorder_result = bst.traverse()  # Default approach is "inorder".
    print(f"Inorder: {inorder_result}")
```

**OUTPUT:**
```bash
Inorder: [1, 5, 8, 10, 12, 15, 20, 22, 25, 28, 30, 30, 36, 36, 36, 40, 48, 50]
```

</details>










---

<div id="postorder-traversal"></div>

## Postorder Traversal

> **What is *"Postorder Traversal"* technique?**

<details>

<summary>ANSWER</summary>

<br/>

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

</details>

---

<div id="postorder-implementation"></div>

## `How do I implement a postorder traversal function?`

<details>

<summary>Python</summary>

<br/>

Before creating methods to *traverse* a *Tree* first, let's create the useful method **traverse()**:

**Python:** [trees.py](src/python/trees.py)
```python
def traverse(self, approach="inorder"):
    if self.isEmpty():
        print("Tree is empty.")
        return
    else:
        result = []
        if approach == "preorder":
            self._preorder_recursive(self.root, result)
            return result
        elif approach == "inorder":
            self._inorder_recursive(self.root, result)
            return result
        elif approach == "postorder":
            self._postorder_recursive(self.root, result)
            return result
        else:
            print(
                "Invalid approach. Please use 'preorder', 'inorder', or 'postorder'."
            )
            return
```

 - **Time and Space Complexity:**
   - Here, the focus is method goals, not Complexities.
 - **Code Explanation:**
   - First, the method check if the *Tree* is empty.
   - Next, if the list is not empty (else block) we create an empty list `"result = []"`:
     - It is interesting to create the list before selecting the approach to avoid repeating the same code.
   - Next, we need to select the method *(preorder, inorder, or postorder)* to be used.
   - The selected method will append() the Node values following your approach.
   - Finally, we return the "result" variable (list).

### Recurvive Approach

Now, let's see how to implement the **postorder** method using **Recursive approach** to do this:

[trees.py](src/python/trees.py)
```python
def _postorder_recursive(self, current_node, result):
    if current_node:                                                # O(1)
        self._postorder_recursive(current_node.leftChild, result)   # O(n)
        self._postorder_recursive(current_node.rightChild, result)  # O(n)
        result.append(current_node.key)                             # O(1)
```

$f(n) = O(1) + O(n) + O(n) + O(1)$

#### Complexity Explanation

 - **Time Complexity: O(n)**
   - The *Time Complexity* of this function is **O(n)**, where **"n"** is the number of nodes in the tree. This is because the function visits each node exactly once in a *postorder* traversal.
 - **Space Complexity: O(n)**
   - The *Space Complexity* of this function is **O(n)**, where **"n"** is the number of nodes in the tree. This is because the function uses recursion to traverse the tree, and each recursive call adds a new frame to the call stack. In the worst case, the call stack can have a depth of **"n"**, resulting in **O(n)** *Space Complexity*.

#### Code Explanation

 - `if current_node:`
   - Checks if *current_node* is not *None* (empty). If it's not empty, it means there's a node to process.
 - If the current_node is not empty (None) we follow the postorder policy: **'LEFT->RIGHT->CURRENT'**:
   - `self._postorder_recursive(current_node.leftChild, result)`
     - Recursively calls `_postorder_recursive` on the *leftChild* of the *current_node*, traversing the left subtree first, following the *postorder* pattern.
   - `self._postorder_recursive(current_node.rightChild, result)`
     - Recursively calls `_postorder_recursive` on the *rightChild* of the *current_node*, traversing the right subtree before the current node, adhering to the *postorder* pattern.
   - `result.append(current_node.key)`
     - Appends the key of the current_node to the result list, storing it in the postorder sequence, after both subtrees have been processed.

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

    postorder_result = bst.traverse(approach="postorder")
    print(f"Postorder: {postorder_result}")
```

**OUTPUT:**
```bash
Postorder: [1, 8, 5, 15, 12, 10, 22, 20, 30, 28, 36, 36, 30, 50, 48, 40, 36, 25]
```

</details>







































































































<!--- ( REFERENCES ) --->

---

<div id="ref"></div>

## REFERENCES

 - [AVL Tree](https://www.javatpoint.com/avl-tree)
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
 - [Difference Between Tree Depth and Height](https://www.baeldung.com/cs/tree-depth-height-difference)

---

Ro**drigo** **L**eite da **S**ilva - **drigols**

<details>

<summary></summary>

<br/>

ANSWER

```bash

```

![img](images/)  

</details>
