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
    Node *new_node = new Node(data); // Allocate a new Node + put data.
    new_node->next = (this->head);   // Make "next" of the "new_node" point to head (old first Node).
    this->head     = new_node;       // Move the head to point to the new node.
}



// Method to insert a new Node after determined Node "n".
void SinglyLinkedList::insertAfterNodeN(Node *prev_node, int data)
{
    if (this->head == nullptr)
    {
        std::cout << "List is empty!\n";
        return; // Stop the method.
    }
    else if (prev_node == NULL)
    {
        std::cout << "The given previous Node cannot be NULL!";
        return; // Stop the method.
    }
    else
    {
        Node *new_node  = new Node(data);  // Allocate a new Node.
        new_node->next  = prev_node->next; // Make "next" of the "new_node" point to "next" of the "prev_node".
        prev_node->next = new_node;        // Make the "next" of "prev_node" point to the "new_node".
    }
}



// Method to insert a new Node at end of a Singly Linked List.
void SinglyLinkedList::append(int data)
{
    Node *new_node  = new Node(data); // Allocate a new Node.
    new_node->next  = NULL;           // Set "next" of new Node as NULL.

    // If the Linked List is empty, then make the "new_node" as head
    // and stop the method (return).
    if (this->head == NULL)
    {
        this->head = new_node;
        return; // Stop the method.
    }
    else
    {
        /**
         * "temp_node" Node was inited with memory address of head Node,
         * now let's loop to change it to be last Node.
        */
        Node *temp_node = this->head;
        while (temp_node->next != NULL)
        {
            temp_node = temp_node->next;
        }

        /**
         * Make "next" pointer of "temp_node" Node point to "new_node".
         * That's, "new_node" will be last node.
        */
        temp_node->next = new_node;
        return; // Stop the method.
    }
}



// Method to delete a Node "n" by position.
void SinglyLinkedList::deleteNodeN(int position)
{
    if (this->head == nullptr)
    {
        std::cout << "List is empty!\n";
        return; // Stop the method.
    }

    Node *temp_node = this->head;

    // If position=0, then remove the "head".
    if (position == 0)
    {
        this->head = temp_node->next; // Change second Node to be the new "head".
        free(temp_node);              // Free old head.
        return;                       // Stop the method.
    }

    // Finds the "Node" before the "Node" (position) to be deleted.
    for (int i = 0; temp_node != NULL && i < position - 1; i++)
        temp_node = temp_node->next;

    // Check if position is more than number of nodes.
    if (temp_node == NULL || temp_node->next == NULL)
    {
        std::cout << "The Node position exceeded!\n";
        return; // Stop the method.
    }

    Node *next = temp_node->next->next; // Save "next" of the Node will be deleted.
    free(temp_node->next);              // Delete the Node in the position passed, "temp_node->next".
    temp_node->next = next;             //  # Link the nodes.
}



// Method to print the entire Linked List starting from the "head".
void SinglyLinkedList::printListFromHead()
{
    if (this->head == nullptr)
    {
        std::cout << "List is empty!\n";
        return; // Stop the method.
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



// Method to print the Linked List starting from a given node.
void SinglyLinkedList::printListFromNodeN(Node *n)
{
    if (n == nullptr)
    {
        std::cout << "Node is empty!\n";
        return; // Stop the method.
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
        return; // Stop the method.
    }
}
