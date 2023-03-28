#ifndef LINKEDLIST_H_
#define LINKEDLIST_H_

#include "Node.h"

class SinglyLinkedList
{
public:
    Node *head;

    SinglyLinkedList();                            // Constructor prototype.
    void printListFromNodeN(Node *n);              // Method prototype.
    void printListFromHead(SinglyLinkedList list); // Method prototype.
};

#endif // LINKEDLIST_H_
