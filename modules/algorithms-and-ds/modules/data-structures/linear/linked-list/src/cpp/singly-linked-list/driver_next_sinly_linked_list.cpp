#include "SinglyLinkedList.h"
#include <iostream>

int main()
{
    SinglyLinkedList list;
    list.head = new Node(10);
    list.head->next = new Node(20);
    list.head->next->next = new Node(30);

    // Assign data manually to the Nodes.
    // list.head->data              = 1;  // assign data in first node.
    // list.head->next->data        = 2;  // assign data to second node.
    // list.head->next->next->data  = 3;  // assign data to third node

    std::cout << "Value in the First Node (head): " << list.head->data << "\n";
    std::cout << "Value in the Second Node: " << list.head->next->data << "\n";
    std::cout << "Value in the Third Node (tail): " << list.head->next->next->data << "\n";

    return 0;
}
