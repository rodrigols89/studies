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

    # Method to insert a new Node at front.
    def push(self, data):
        # Allocate a new Node.
        new_node = Node()

        new_node.data = data      # Put data in the new Node.
        new_node.next = self.head # Make "next" of the "new_node" point to head (old first Node).
        self.head     = new_node  # Move the head to point to the new node.

    # Method to insert a new Node after determined Node "n".
    def insertAfterNodeN(self, prev_node, data):
        if self.head is None:
            print("List is empty!")
        elif prev_node is None:
            print("The given previous Node cannot be NULL!")
        else:
            # Allocate a new Node.
            new_node = Node()

            new_node.data  = data           # Put data in the new Node.
            new_node.next  = prev_node.next # Make "next" of the "new_node" point to "next" of the "prev_node".
            prev_node.next = new_node       # Move the "next" of "prev_node" as "new_node".

    def append(self, data):
        # Allocate a new Node.
        new_node = Node(data)

        last = self.head # Creates a Node "last" starting from the head.

        # Put data in the "new_node" and set "next" of new Node as None.
        new_node.data = data
        new_node.next = None

        # If the Linked List is empty, then make the "new_node" as head and stop the method (return).
        if self.head is None:
            self.head = new_node
            return
        else:
            # "Last" Node was initialized as head, now let's change it to be the last Node.
            while last.next is not None:
                last = last.next

            # Make "next" of "last" Node point to "new_node", that is,
            # "new_node" will be the last node.
            last.next = new_node
            return # Stop the method.
