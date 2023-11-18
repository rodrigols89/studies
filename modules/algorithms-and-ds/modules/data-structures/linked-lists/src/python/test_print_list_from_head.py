##########################################################################
# Rodrigo Leite da Silva - drigols                                       #
# Last update: 09/11/2023                                                #
##########################################################################

from singly_linked_list import SinglyLinkedList, Node

if __name__ == "__main__":

    sll = SinglyLinkedList()

    print("####### ( Print values from the 'head' until 'tail' ) ######")
    sll.print_list_from_head()  # Empty list case.

    sll.head = Node(40)  # 40(head)
    sll.print_list_from_head()

    sll.head.next = Node(50)  # 40(head)->50
    sll.print_list_from_head()

    sll.head.next.next = Node(60)  # 40(head)->50->60
    sll.print_list_from_head()
