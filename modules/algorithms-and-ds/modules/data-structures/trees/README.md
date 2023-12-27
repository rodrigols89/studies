# Trees

## Contents

 - **Basics:**
   - [Tree Terminology](#tree-terminology)
   - [Tree Height & Depth](#tree-height-depth)
   - [Node class representation for a Binary Tree](#node-class-for-bt)
 - **Types of Trees:**
   - **Binary Tree based on the number of children:**
     - [Full Binary Tree](#intro-to-full-binary-tree)
     - [Degenerate (or pathological) Binary Tree](#intro-to-degenerate-binary-tree)
     - [Skewed Binary Tree](#intro-to-skewed-binary-tree)
   - **Binary Tree based on completion of levels:**
     - [Complete Binary Tree](#intro-to-complete-binary-tree)
     - [Perfect Binary Tree](#intro-to-perfect-binary-tree)
     - [Balanced Binary Tree (Also known as Height Balanced Tree)](#intro-to-balanced-binary-tree)
   - **Special Types of Trees:**
     - [Binary Search Tree](#intro-to-binary-search-tree)
       - [Useful methods len(), isEmpty() | O(1)](#bst-useful-methods)
       - [Inserting in a Binary Search Tree (Recursive Approach)](#insert-bst-recursive-approach)
       - [Inserting in a Binary Search Tree (Iterative Approach)](#insert-bst-iterative-approach)
     - AVL Tree
     - Red Black Tree
     - B Tree
     - B+ Tree
     - Segment Tree
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

---

<div id="tree-height-depth"></div>

## Tree Height & Depth

> To know the *Tree's Height* and *Depth*, **we need to focus on each Node** ➔ **not the entire tree**.

For each *node* in a tree, we can define two features:

 - **Height:**
   - A **"node height"** is the number of edges from the *current Node* to the most distant *leaf* node.
 - **Depth:**
   - A **"node depth"** is the number of edges from the *current node* to the *root*.

For example, see the image below to understand more easily:

![img](images/tree-height-depth.png)  

---

<div id="node-class-for-bt"></div>

## Node class representation for a Binary Tree

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




































































































<!--- ( Types of Trees/Binary Tree based on the number of children ) --->

---

<div id="intro-to-full-binary-tree"></div>

## Full Binary Tree

A **Binary Tree** is a **Full Binary Tree** if every node has **0** or **2 children**.

For example:

![img](images/full-binary-tree-01.png)

---

<div id="intro-to-degenerate-binary-tree"></div>

## Degenerate (or pathological) Binary Tree

A **Binary Tree** is a **Degenerate (or pathological) Binary Tree** when every internal node has **one child**.

![img](images/degenerate-binary-tree-01.png)  

> **NOTE:**  
> A degenerate or pathological tree is a tree having a single child either left or right.

---

<div id="intro-to-skewed-binary-tree"></div>

## Skewed Binary Tree

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




































































































<!--- ( Types of Trees/Binary Tree based on completion of levels ) --->

---

<div id="intro-to-complete-binary-tree"></div>

## Complete Binary Tree

>  A **Binary Tree** is a **Complete Binary Tree** if all the levels are completely filled except possibly the last level and the last level has all keys as left as possible.

A **Complete Binary Tree** is just like a **Full Binary Tree**, but with two major differences:

 - Every level except the last level must be completely filled.
 - All the leaf elements must lean towards the left.
 - The last leaf element might not have a right sibling i.e. a complete binary tree doesn’t have to be a full binary tree.

For example, see the image below to understand more easily:

![img](images/complete-binary-tree-01.png)

---

<div id="intro-to-perfect-binary-tree"></div>

## Perfect Binary Tree

A **Binary tree** is a **Perfect Binary Tree** when:

 - All the internal nodes have two children.
 - And all leaf nodes are at the same level. 

For example, see the image below to understand more easily:

![img](images/perfect-binary-tree-01.png)

---

<div id="intro-to-balanced-binary-tree"></div>

## Balanced Binary Tree (Also known as Height Balanced Tree)

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




































































































<!--- ( Types of Trees/BSpecial Types of Trees ) --->

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
        self.size = 0
```

---

<div id="bst-useful-methods"></div>

## Useful methods len(), isEmpty() | O(1)

Here, let's implement the useful methods **len()** and **isEmpty()**:

**Python:** [trees.py](src/python/trees.py)
```python
def isEmpty(self):
    return self.root is None  # O(1)

def __len__(self):
    return self.size  # O(1)
```

### Complexity Explanation

 - **Time Complexity: O(1)**
   - The *Time Complexity* of both methods is **O(1)** because they both have constant time complexity. This is because they both only involve simple operations such as checking if a variable is None or returning a variable, which can be done in constant time.
 - **Space Complexity: O(1)**
   - The *Space Complexity* of both methods is also **O(1)** because they do not use any additional space that grows with the input size. They only use a constant amount of space to store the variables.

Now, let's test in the practice:

**Python:**
```python
from trees import BinarySearchTree

if __name__ == '__main__':

    bst = BinarySearchTree()

    print(f"The Binary Search Tree is empty? {bst.isEmpty()}")
    print(f"Binary Search Tree size: {bst.__len__()}")
```

**OUTPUT:**
```bash
The Binary Search Tree is empty? True
Binary Search Tree size: 0
```

---

<div id="insert-bst-recursive-approach"></div>

## Inserting in a Binary Search Tree (Recursive Approach)

> A **new key** is always inserted at the *leaf (folha)* by maintaining the *property* of the Binary Search Tree.

![img](images/inserting-bst.gif)  

Before creating a method to insert a new Node using a *recursive approach*, first let's create the useful method **insert()**:

**Python:** [trees.py](src/python/trees.py)
```python
def insert(self, key, approach="recursive"):
    if self.isEmpty():
        self.root = Node(key)
        self.size += 1
    else:
        if approach == "recursive":
            self._insert_recursive(self.root, key)
        elif approach == "iterative":
            self._insert_iterative(self.root, key)
        else:
            print("Invalid approach. Please use 'recursive' or 'iterative'.")
        self.size += 1
```

 - **Time and Space Complexity:**
   - **NOTE:** For now, don't let's pay attention to Complexities. Just the method goals.
 - **Code Explanation:**
   - `if self.isEmpty():`
     - The focus here is to check if the Binary Search Tree is empty. If is empty, we just create a new Node and set it as the *"BST"* root.
     - Next, we increment the *"size"* of the BST by 1.
   - `The "else" block has some crucial parts:`
     - First, but not crucial is to choose the insertion approach *"recursive"* or *"iterative"*.
     - The really crucial part to pay attention is `"(self.root, key)"`:
       - See that both *"recursive"* or *"iterative"* approaches receive the same arguments.
       - Passing `"self.root"` as an argument is the most crucial part of this code because:
         - We always start from the root by passing Node by Node (recursively or iteratively).
         - That is, the *recursive* or *iterative* methods *do not need to worry about (não precisam se preocupar)* where to start to pass Node by Node because we've already given them the starting point (self.root).
         - **NOTE:** If we hadn't passed the root/head of the tree here, anyone calling this method would have to pass the starting point. E.g. `insert(root, data)`.
     - `self.size += 1`
       - As the "_insert_recursive" and "_insert_iterative" methods will iterate Node by Node in a *recursive* or loop way we cannot increment the number of Nodes in the Tree from them. It is interesting to increase this at the end of the else() block.

Now, let's see how to insert a new node (data/key) in the ***Binary Search Tree*** using a *recursive approach*

[trees.py](src/python/trees.py)
```python
def _insert_recursive(self, current_node, key):
    if key <= current_node.key:                                   # O(1)
        if current_node.leftChild is None:                        # O(1)
            current_node.leftChild = Node(key)                    # O(1)
        else:
            self._insert_recursive(current_node.leftChild, key)   # O(h)
    elif key >= current_node.key:                                 # O(1)
        if current_node.rightChild is None:                       # O(1)
            current_node.rightChild = Node(key)                   # O(1)
        else:
            self._insert_recursive(current_node.rightChild, key)  # O(h)
```

$f(n) = O(1) + O(1) + O(1) + O(h) + O(1) + O(1) + O(1) + O(h)$$

### Complexity Explanation

The time complexity of this recursive insertion function is O(log n) in the average case and O(n) in the worst case, where n is the number of nodes in the tree. This is because in a balanced binary search tree, the height of the tree is logarithmic in the number of nodes, so the function will make approximately log n recursive calls. However, in the worst case where the tree is completely unbalanced, the height of the tree is equal to the number of nodes, resulting in O(n) time complexity.

The space complexity of this function is O(log n) in the average case and O(n) in the worst case. This is because the function uses the call stack to store the recursive calls, and the maximum depth of the call stack is equal to the height of the tree. In a balanced binary search tree, the height is logarithmic in the number of nodes, so the space complexity is O(log n). However, in the worst case where the tree is completely unbalanced, the height is equal to the number of nodes, resulting in O(n) space complexity.















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

 - We have two methods `preorder()` and `_preorder_recursive()`:
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

 - We have two methods `inorder()` and `_inorder_recursive()`:
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

 - We have two methods `postorder()` and `_postorder_recursive()`:
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



     - [Tree Traversal Techniques:](#ttt)
       - [Depth First Search (DFS):](#depth-first-search)
         - [Preorder Traversal (current-left-right)](#preorder-traversal)
         - [Inorder Traversal (left-current-right)](#inorder-traversal)
         - [Postorder Traversal (left-right-current)](#postorder-traversal)
       - Breadth-First Search (BFS):
         - Level Order Traversal
