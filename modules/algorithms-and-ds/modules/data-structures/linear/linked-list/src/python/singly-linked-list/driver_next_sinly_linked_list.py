from SinglyLinkedList import SinglyLinkedList
from Node import Node

list = SinglyLinkedList()
list.head = Node(10)
list.head.next = Node(20)
list.head.next.next = Node(30)

# Assign data manually to the Nodes.
# list.head.data = 1  # assign data in first node.
# list.head.next.data = 2  # assign data to second node.
# list.head.next.next.data = 3  # assign data to third node

print("Value in the First Node (head):", list.head.data)
print("Value in the Second Node:", list.head.next.data)
print("Value in the Third Node (tail):", list.head.next.next.data)
