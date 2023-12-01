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

    graph.print_adj_list()


"""
Adjacency List for vertex 0: 1 -> 2 -> 3 -> 4 -> None
Adjacency List for vertex 1: 0 -> 3 -> None
Adjacency List for vertex 2: 0 -> 4 -> 3 -> None
Adjacency List for vertex 3: 0 -> 2 -> 1 -> 4 -> None
Adjacency List for vertex 4: 0 -> 2 -> 3 -> None
"""
