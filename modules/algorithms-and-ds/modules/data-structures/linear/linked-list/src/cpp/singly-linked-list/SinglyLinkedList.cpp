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
