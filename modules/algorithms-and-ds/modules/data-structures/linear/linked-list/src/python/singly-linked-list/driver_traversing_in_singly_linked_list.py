from SinglyLinkedList import SinglyLinkedList
from Node import Node

print("########## (Print values from Node 'n') ##########")

list = SinglyLinkedList()

list.printListFromNodeN(list.head)

list.head = Node(10)
list.head.next = Node(20)
list.head.next.next = Node(30)

list.printListFromNodeN(list.head)
list.printListFromNodeN(list.head.next)
list.printListFromNodeN(list.head.next.next)
list.printListFromNodeN(list.head.next.next.next)

print("\n####### (Print values from the 'head' Node) ######")

list = SinglyLinkedList()

list.printListFromHead()

list.head = Node(40)
list.printListFromHead()

list.head.next = Node(50)
list.printListFromHead()

list.head.next.next = Node(60)
list.printListFromHead()
