#include "SinglyLinkedList.h"
#include <iostream>

int main()
{
    SinglyLinkedList list;
    // list.head = new Node(10);
    // list.head->next = new Node(15);
    // list.head->next->next = new Node(20);
    // list.head->next->next->next = new Node(25);
    list.printListFromHead(); // Print Nodes values.

    list.push(5);
    list.printListFromHead(); // Print new Node value.

    return 0;
}

