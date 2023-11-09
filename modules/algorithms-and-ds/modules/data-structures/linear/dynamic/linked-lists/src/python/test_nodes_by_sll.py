##########################################################################
# Rodrigo Leite da Silva - drigols                                       #
# Last update: 08/11/2023                                                #
##########################################################################

from singly_linked_list import SinglyLinkedList, Node

if __name__ == "__main__":

    # Singly Linked List instance.
    sll = SinglyLinkedList()

    # Assign data + Link the Nodes.
    sll.head = Node(10)  # 10
    sll.head.next = Node(20)  # 10->20
    sll.head.next.next = Node(30)  # 10->20->30

    print("Value in the First Node (head):", sll.head.data)
    print("Value in the Second Node:", sll.head.next.data)
    print("Value in the Third Node (tail):", sll.head.next.next.data)
