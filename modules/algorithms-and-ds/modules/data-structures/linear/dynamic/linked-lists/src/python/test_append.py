##########################################################################
# Rodrigo Leite da Silva - drigols                                       #
# Last update: 09/11/2023                                                #
##########################################################################

from singly_linked_list import SinglyLinkedList, Node

if __name__ == "__main__":

    List1 = SinglyLinkedList()  # First list instance.
    print("List1 = 5->10->15->20->25 + append(30):")
    List1.head = Node(5)
    List1.head.next = Node(10)
    List1.head.next.next = Node(15)
    List1.head.next.next.next = Node(20)
    List1.head.next.next.next.next = Node(25)
    List1.append(30)
    List1.print_list_from_head()

    List2 = SinglyLinkedList()  # Second list instance.
    print("\nList2 = append(30):")
    List2.append(30)
    List2.print_list_from_head()

    list3 = SinglyLinkedList()  # Third list instance.
    print("\nList3 = append(1) + append(2) + append(3):")
    list3.append(1)
    list3.append(2)
    list3.append(3)
    list3.print_list_from_head()
