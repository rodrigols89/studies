from Node import Node


class SinglyLinkedList:

    # Constructor to initialize the Node head.
    def __init__(self):
        self.head = None



    # Method to insert a new Node at front.
    def push(self, data):
        new_node = Node(data)      # Allocate a new Node + put data.
        new_node.next = self.head  # Make "next" of the "new_node" point to head (old first Node).
        self.head     = new_node   # Move the head to point to the new node.



    # Method to insert a new Node after determined Node "n".
    def insertAfterNodeN(self, prev_node, data):
        if self.head is None:
            print("List is empty!")
            return # Stop the method.
        elif prev_node is None:
            print("The given previous Node cannot be NULL!")
            return # Stop the method.
        else:
            new_node       = Node(data)      # Allocate a new Node.
            new_node.next  = prev_node.next  # Make "next" of the "new_node" point to "next" of the "prev_node".
            prev_node.next = new_node        # Make the "next" of "prev_node" point to the "new_node".



    # Method to insert a new Node at end of a Singly Linked List.
    def append(self, data):
        new_node = Node(data)  # Allocate a new Node.
        temp     = self.head   # Creates a Node "last" starting from the head.

        # If the Linked List is empty, then make the "new_node" as head and stop the method (return).
        if self.head is None:
            self.head = new_node
            return
        else:
            # "Last" Node was initialized as head, now let's change it to be the last Node.
            while temp.next is not None:
                temp = temp.next

            # Make "next" pointer of "temp_node" Node point to "new_node".
            # That's, "new_node" will be last node.
            temp.next = new_node
            return # Stop the method.



    # Method to delete a Node "n" by position.
    def deleteNodeN(self, position):
        if self.head is None:
            print("List is empty!")
            return

        temp_node = self.head

        if position == 0:
            self.head = temp_node.next
            del temp_node
            return

        # Finds the "Node" before the "Node" (position) to be deleted.
        for i in range(position - 1):
            if temp_node is None:
                break
            temp_node = temp_node.next

        # Check if position is more than number of nodes.
        if temp_node is None or temp_node.next is None:
            print("The Node position exceeded!")
            return

        next = temp_node.next.next # Save "next" of the Node will be deleted.
        del temp_node.next         # Delete the Node in the position passed, "temp_node->next".
        temp_node.next = next      # Link the nodes.











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
