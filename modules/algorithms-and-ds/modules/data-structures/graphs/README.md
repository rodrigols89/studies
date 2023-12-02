# Graphs

## Contents

 - **Basics:**
   - [Intro to Graphs (Vertex/Node, Edge, Weight, Adjacency, Path, Cycle)](#intro-to-graphs)
 - **Representation of Graphs:**
   - **[Undirected Graphs (Symmetry or Bidirectional)](#undirected-graphs)**
     - [Adjacency Matrix for Undirected Graphs](#adjacency-matrix-for-undirected-graphs)
     - [Adjacency List for Undirected Graphs](#adjacency-list-for-undirected-graphs)
   - **[Directed Graphs (Asymmetry or Unidirectional)](#directed-graphs)**
 - **Tips & Tricks:**
   - [Add and Remove problem (Index out of range)](#add-remove-problem-01)
   - [Add and Remove problem (Add the same edge twice)](#add-remove-problem-02)
 - [REFERENCES](#ref)








































<!--- ( Basics ) --->

---

<div id="intro-to-graphs"></div>

## Intro to Graphs (Vertex/Node, Edge, Weight, Adjacency, Path, Cycle)

> A ***Graph*** is a *non-linear* data structure consisting of **vertices (nodes)** and **edges**.

 - The vertices are sometimes also referred to as nodes.
 - The edges are lines or arcs that connect any two vertices (nodes) in the graph.

**NOTE:**  
More formally a Graph is composed of **"a set of vertices (V)"** and **"a set of edges (E)"**. The graph is denoted by **"G(V, E)"**.

For example:

```bash
V = {0, 1, 2, 3}  # Set of vertices.
E = {(0, 1), (0, 2), (0, 3), (1, 2)}  # Set of edges.

G = {V, E}  # The Graph.
```

The **visual graph** to the above example is:

![img](images/graphs-01.png)  

Looking at the example above we have more two concepts of graphs: 

 - **Adjacency:**
   - A *vertex* is said to be `adjacent` to another *vertex* if there is an edge connecting them.
   - **NOTE:** Looking at our visual example Vertices 2 and 3 are not adjacent because there is no edge between them.
 - **Path:**
   - A sequence of edges that allows you to go from vertex A to vertex B is called a path.
   - **NOTE:** Looking at our visual example *0-1*, *1-2* and *0-2* are paths from *vertex 0* to *vertex 2*.

### Graphs with "weights"

 - *Edges* may be **weighted** to show that there is a cost to go from one vertex to another.
 - For example in a graph of roads that connect one city to another, the *weight* on the *edge* might represent the distance between the two cities.

For example, imagine we have a **"Graph = (V, E)"**, denoted by:

![img](images/graphs-02.png)  

> **NOTES:**  
> See that again we have a **"set of vertices"** and a **"set of edges"**. However, `"our edges have weights"`.

See the graph for our example below:

![img](images/graphs-03.png)  

 - **Cycle:**
   - A *Cycle* in a graph is a path that starts and ends at the same vertex:
     - For example, in our example above the path **(V5, V2, V3, V5)** is a cycle.
   - **NOTE:** A graph with no cycles is called an **"Acyclic Graph"**.
   - **NOTE:** A *Directed Graph* with no cycles is called a *Directed Acyclic Graph* or a *DAG*:
     - We will see that we can solve several important problems if the problem can be represented as a DAG.








































<!--- ( Representation of Graphs/Undirected Graphs ) --->

---

<div id="undirected-graphs"></div>

## Undirected Graphs (Symmetry or Bidirectional)

An ***Undirected Graph*** is a *graph* where the *edges* do not have a specific direction and it is `bidirectional` in nature it does not have a parent-child relation concept as there is no particular direction.

For example:

![img](images/graphs-01.png)  

### Undirected Graph is Symmetry

 - *Symmetry* is present in the undirected graph as each edge is `bidirectional`, so it’s not like anyone’s the boss.
 - The graph is connected, so you can always find a way to get to any node you want to, and the degree of each vertex tells you how popular that node is in the graph.

### Algorithms for Undirected Graphs

 - **Depth-First Search (DFS).**
 - **Breadth-First Search (BFS).**

---

<div id="adjacency-matrix-for-undirected-graphs"></div>

## Adjacency Matrix for Undirected Graphs

An ***Adjacency Matrix*** is one of the most popular ways to represent a graph because it's the easiest one to understand and implement and works reasonably well for many applications.

 - It uses an **"nxn matrix"** to represent a graph *(where "n" is the number of vertices in the graph)*.
   - In other words, the number of rows and columns is equal to the number of vertices in the graph.

To understand more easily, see the **Undirected Graph** and your **Adjacency Matrix** example below:

![img](images/ad-mat-01.png)  

Now, let's see how to implement an **Adjacency Matrix** starting with the *constructor*:

[graphs.py](src/python/graphs.py)
```python
class AdjacencyMatrix:
    def __init__(self, num_of_vertices):
        self.num_of_vertices = num_of_vertices
        self.adj_matrix = [
            [0 for column in range(num_of_vertices)] for row in range(num_of_vertices)
        ]
```

Looking at the class *constructor* above we can see that:

 - **We have "num_of_vertices" instance variable:**
   - That's, the number of vertices on the Graph.
 - **Next, we create a matrix of size equal to the number of vertices passed to the constructor:**
   - `[0 for column in range(num_of_vertices)]`
     - If you pay attention, here we have a list `"[]"` and the list comprehension to fills the list `"0 for column in range(num_of_nodes)"`
       - `g1 = AdjacencyMatrix(1) = [[0]]`
       - `g1 = AdjacencyMatrix(2) = [[0, 0]]`
       - `g1 = AdjacencyMatrix(3) = [[0, 0, 0]]`
       - `g1 = AdjacencyMatrix(4) = [[0, 0, 0, 0]]`
       - `g1 = AdjacencyMatrix(5) = [[0, 0, 0, 0, 0]]`
       - **NOTE:** The focus here is to fill the list *(columns of the matrix)* with zeros.
   - `for row in range(num_of_vertices)`
     - Here the focus is to add the number of lists (rows) to the matrix:
       - `g1 = AdjacencyMatrix(1) = [[0]]`
       - `g1 = AdjacencyMatrix(2) = [[0, 0], [0, 0]]`
       - `g1 = AdjacencyMatrix(3) = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]`


**NOTE:**  
To understand more easily this part `"for row in range(num_of_vertices)"`, see the example below:

```python
g1 = AdjacencyMatrix(3) = [
  [0, 0, 0],
  [0, 0, 0],
  [0, 0, 0]
]
```

Let's see how it works in practice:

```python
from graphs import AdjacencyMatrix

if __name__ == "__main__":

    g1 = AdjacencyMatrix(1)
    print(g1.adj_matrix)

    g2 = AdjacencyMatrix(2)
    print(g2.adj_matrix)

    g3 = AdjacencyMatrix(3)
    print(g3.adj_matrix)

    g4 = AdjacencyMatrix(4)
    print(g4.adj_matrix)

    g5 = AdjacencyMatrix(5)
    print(g5.adj_matrix)
```

**OUTPUT:**
```bash
[[0]]
[[0, 0], [0, 0]]
[[0, 0, 0], [0, 0, 0], [0, 0, 0]]
[[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
[[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
```

Now, let's implement the useful method `"__len__()"` to check the size of the *Adjacency Matrix* (that's, how many vertices are there in the Graph):

[graphs.py](src/python/graphs.py)
```python
def __len__(self):
    return self.num_of_vertices
```

Another useful method is a method to print (show) the **Adjacency Matrix**:

[graphs.py](src/python/graphs.py)
```python
def print_adjacency_matrix(self):
    for row in self.adj_matrix:
        print(row)
```

Let's see how it works in practice:

```python
from graphs import AdjacencyMatrix

if __name__ == "__main__":

    graph = AdjacencyMatrix(4)
    graph.print_adjacency_matrix()
```

**OUTPUT:**
```bash
[0, 0, 0, 0]
[0, 0, 0, 0]
[0, 0, 0, 0]
[0, 0, 0, 0]
```

Ok, now let's see how to add an edge between two vertices (source->destination) on the **Adjacency Matrix** to an **Undirected Graph:**

[graphs.py](src/python/graphs.py)
```python
def add_edge(self, source, destination):
    self.adj_matrix[source][destination] = 1
    self.adj_matrix[destination][source] = 1
```

See how easy it was:

 - **source:**
   - The *"source"* is the exit *point (vertex)*.
   - The *"row"* in the *Adjacency Matrix* represents the *point (vertex)* of departure (saída).
 - **destination:**
   - The *"destination"* is the *point (vertex)* of arrival (chegada).
   - The *"column"* in the *Adjacency Matrix* represents the *point (vertex)* of arrival (chegada).
 - **In an "Undirected Graph", an edge between two vertices is "bidirectional":**
   - Meaning it can be traversed in both directions. Therefore, when adding an edge between vertices *"source"* and *"destination"*, you need to reflect this connection in both directions in the adjacency matrix:
     - This is because some problems need symmetric representations.
     - `"self.adj_matrix[source][destination] = 1"`
     - `"self.adj_matrix[destination][source] = 1"`

Let's see how it works in practice:

```python
from graphs import AdjacencyMatrix

if __name__ == "__main__":

    graph = AdjacencyMatrix(4)

    graph.add_edge(0, 1)
    graph.add_edge(0, 3)
    graph.add_edge(2, 1)
    graph.add_edge(2, 3)

    graph.print_adjacency_matrix()
```

**OUTPUT:**
```bash
[0, 1, 0, 1]
[1, 0, 1, 0]
[0, 1, 0, 1]
[1, 0, 1, 0]
```

![img](images/ad-mat-01.png)  

We can also design an **Adjacency Matrix** to represent the *weight of the Graph*. For example:

![img](images/ad-mat-02.png)  

Now, let's implement a method to insert an Edge on the **Adjacency Matrix** based on *weights*:

[graphs.py](src/python/graphs.py)
```python
def add_edge_based_weight(self, source, destination, weight):
    self.adj_matrix[source][destination] = weight
    self.adj_matrix[destination][source] = weight
```

> **NOTE:**  
> See that like the old approach, we also use the **"source"** and **"destination"** to locate the `intersection` on the Matrix between the two vertices. However, here we assign the **"weight"** on the Matrix, not one (1).


Let's see how it works in practice:

```python
from graphs import AdjacencyMatrix

if __name__ == "__main__":

    graph = AdjacencyMatrix(5)

    graph.add_edge_based_weight(0, 1, 2)
    graph.add_edge_based_weight(0, 2, 3)

    graph.add_edge_based_weight(1, 2, 15)
    graph.add_edge_based_weight(1, 3, 2)

    graph.add_edge_based_weight(3, 4, 9)

    graph.add_edge_based_weight(4, 2, 13)

    graph.print_adjacency_matrix()
```

**OUTPUT:**
```bash
[0, 2, 3, 0, 0]
[2, 0, 15, 2, 0]
[3, 15, 0, 0, 13]
[0, 2, 0, 0, 9]
[0, 0, 13, 9, 0]
```

![img](images/ad-mat-02.png)  

Finally, let's see how to *remove* an edge between two vertices (source->destination) on the **Adjacency Matrix** for an **Undirected Graph**:

[graphs.py](src/python/graphs.py)
```python
def remove_edge(self, source, destination):
    if self.adj_matrix[source][destination] == 0:
        print(f"No Edge from {source} to {destination}")
        return
    self.adj_matrix[source][destination] = 0
    self.adj_matrix[destination][source] = 0
```

See that:

 - **First we need to check if the Edge exists or not:**
   - `if self.adjMatrix[source][destination] == 0:`
   - If not exists we stop the function.
 - **If the Edge exists, we need to remove it:**
   - `self.adjMatrix[source][destination] = 0`
   - `self.adjMatrix[destination][source] = 0`
   - **In an "Undirected Graph", an edge between two vertices is "bidirectional":**
     - Meaning it can be traversed in both directions. Therefore, when removing an edge between vertices *"source"* and *"destination"*, you need to reflect this connection in both directions in the adjacency matrix:
       - This is because some problems need symmetric representations.

Let's see how it works in practice:

```python
from graphs import AdjacencyMatrix

if __name__ == "__main__":

    graph = AdjacencyMatrix(4)

    graph.add_edge(0, 1)
    graph.add_edge(0, 3)
    graph.add_edge(2, 1)
    graph.add_edge(2, 3)
    graph.print_adjacency_matrix()

    print("")
    graph.remove_edge(1, 3)
    graph.remove_edge(0, 1)
    graph.print_adjacency_matrix()
```

**OUTPUT:**
```bash
[0, 1, 0, 1]
[1, 0, 1, 0]
[0, 1, 0, 1]
[1, 0, 1, 0]

No Edge from 1 to 3
[0, 0, 0, 1]
[0, 0, 1, 0]
[0, 1, 0, 1]
[1, 0, 1, 0]
```

---

<div id="adjacency-list-for-undirected-graphs"></div>

## Adjacency List for Undirected Graphs

> An **Adjacency List** represents a graph as **an array (or list) of Linked Lists**. This approach is the most efficient way to store a graph.

 - It allows you to store only edges that are present in a graph:
   - Which is the opposite of an *Adjacency Matrix*, which explicitly stores all possible edges (both existent and non-existent).

For example, see an **Undirected Graphs** and your **Adjacency List** below:

![img](images/ad-list-01.png)  

Now, let's see how to implement an **Adjacency List** starting by implementing the **Node class**:

[graphs.py](src/python/graphs.py)
```python
class AdjacencyList(AdjNode):
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.edges_list = [None] * self.num_vertices
```

See that:

 - We have **"a specially designed Node"** class **"to represent each edge of the Graph"**:
   - **NOTE:** That is, each Node instance represents an "edge" between two vertices (or a loop for the same vertex) and your *weight*.
   - **destination:**
     - The *"destination"* instance variable is the *Vertex* that is connected to the current (source) Vertex.
     - That's, the *Vertex* we point to go (current->destination).
   - **next:**
     - Finally, we have the "next" instance variable that is used to point (reference) the next edge (Node).

Ok, now let's see how to implement the **Adjacency List** class *constructor*:

[graphs.py](src/python/graphs.py)
```python
class AdjacencyList(AdjNode):
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.edges_list = [None] * self.num_vertices
```

See that:

 - The class **AdjacencyList** *inherits* from the **AdjNode** class.
 - The constructor receives the number of vertices as instance variable.
 - Next, we create a list of size equal to the number of vertices passed to the constructor:
   - That's, we have a fixed number of vertices in the Graph.

Let's see how it works in practice:

```python
from graphs import AdjacencyList

if __name__ == "__main__":

    g1 = AdjacencyList(5)
    print(g1.edges_list)

    g2 = AdjacencyList(10)
    print(g2.edges_list)
```

**OUTPUT:**
```bash
[None, None, None, None, None]
[None, None, None, None, None, None, None, None, None, None]
```

> **NOTE:**  
> See that we have a list of "None" to store the edges of the Graph.

Knowing that:

 - We have an **AdjNode** class to **represent each edge of the Graph**:
   - Saving your *"destination"* and *"next->AdjNode"*.
 - We have an **AdjacencyList** class that contains a `list (self.edges_list)` to store the edges of the Graph.

> **Now, how to add the edges (AdjNode instances) to the Graph (AdjacencyList)?**

To do this let's implement the **add_edge()** method on the **AdjacencyList class**:

[graphs.py](src/python/graphs.py)
```python
def add_edge(self, source, destination):
    new_node = AdjNode(destination)
    new_node.next = self.edges_list[source]
    self.edges_list[source] = new_node

    new_node = AdjNode(source)
    new_node.next = self.edges_list[destination]
    self.edges_list[destination] = new_node
```

Here, let's explain statement by statement:

**STETAMENT-01:**  
```python
node = AdjNode(destination)

      +---+
      | 2 | --> NULL
      +---+
       / \
        |
    Destination
```

The code above just makes a Node that saves the destination vertex.

**STETAMENT-02:**  
```python
# Driver code example 01.
graph = AdjacencyList(4)
print(graph.edges_list)

graph.add_edge(1, 2)

# Add_edge() method.
node.next = self.edges_list[source]

                      0     1     2     3
     self.edges_list[None, None, None, None]
                           / \
      +---+                 |
      | 2 |------(next)-----|
      +---+
       / \
        |
    Destination
```

 - Looking at the example above we can see that the code `"node.next = self.edges_list[source]"` sets the "next" of the new_node to the space reserved for the source of the vertex in the list.
 - **NOTE:** As each edge has a reserved space in the list, our “next” always points to that space in the list.

**STETAMENT-03:**  
```python
# Driver code example 01.
graph = AdjacencyList(4)
print(graph.edges_list)

graph.add_edge(1, 2)

# Add_edge() method.
self.edges_list[source] = new_node

                 0     1     2     3
                      +---+ 
self.edges_list[None, | 2 |, None, None]
                      +---+
```

> **NOTE:**  
> - As each edge has a reserved space in the list, our "new_node" always is added at the end of this space.
> - **NOTE:** Knowing this, if we pay attention we can see that the order in which we add new edges changes the result when printing (showing) the edges.

Finally, how an Undirected Graph is bidirectional we need to do the same process in the reverse order:

**LAST STETAMENTS (REVERSE ORDER):** 
```python
new_node = AdjNode(source)
new_node.next = self.edges_list[destination]
self.edges_list[destination] = new_node
```

> **Ok, but how can I see the AdjacencyList?**

To do this let's implement the **print_adjacency_list()** method on the **AdjacencyList class**:

[graphs.py](src/python/graphs.py)
```python
def print_adjacency_list(self):
    for list_index in range(self.num_vertices):
        current = self.edges_list[list_index]
        print(f"Adjacency List for vertex {list_index}: ", end="")
        while current:
            print(f"{current.destination} -> ", end="")
            current = current.next
        print("None")
```

See that:

 - **We use the control instance variable "self.num_vertices" to iterate through the list of vertices:**
   - The *range()* function is used to transforme the number to indexing (0 to n).
 - **Internally we pass the list "self.edges_list[i]" to "current" variable:**
   - This is important to not modify the original list.
   - And iterate through the list by *"list_index"*.
 - **More internally, we use the "current" variable to iterate through the list of edges (nodes):**
   - The *while* loop is used to iterate through the list of edges (nodes).
   - We jump to the next edge (node) by *"current = current.next"*.

Let's see how it works in practice:

[graphs.py](src/python/graphs.py)
```python
from graphs import AdjacencyList

if __name__ == "__main__":

    graph = AdjacencyList(5)

    graph.add_edge(4, 4)

    graph.add_edge(3, 1)

    graph.add_edge(2, 3)

    graph.add_edge(4, 2)

    graph.add_edge(0, 4)
    graph.add_edge(0, 3)
    graph.add_edge(0, 2)
    graph.add_edge(0, 1)

    graph.print_adjacency_list()
```

**OUTPUT:**
```bash
Adjacency List for vertex 0: 1 -> 2 -> 3 -> 4 -> None
Adjacency List for vertex 1: 0 -> 3 -> None
Adjacency List for vertex 2: 0 -> 4 -> 3 -> None
Adjacency List for vertex 3: 0 -> 2 -> 1 -> None
Adjacency List for vertex 4: 0 -> 2 -> 4 -> 4 -> None
```

![img](images/ad-list-01.png)  

> **What?**  
> Why the result is different from the image?

**NOTE:**  
This is because the order we add the edges changes the result when printing (showing) the edges.

For example, let's change the order we add the edges to see the result:

```python
from graphs import AdjacencyList

if __name__ == "__main__":

    graph = AdjacencyList(5)

    graph.add_edge(3, 4)

    graph.add_edge(2, 4)
    graph.add_edge(2, 3)

    graph.add_edge(3, 1)

    graph.add_edge(0, 4)
    graph.add_edge(0, 3)
    graph.add_edge(0, 2)
    graph.add_edge(0, 1)

    graph.print_adjacency_list()
```

**OUTPUT:**
```bash
Adjacency List for vertex 0: 1 -> 2 -> 3 -> 4 -> None
Adjacency List for vertex 1: 0 -> 3 -> None
Adjacency List for vertex 2: 0 -> 3 -> 4 -> None
Adjacency List for vertex 3: 0 -> 1 -> 2 -> 4 -> None
Adjacency List for vertex 4: 0 -> 2 -> 3 -> None
```

![img](images/ad-list-01.png)  








































<!--- ( Representation of Graphs/Directed Graphs ) --->

---

<div id="directed-graphs"></div>

## Directed Graphs (Asymmetry or Unidirectional)

A **Directed Graph** is a *graph* that is `unidirectional` in this the edges have a specific direction and the edges have directions specified with them also a directed graph can contain cycles.

For example:

![img](images/directed-graph-01.png)

### Directed Graphs is Asymmetry

*Asymmetry* is present in the Directed Graph as the edges are all one-way, so it’s not like everyone is on equal footing and the graph might not be connected, which means there might be some nodes that are totally out of the loop.

### Algorithms for Directed Graphs

 - **Topological Sort.**
 - **Dijkstra’s Algorithm.**








































<!--- ( Tips & Tricks ) --->

---

<div id="add-remove-problem-01"></div>

## Add and Remove problem (index out of range)

We always need to pay attention to not try to **"add/remove"** an edge out of the Matrix/List range (size).

For example:

```python
from graphs import AdjacencyMatrix

if __name__ == "__main__":

    graph = AdjacencyMatrix(4)

    graph.add_edge(0, 1)
    graph.add_edge(0, 3)
    graph.add_edge(2, 1)
    graph.add_edge(2, 3)

    graph.add_edge(4, 3)  # Out index (size).

    graph.print_adjacency_matrix()
```

**OUTPUT:**
```bash
Traceback (most recent call last):
  File ..................., line 23, in <module>
    graph.add_edge(3, 4)  # Out the range (size).
    ^^^^^^^^^^^^^^^^^^^^
  File ..................., line 22, in add_edge
    self.adjMatrix[source][destination] = 1
    ~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^
IndexError: list assignment index out of range
```

---

<div id="add-remove-problem-02"></div>

## Add edge problem (Add the same edge twice)

> When we add an edge we need to pay attention to not add the same edge twice.

For example:

```python
add_edge(1, 2)
add_edge(2, 1)
```

**NOTE:**  
In the example above, we add the same edge two times. Unless (a menos) they had two edges connecting the same vertices.

For example, see two edges connecting the same vertices:

![img](images/double-vertices.png)  

See that we have two edges connecting the vertices 3 and 4.

```python
add_edge(3, 4)
add_edge(4, 3)
```

> **NOTE:**  
> To solve this problem of adding an edge more than once, first we count how many edges there are in the Graph and then add them one by one.








































<!--- ( REFERENCES ) --->

---

<div id="ref"></div>

## REFERENCES

 - [Python Graphs (Using dictionaries)](https://www.tutorialspoint.com/python_data_structure/python_graphs.htm)
 - [Graph Data Stucture](https://www.programiz.com/dsa/graph)
 - [Introduction to Graphs – Data Structure and Algorithm Tutorials](https://www.geeksforgeeks.org/introduction-to-graphs-data-structure-and-algorithm-tutorials/)
 - [Types of Graphs with Examples](https://www.geeksforgeeks.org/graph-types-and-applications/)
 - [Adjacency Matrix](https://www.programiz.com/dsa/graph-adjacency-matrix)
 - [Adjacency List](https://www.programiz.com/dsa/graph-adjacency-list)
 - [Data Structures & Algorithms in Python](https://learning.oreilly.com/library/view/data-structures/9780134855912/)
 - [Problem Solving with Algorithms and Data Structures using Python](https://runestone.academy/ns/books/published/pythonds/index.html)
 - [What is Undirected Graph? | Undirected Graph meaning](https://www.geeksforgeeks.org/what-is-unidrected-graph-undirected-graph-meaning/)
 - [What is Directed Graph? | Directed Graph meaning](https://www.geeksforgeeks.org/what-is-directed-graph-directed-graph-meaning/)
 - [Kruskal’s Minimum Spanning Tree (MST) Algorithm](https://www.geeksforgeeks.org/kruskals-minimum-spanning-tree-algorithm-greedy-algo-2/)
 - [Prim’s Algorithm for Minimum Spanning Tree (MST)](https://www.geeksforgeeks.org/prims-minimum-spanning-tree-mst-greedy-algo-5/)
 - [How to find Shortest Paths from Source to all Vertices using Dijkstra’s Algorithm](https://www.geeksforgeeks.org/dijkstras-shortest-path-algorithm-greedy-algo-7/)
 - [Breadth First Search or BFS for a Graph](https://www.geeksforgeeks.org/breadth-first-search-or-bfs-for-a-graph/)
 - [Depth First Search or DFS for a Graph](https://www.geeksforgeeks.org/depth-first-search-or-dfs-for-a-graph/)
 - [Difference between BFS and DFS](https://www.geeksforgeeks.org/difference-between-bfs-and-dfs/)
 - [Add and Remove Edge in Adjacency List representation of a Graph](https://www.geeksforgeeks.org/add-and-remove-edge-in-adjacency-list-representation-of-a-graph/)
 - [Convert Adjacency Matrix to Adjacency List representation of Graph](https://www.geeksforgeeks.org/convert-adjacency-matrix-to-adjacency-list-representation-of-graph/)
 - [Convert Adjacency List to Adjacency Matrix representation of a Graph](https://www.geeksforgeeks.org/convert-adjacency-list-to-adjacency-matrix-representation-of-a-graph/)
 - [Graph as adjacency list – Graph implementation 1](https://www.lavivienpost.net/graph-implementation-as-adjacency-list/)
 - [Weighted graph as adjacency list – Graph implementation 2](https://www.lavivienpost.net/weighted-graph-as-adjacency-list/)
 - [Representation of Graphs: Adjacency Matrix and Adjacency List](https://www.thecrazyprogrammer.com/2014/03/representation-of-graphs-adjacency-matrix-and-adjacency-list.html)

---

Ro**drigo** **L**eite da **S**ilva - **drigols**
