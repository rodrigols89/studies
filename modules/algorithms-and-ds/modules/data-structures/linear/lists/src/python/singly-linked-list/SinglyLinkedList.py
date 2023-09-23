from Node import Node


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    # Method to insert a new Node after passed Node.
    def insertAfterPassedNode(self, passed_node, data):
        if passed_node is None:
            print("The passed Node cannot be NULL!")
            return
        new_node = Node(data)
        new_node.next = passed_node.next
        passed_node.next = new_node

    # Method to insert a new Node at end of a Singly Linked List.
    def append(self, data):
        new_node = Node(data)
        new_node.next = None
        if self.head is None:
            self.head = new_node
            return
        else:
            temp_node = self.head
            while temp_node.next is not None:
                temp_node = temp_node.next
            temp_node.next = new_node

    # Method to delete a Node "n" by position.
    def deleteNodeN(self, position):
        if self.head is None:
            print("List is empty!")
            return
        else:
            temp_node = self.head
            if position == 0:
                self.head = temp_node.next
                del temp_node
                return
            for i in range(position - 1):
                if temp_node is None:
                    break
                temp_node = temp_node.next
            if temp_node is None or temp_node.next is None:
                print("The Node position exceeded!")
                return
            next = temp_node.next.next
            del temp_node.next
            temp_node.next = next

    # Method to print the entire Linked List starting from the "head".
    def printListFromHead(self):
        if self.head is None:
            print("List is empty!")
            return
        else:
            current_node = self.head
            while current_node is not None:
                print(current_node.data, end=" ")
                current_node = current_node.next
