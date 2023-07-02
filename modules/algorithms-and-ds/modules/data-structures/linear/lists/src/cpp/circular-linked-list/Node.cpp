#include "Node.h"

// Constructor implementation (definition).
Node::Node(int data)
{
    this->data = data;
    this->prev = nullptr;
    this->next = nullptr;
}
