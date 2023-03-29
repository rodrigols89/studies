from SinglyLinkedList import SinglyLinkedList
from Node import Node

list = SinglyLinkedList()
list.head = Node(10)
list.head.next = Node(20)
list.head.next.next = Node(30)
list.head.next.next.next = Node(50)
list.printListFromHead() # Print Nodes values.

list.insertAfterNodeN(list.head.next.next, 40)
list.printListFromHead() # Print new Node value.
