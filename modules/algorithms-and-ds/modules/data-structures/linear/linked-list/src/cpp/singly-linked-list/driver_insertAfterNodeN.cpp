#include "SinglyLinkedList.h"
#include <iostream>

int main()
{
    SinglyLinkedList list;
    list.head = new Node(10);
    list.head->next = new Node(20);
    list.head->next->next = new Node(30);
    list.head->next->next->next = new Node(50);
    list.printListFromHead(); // Print Node values.

    list.insertAfterNodeN(list.head->next->next, 40);
    list.printListFromHead(); // Print new Node values.

    return 0;
}
