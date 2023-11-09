##########################################################################
# Rodrigo Leite da Silva - drigols                                       #
# Last update: 08/11/2023                                                #
##########################################################################

from singly_linked_list import Node

if __name__ == "__main__":

    # Create nodes.
    head = Node(10)
    second = Node(20)
    third = Node(30)

    # Connect nodes.
    head.next = second
    second.next = third

    # You don't need to set the next of the last node.
    # By default the next always points to None.
    # third.next = None

    print(f"Value in the First Node (head): {head.data}")
    print(f"Value in the Second Node: {second.data}")
    print(f"Value in the Third Node (tail): {third.data}")
