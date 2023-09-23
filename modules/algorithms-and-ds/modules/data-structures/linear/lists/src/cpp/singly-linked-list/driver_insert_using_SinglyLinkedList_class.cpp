#include "SinglyLinkedList.h"
#include <iostream>

int main()
{
    SinglyLinkedList sll;

    // Assign data using constructor.
    sll.head = new Node(10);
    sll.head->next = new Node(20);
    sll.head->next->next = new Node(30);

    // Assign data using "->" operator.
    // sll.head->data              = 10;
    // sll.head->next->data        = 20;
    // sll.head->next->next->data  = 30;

    std::cout << "Value in the First Node (head): " << sll.head->data << "\n";
    std::cout << "Value in the Second Node: " << sll.head->next->data << "\n";
    std::cout << "Value in the Third Node (tail): " << sll.head->next->next->data << "\n";

    return 0;
}
