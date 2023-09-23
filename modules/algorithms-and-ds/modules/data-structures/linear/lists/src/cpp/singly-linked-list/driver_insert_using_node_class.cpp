#include "Node.h"
#include <iostream>

int main()
{
    // Node pointers
    Node *head   = nullptr;
    Node *second = nullptr;
    Node *third  = nullptr;

    // Assign data using constructor.
    head   = new Node(10);
    second = new Node(20);
    third  = new Node(30);

    // Assign data using "->" operator.
    // head->data   = 10;
    // second->data = 20;
    // third->data  = 30;

    head->next   = second;  // Link first (head) node with second.
    second->next = third;   // Link second node with the third.
    third->next  = nullptr; // Set last Node (tail) as NULL.

    std::cout << "Value in the First Node (head): " << head->data << "\n";
    std::cout << "Value in the Second Node: " << second->data << "\n";
    std::cout << "Value in the Third Node (tail): " << third->data << "\n";

    return 0;
}
