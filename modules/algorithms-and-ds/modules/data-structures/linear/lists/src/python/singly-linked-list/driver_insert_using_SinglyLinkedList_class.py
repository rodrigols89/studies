from SinglyLinkedList import SinglyLinkedList
from Node import Node

sll = SinglyLinkedList()

# Assign data using constructor.
sll.head = Node(10)
sll.head.next = Node(20)
sll.head.next.next = Node(30)

# Assign data using "." operator.
# sll.head.data = 1
# sll.head.next.data = 2
# sll.head.next.next.data = 3

print("Value in the First Node (head):", sll.head.data)
print("Value in the Second Node:", sll.head.next.data)
print("Value in the Third Node (tail):", sll.head.next.next.data)
