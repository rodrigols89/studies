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

void SinglyLinkedList::push(int data)
{
    Node *new_node = new Node();   // Allocate a new Node.
    new_node->data = data;         // Put data in the new Node.
    new_node->next = (this->head); // Make "next" of the "new_node" point to head (old first Node).
    this->head     = new_node;     // Move the head to point to the new node.
}

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
        Node *new_node = new Node();       // Allocate a new Node.
        new_node->data  = data;            // Put data in the new Node.
        new_node->next  = prev_node->next; // Make "next" of the "new_node" point to "next" of the "prev_node".
        prev_node->next = new_node;        // Move the "next" of "prev_node" as "new_node".
    }
}

void SinglyLinkedList::append(int data)
{
    Node *new_node = new Node(); // Allocate a new Node.
    Node *last     = this->head; // Creates a Node "last" starting from the head.
    new_node->data = data;       // Put data in the "new_Node".
    new_node->next = NULL;       // Set "next" of new Node as NULL.

    // If the Linked List is empty, then make the "new_node" as head
    // and stop the method (return).
    if (this->head == NULL)
    {
        this->head = new_node;
        return; // Stop the method.
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

void SinglyLinkedList::deleteNodeN(int position)
{
    if (this->head == nullptr)
    {
        std::cout << "List is empty!\n";
        return; // Stop the method.
    }
    else
    {
        Node *temp = this->head; // Store head node.
        // If position=0, then remove the "head".
        if (position == 0)
        {
            this->head = temp->next; // Change second Node to be the new "head".
            free(temp);              // Free old head.
            return;                  // Stop the method.
        }
        else
        {
            /**
             * [Finds the "Node" before the "Node" (position) to be deleted]
             * Check in all iterations if the de Node (starting from temp=head)
             * is NULL and "i < position -1", that's, the Node before the "Node"
             * (position) to be deleted.
             *
             * For example, imagine we have the following list: 8->2->3->1->7->NULL
             *
             * - temp = head (zero 0) = [8]->2->3->1->7->NULL
             * - Imagine that passed position was: 4
             *
             * First iteration: i=0 < (position=4 - 1) = 3 | YES!
             * (temp = temp->next) = 8->[2]->3->1->7->NULL
             *
             * Second iteration: i++, i=1 < (position=4 - 1) = 3 | YES!
             * (temp = temp->next) = 8->2->[3]->1->7->NULL
             *
             * Third iteration: i++, i=2 < (position=4 - 1) = 3 | YES!
             * (temp = temp->next) =  8->2->3->[1]->7->NULL
             *
             * Fourth iteration: i++, i=3 < (position=4 - 1) = 3 | NO!
             * The internal statements in the loop "for" now not is executed!
             *
             * Ok, we have the "Node" before the "Node" that will be deleted
             * saved in the "temp" pointer: 8->2->3->[1]->7->NULL
             *
             * [Another example was if the "position" was 1:]
             *
             * First iteration: i=0 < (position=1 - 1) = 0 | NO!
             * That's, temp = [8]->2->3->1->7->NULL, a "Node" before the
             * Node" that will be deleted saved in the "temp" pointer.
             */
            for (int i = 0; temp != NULL && i < position - 1; i++)
                temp = temp->next;

            // Check if position is more than number of nodes.
            if (temp == NULL || temp->next == NULL)
            {
                std::cout << "The Node position exceeded!\n";
                return; // Stop the method.
            }

            /**
             * As the "temp->next" is the Node that will be deleted, we need to save
             * the "next" of the Node that will be deleted in some pointer (next).
             *
             * For example, position=1:
             *
             *  next   =   temp -> next -> next
             *              [8] ->  2   ->   3   ->1->7->NULL
             *                      |        |
             *                      |        ---(Node will be save in "next" pointer)
             *                      |
             *            (Node will be deleted)
             */
            Node *next = temp->next->next;

            /**
             * Delete the Node in the position passed, "temp->next":
             *
             *  next   =   temp ->        -> next
             *              [8] ->        ->   3   ->1->7->NULL
             *                                 |
             *                                 ---(Node will be save in "next" pointer)
             */
            free(temp->next); // Free Node selected in memory.

            /**
             * Make the "Node" before the "Node" that was deleted point
             * to the "Node" after the "Node" that was deleted.
             *
             *    [8]->3->1->7->NULL
             *     |   |
             *     |   ---------
             *     |           |
             * temp->next = next
             */
            temp->next = next;
        }
    }
}
