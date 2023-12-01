##########################################################################
# Rodrigo Leite da Silva - drigols                                       #
# Last update: 01/12/2023                                                #
##########################################################################


class AdjacencyMatrix:
    def __init__(self, num_of_vertices):
        self.num_of_vertices = num_of_vertices
        self.adj_matrix = [
            [0 for column in range(num_of_vertices)] for row in range(num_of_vertices)
        ]

    def __len__(self):
        return self.num_of_vertices

    def print_adjacency_matrix(self):
        for row in self.adj_matrix:
            print(row)

    def add_edge(self, source, destination):
        self.adj_matrix[source][destination] = 1
        self.adj_matrix[destination][source] = 1

    def add_edge_based_weight(self, source, destination, weight):
        self.adj_matrix[source][destination] = weight
        self.adj_matrix[destination][source] = weight

    def remove_edge(self, source, destination):
        if self.adj_matrix[source][destination] == 0:
            print(f"No Edge from {source} to {destination}")
            return
        self.adj_matrix[source][destination] = 0
        self.adj_matrix[destination][source] = 0


class AdjNode:
    def __init__(self, destination):
        self.destination = destination
        self.next = None


class AdjacencyList(AdjNode):
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.edges_list = [None] * self.num_vertices

    def add_edge(self, source, destination):
        new_node = AdjNode(destination)
        new_node.next = self.edges_list[source]
        self.edges_list[source] = new_node

        new_node = AdjNode(source)
        new_node.next = self.edges_list[destination]
        self.edges_list[destination] = new_node

    def print_adjacency_list(self):
        for list_index in range(self.num_vertices):
            current = self.edges_list[list_index]
            print(f"Adjacency List for vertex {list_index}: ", end="")
            while current:
                print(f"{current.destination} -> ", end="")
                current = current.next
            print("None")

    def print_adj_list(self):
        for key in self.edges_list.keys():
            print("node", key, ": ", self.edges_list[key])
