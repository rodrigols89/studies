#include "SinglyLinkedList.h"
#include <iostream>

int main()
{
    // Node pointers
    Node *head   = nullptr;
    Node *second = nullptr;
    Node *third  = nullptr;

    // Allocate 3 Nodes in the Heap.
    head   = new Node(10); // Assigns data from the constructor.
    second = new Node(20); // Assigns data from the constructor.
    third  = new Node(30); // Assigns data from the constructor.

    // Assign data manually to the Nodes.
    // head->data   = 10;  // assign data in first node.
    // second->data = 20;  // assign data to second node.
    // third->data  = 30;  // assign data to third node

    head->next   = second;  // Link first node with second
    second->next = third;   // Link second node with the first.
    third->next  = nullptr; // Set last Node (tail) as NULL.

    std::cout << "Value in the First Node (head): " << head->data << "\n";
    std::cout << "Value in the Second Node: " << second->data << "\n";
    std::cout << "Value in the Third Node (tail): " << third->data << "\n";

    return 0;
}
