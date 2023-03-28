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

void SinglyLinkedList::printListFromHead(SinglyLinkedList list)
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
