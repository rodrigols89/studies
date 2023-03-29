#include <iostream>
#include "SinglyLinkedList.h"

// Constructor implementation (definition).
SinglyLinkedList::SinglyLinkedList()
{
    this->head = nullptr;
}

void SinglyLinkedList::printListFromNodeN(Node *n)
{
    if (n == nullptr)
    {
        std::cout << "Node is empty!"
                  << "\n";
    }
    else
    {
        Node *current_node = n;
        while (current_node != NULL)
        {
            std::cout << current_node->data << " ";
            current_node = current_node->next;
        }
        std::cout << "\n";
    }
}

void SinglyLinkedList::printListFromHead()
{
    if (this->head == nullptr)
    {
        std::cout << "List is empty!"
                  << "\n";
    }
    else
    {
        Node *current_node = this->head;
        while (current_node != NULL)
        {
            std::cout << current_node->data << " ";
            current_node = current_node->next;
        }
        std::cout << "\n";
    }
}

void SinglyLinkedList::push(int data)
{
    // Allocate a new Node.
    Node *new_node = new Node();

    new_node->data = data;         // Put data in the new Node.
    new_node->next = (this->head); // Make "next" of the "new_node" point to head (old first Node).
    this->head     = new_node;     // Move the head to point to the new node.
}

void SinglyLinkedList::insertAfterNodeN(Node *prev_node, int data)
{
    if (this->head == nullptr)
    {
        std::cout << "List is empty!"
                  << "\n";
    }
    else if (prev_node == NULL)
    {
        std::cout << "The given previous Node cannot be NULL!";
        return;
    }
    else
    {
        // Allocate a new Node.
        Node *new_node = new Node();

        new_node->data  = data;            // Put data in the new Node.
        new_node->next  = prev_node->next; // Make "next" of the "new_node" point to "next" of the "prev_node".
        prev_node->next = new_node;        // Move the "next" of "prev_node" as "new_node".
    }
}

void SinglyLinkedList::append(int data)
{
    // Allocate a new Node.
    Node *new_node = new Node();

    Node *last     = this->head; // Creates a Node "last" starting from the head.
    new_node->data = data;       // Put data in the "new_Node".
    new_node->next = NULL;       // Set "next" of new Node as NULL.

    // If the Linked List is empty, then make the "new_node" as head
    // and stop the method (return).
    if (this->head == NULL)
    {
        this->head = new_node;
        return;
    }
    else
    {
        // "Last" Node was inited as head, now let's change it to be last Node.
        while (last->next != NULL)
        {
            last = last->next;
        }

        // Make "next" of "last" Node point to "new_node", that's,
        // "new_node" will be last node.
        last->next = new_node;
        return; // Stop the method.
    }
}
