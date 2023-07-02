from SinglyLinkedList import SinglyLinkedList
from Node import Node

print("####### ( Print Node values from the 'head' until 'tail' ) ######")

sll = SinglyLinkedList()

sll.printListFromHead()

sll.head = Node(40)
sll.printListFromHead()

sll.head.next = Node(50)
sll.printListFromHead()

sll.head.next.next = Node(60)
sll.printListFromHead()
