##########################################################################
# Rodrigo Leite da Silva - drigols                                       #
# Last update: 23/12/2023                                                #
##########################################################################


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkedList(Node):
    def __init__(self):
        self.head = None
        self.tail = None

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        else:
            temp_node = self.head
            while temp_node.next is not None:
                temp_node = temp_node.next
            temp_node.next = new_node

    def append_constant(self, data):
        new_node = Node(data)
        if self.head is None:
            # If the list is empty, the "head" and "tail"
            # are set as the same Node (reference).
            self.head = new_node
            self.tail = self.head
        else:
            self.tail.next = new_node
            self.tail = new_node

    def print_list_from_head(self):
        if self.head is None:
            print("List is empty!")
            return
        else:
            current_node = self.head
            while current_node is not None:
                print(current_node.data, end=" ")
                current_node = current_node.next
        print("")
