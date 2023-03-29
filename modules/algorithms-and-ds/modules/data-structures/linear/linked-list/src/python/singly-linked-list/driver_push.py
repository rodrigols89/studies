from SinglyLinkedList import SinglyLinkedList
from Node import Node

list = SinglyLinkedList()
list.head = Node(10)
list.head.next = Node(15)
list.head.next.next = Node(20)
list.head.next.next.next = Node(25)
list.printListFromHead() # Print Nodes values.

list.push(5)
list.printListFromHead() # Print new Node value.
