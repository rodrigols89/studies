from Node import Node


class SinglyLinkedList:

    # Constructor to initialize the Node head.
    def __init__(self):
        self.head = None

    # Method to print the Linked List starting from a given node.
    def printListFromNodeN(self, n):
        if n is None:
            print("Node is empty!")
        else:
            current_node = n
            while current_node is not None:
                print(current_node.data, end=" ")
                current_node = current_node.next
            print()

    # Method to print the entire Linked List starting from the "head".
    def printListFromHead(self):
        if self.head is None:
            print("List is empty!")
        else:
            current_node = self.head
            while current_node is not None:
                print(current_node.data, end=" ")
                current_node = current_node.next
            print()
