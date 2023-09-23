#include <iostream>
#include "SinglyLinkedList.h"

// Constructor implementation (definition).
SinglyLinkedList::SinglyLinkedList()
{
    this->head = nullptr;
}

// Method to insert a new Node at front.
void SinglyLinkedList::push(int data)
{
    Node *new_node = new Node(data);
    new_node->next = (this->head);
    this->head = new_node;
}

// Method to insert a new Node after passed Node.
void SinglyLinkedList::insertAfterPassedNode(Node *passed_node, int data)
{
    if (passed_node == NULL)
    {
        std::cout << "The passed Node cannot be NULL!";
        return;
    }
    Node *new_node = new Node(data);
    new_node->next = passed_node->next;
    passed_node->next = new_node;
}

// Method to insert a new Node at end of a Singly Linked List.
void SinglyLinkedList::append(int data)
{
    Node *new_node = new Node(data);
    new_node->next = NULL;
    if (this->head == NULL)
    {
        this->head = new_node;
        return; // Stop the method.
    }
    else
    {
        Node *temp_node = this->head;
        while (temp_node->next != NULL)
        {
            temp_node = temp_node->next;
        }
        temp_node->next = new_node;
    }
}

// Method to delete a Node "n" by position.
void SinglyLinkedList::deleteNodeN(int position)
{
    if (this->head == nullptr)
    {
        std::cout << "List is empty!\n";
        return;
    }
    else
    {
        Node *temp_node = this->head;
        if (position == 0)
        {
            this->head = temp_node->next;
            free(temp_node);
            return;
        }
        for (int i = 0; temp_node != NULL && i < position - 1; i++)
            temp_node = temp_node->next;
        if (temp_node == NULL || temp_node->next == NULL)
        {
            std::cout << "The Node position exceeded!\n";
            return;
        }
        Node *next = temp_node->next->next;
        free(temp_node->next);
        temp_node->next = next;
    }
}

// Method to print the entire Linked List starting from the "head".
void SinglyLinkedList::printListFromHead()
{
    if (this->head == nullptr)
    {
        std::cout << "List is empty!\n";
        return;
    }
    else
    {
        Node *current_node = this->head;
        while (current_node != NULL)
        {
            std::cout << current_node->data << " ";
            current_node = current_node->next;
        }
    }
}
