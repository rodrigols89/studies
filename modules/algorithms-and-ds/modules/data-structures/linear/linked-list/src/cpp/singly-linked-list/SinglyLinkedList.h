#ifndef LINKEDLIST_H_
#define LINKEDLIST_H_

#include "Node.h"

class SinglyLinkedList
{
public:
    Node *head;

    // Constructor prototype.
    SinglyLinkedList();

    // Insert methods.
    void push(int data);                              // Method prototype.
    void insertAfterNodeN(Node *prev_node, int data); // Method prototype.
    void append(int data);                            // Method prototype.

    // Delete methods.
    void deleteNodeN(int position);                   // Method prototype.

    // Traversing methods.
    void printListFromNodeN(Node *n);                 // Method prototype.
    void printListFromHead();                         // Method prototype.

};

#endif // LINKEDLIST_H_
