# Trees

## Contents

 - Basics:
   - [Tree Terminology](#tree-terminology)
 - [Binary Tree](#intro-to-binary-tree)
   - Special types of Binary Tree:
     - [Binary Search Tree](#intro-to-binary-search-tree)
       - Inserting:
         - [Inserting in a Binary Search Tree (Recursive Approach)](#insert-bst-recursive-approach)
   - Basic operations on Binary Tree:
     - Traversing:
       - Depth-First Search (DFS):
         - Preorder Traversal (current-left-right)
         - Inorder Traversal (left-current-right)
         - Postorder Traversal (left-right-current)
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
   - Classes Implementations:
     - [Node class for a Binary Tree](#node-for-binary-tree)
     - [Class for a Binary Search Tree](#binary-search-tree-class)
 - [REFERENCES](#ref)








































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

## Binary Tree

> A **Binary Tree** is a *tree* data structure in which each parent node can have at most two children.

Each node of a binary tree consists of three items:

 - Data *item (or key)*.
 - Address of *left child*.
 - Address of *right child*.

For example:

![img](images/binary-tree-00.png)  








































<!--- ( Binary Tree/Special types of Binary Tree/Binary Search Tree ) --->

---

<div id="intro-to-binary-search-tree"></div>

## Binary Search Tree

**Binary Search Tree** is a *node-based binary tree* data structure that has the following properties:

 - All nodes of the **left subtree** are `less than` the **root node**.
 - All nodes of **right subtree** are `more than` the **root node**.
 - Both subtrees of each node are also **Binary Search Tree**.
   - In other words, they have the above two properties

For example:

![img](images/bst-01.png)  

---

<div id="insert-bst-recursive-approach"></div>

## Inserting in a Binary Search Tree (Recursive Approach)

Here, let's see how to insert a new node (data/key) in the ***Binary Search Tree*** using a *recursive approach*:

[trees.py](src/python/trees.py)
```python
class BinarySearchTree(Node):

  ......


    def insert(self, key):
        if self.isEmpty():
            self.root = Node(key)
        else:
            self._insert(self.root, key)

    def _insert(self, current_node, key):
        if key < current_node.key:
            if current_node.leftChild is None:
                current_node.leftChild = Node(key)
            else:
                self._insert(current_node.leftChild, key)
        elif key > current_node.key:
            if current_node.rightChild is None:
                current_node.rightChild = Node(key)
            else:
                self._insert(current_node.rightChild, key)
```

See that:

 - We have two methods `"insert() public"` and `"_insert() private"`:
 - `insert():`
   - This method first checks if the *Binary Search Tree* is empty:
     - If the Tree is empty, it creates a new Node (value/key) as root.
   - If it's not empty, it calls the private method `"_insert()"`:
     - That's, we need to insert a new value (key) into the Tree with existing values.
 - `_insert() - This is the real method to insert a new value into the not empty Tree:`
   - This method receives the following arguments:
     - **current_node:** The first time, the "current_node" will be the "root" and loop Node by Node when necessary.
     - **key:** The "key" is the value to be inserted at the new Node.
   - Inside of the `_insert()` method the first thing to check is the side to move, left or right:
     - `"if key < current_node.key"`:
       - If the *"key"* `is less than` *"the key of the current_node"*, we move to the left subtree.
     - `"elif key > current_node.key"`:
       - If the *"key"* `is greater than` *"the key of the current_node"*, we move to the right subtree.
   - Next, we need to check if the *"current_node.left/right"* are empty (`"if current_node.leftChild is None" | "if current_node.rightChild is None"`):
     - If the *"current_node.left/right"* `is empty (None)`, then we must insert the new Node (value/key) here.
     - If the *"current_node.left/right"* `is not empty`, then we need to move recursively to the next Node (left or right):
       - `"self._insert(current_node.leftChild, key)"`
       - `"self._insert(current_node.rightChild, key)"`
       - **NOTE:** See that here we pass the *"current_node.left/right"* to the `_insert()` method, not the *root* Node.
       - **Base case (condiction to stop the recursion):**
         - The new Node (value/key) was created.
         - When the new Node (value/key) is created we don't call the `_insert()` method again recursively.

Now, let's test in the practice:

```python
from trees import BinarySearchTree

if __name__ == "__main__":

    bst = BinarySearchTree()

    #     (10) (root)
    #     / \
    #    /   \
    #   /     \
    # None     None
    bst.insert(10)
    print(bst.root.key)


    #          10 (root)
    #         / \
    #        /   \
    #       /     \
    #     (5)      None
    #     / \
    #    /   \
    #   /     \
    # None     None
    bst.insert(5)
    print(bst.root.leftChild.key)


    #            10 (root)
    #           / \
    #          /    \
    #         /      \
    #        /        \
    #       /          \
    #      5           (15)
    #     / \          / \
    #    /   \        /   \
    #   /     \      /     \
    # None     None None     None
    bst.insert(15)
    print(bst.root.rightChild.key)


    #               10 (root)
    #               / \
    #              /   \
    #             /     \
    #            /       \
    #           /         \
    #          5           15
    #         / \          / \
    #        /   \        /   \
    #       /     \      /     \
    #      (2)     None None     None
    #     / \
    #    /   \
    #   /     \
    # None     None
    bst.insert(2)
    print(bst.root.leftChild.leftChild.key)


    #               10 (root)
    #               / \
    #              /   \
    #             /     \
    #            /       \
    #           /         \
    #          5           15
    #         / \          / \
    #        /   \        /   \
    #       /     \      /     \
    #      2       None None   (17)    
    #     / \                   / \
    #    /   \                 /   \
    #   /     \               /     \
    # None     None         None     None
    bst.insert(17)
    print(bst.root.rightChild.rightChild.key)


    #               10 (root)
    #               / \
    #              /   \
    #             /     \
    #            /       \
    #           /         \
    #          5           15
    #         / \          / \
    #        /   \        /   \
    #       /     \      /     \
    #      2       None None    17    
    #     / \                   / \
    #    /   \                 /   \
    #   /     \               /     \
    # None     None         None     (18)
    #                                 / \
    #                                /   \
    #                              None   None
    bst.insert(18)
    print(bst.root.rightChild.rightChild.rightChild.key)
```

**OUTPUT:**
```bash
10
5
15
2
17
18
```








































<!--- ( Classes Implementations ) --->

---

<div id="node-for-binary-tree"></div>

## Node class for a Binary Tree

> A common approach to work with ***Binary Trees*** is to create a ***Node*** class to represent our nodes in the Tree.

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

---

<div id="binary-search-tree-class"></div>

## Class for a Binary Search Tree

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








































<!--- ( REFERENCES ) --->

---

<div id="ref"></div>

## REFERENCES

 - [Data Structures & Algorithms in Python](https://learning.oreilly.com/library/view/data-structures/9780134855912/)
 - [Introduction to Binary Tree – Data Structure and Algorithm Tutorials](https://www.geeksforgeeks.org/introduction-to-binary-tree-data-structure-and-algorithm-tutorials/)
 - [Types of Binary Tree](https://www.geeksforgeeks.org/types-of-binary-tree/)
 - [Applications, Advantages and Disadvantages of Binary Tree](https://www.geeksforgeeks.org/applications-advantages-and-disadvantages-of-binary-tree/)
 - [Applications, Advantages and Disadvantages of Binary Search Tree](https://www.geeksforgeeks.org/applications-advantages-and-disadvantages-of-binary-search-tree/)

---

Ro**drigo** **L**eite da **S**ilva - **drigols**

Now, let's test in the practice:

[trees.py](src/python/trees.py)
```python

```

**OUTPUT:**
```bash

```

