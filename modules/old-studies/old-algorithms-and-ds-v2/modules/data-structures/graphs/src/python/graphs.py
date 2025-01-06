##########################################################################
# Rodrigo Leite da Silva - drigols                                       #
# Last update: 25/01/2024                                                #
##########################################################################


class AdjacencyMatrix:
    def __init__(self, n):
        self.n = n
        self.matrix = [[0 for _ in range(n)] for _ in range(n)]

    def print_adjacency_matrix(self):
        for row in self.matrix:
            print(row)

    def add_edge(self, source, destination):
        self.matrix[source][destination] = 1
        self.matrix[destination][source] = 1

    def add_edge_based_weight(self, source, destination, weight):
        self.matrix[source][destination] = weight
        self.matrix[destination][source] = weight

    def remove_edge(self, source, destination):
        if self.matrix[source][destination] == 0:
            print(f"No Edge from {source} to {destination}")
            return
        self.matrix[source][destination] = 0
        self.matrix[destination][source] = 0


class AdjNode:
    def __init__(self, vertex, next=None):
        self.vertex = vertex
        self.next = next


class AdjacencyList(AdjNode):
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.edges_list = [None] * self.num_vertices

    def add_vertex(self, source, destination):
        new_node = AdjNode(destination)
        new_node.next = self.edges_list[source]
        self.edges_list[source] = new_node

        new_node = AdjNode(source)
        new_node.next = self.edges_list[destination]
        self.edges_list[destination] = new_node

    def print_adjacency_list(self):
        for index_vertex in range(self.num_vertices):
            current = self.edges_list[index_vertex]
            print(f"Adjacency List for vertex {index_vertex}: ", end="")
            while current:
                print(f"{current.vertex} -> ", end="")
                current = current.next
            print("None")
