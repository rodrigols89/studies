##########################################################################
# Rodrigo Leite da Silva - drigols                                       #
# Last update: 09/11/2023                                                #
##########################################################################


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkedList(Node):
    def __init__(self):
        self.head = None

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.head  # Do "new_node" point to old head.
        self.head = new_node  # Set head as "new_node".

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        else:
            # Loop until the last Node (old last Node)
            # and save in the temp_node.
            temp_node = self.head
            while temp_node.next is not None:
                temp_node = temp_node.next
            # Do old last Node point to new last Node.
            temp_node.next = new_node

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
