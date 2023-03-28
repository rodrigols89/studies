from SinglyLinkedList import SinglyLinkedList
from Node import Node

# Node pointers
head = None
second = None
third = None

# Allocate 3 Nodes in the Heap.
head = Node(10)  # Assigns data from the constructor.
second = Node(20)  # Assigns data from the constructor.
third = Node(30)  # Assigns data from the constructor.

# Assign data manually to the Nodes.
# head.data = 10  # assign data in first node.
# second.data = 20  # assign data to second node.
# third.data = 30  # assign data to third node

head.next = second  # Link first node with second
second.next = third  # Link second node with the first.
third.next = None  # Set last Node (tail) as NULL.

print(f"Value in the First Node (head): {head.data}")
print(f"Value in the Second Node: {second.data}")
print(f"Value in the Third Node (tail): {third.data}")
