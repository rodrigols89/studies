#ifndef LINKEDLIST_H_
#define LINKEDLIST_H_

#include "Node.h"

class SinglyLinkedList
{
public:
    Node *head;

    SinglyLinkedList(); // Constructor prototype.

    // Insert methods.
    void push(int data);                                     // Method prototype.
    void insertAfterPassedNode(Node *passed_node, int data); // Method prototype.
    void append(int data);                                   // Method prototype.

    // Delete methods.
    void deleteNodeN(int position);                          // Method prototype.

    // Traversing methods.
    void printListFromHead();                                // Method prototype.
};

#endif // LINKEDLIST_H_
