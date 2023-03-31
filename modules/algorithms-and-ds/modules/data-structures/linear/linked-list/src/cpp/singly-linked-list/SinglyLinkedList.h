#ifndef LINKEDLIST_H_
#define LINKEDLIST_H_

#include "Node.h"

class SinglyLinkedList
{
public:
    Node *head;

    SinglyLinkedList();                               // Constructor prototype.
    void printListFromNodeN(Node *n);                 // Method prototype.
    void printListFromHead();                         // Method prototype.
    void push(int data);                              // Method prototype.
    void insertAfterNodeN(Node *prev_node, int data); // Method prototype.
    void append(int data);                            // Method prototype.
    void deleteNodeN(int position);                   // Method prototype.
};

#endif // LINKEDLIST_H_
