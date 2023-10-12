from SinglyLinkedList import SinglyLinkedList
from Node import Node

print("List1 = 5->10->15->20->25 + append(30):")
List1 = SinglyLinkedList()
List1.head = Node(5)
List1.head.next = Node(10)
List1.head.next.next = Node(15)
List1.head.next.next.next = Node(20)
List1.head.next.next.next.next = Node(25)
List1.append(30)
List1.printListFromHead()

print("\nList2 = append(30):")
List2 = SinglyLinkedList()
List2.append(30)
List2.printListFromHead()

print("\nList3 = append(1) + append(2) + append(3):")
list3 = SinglyLinkedList()
list3.append(1)
list3.append(2)
list3.append(3)
list3.printListFromHead()
