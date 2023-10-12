#include "SinglyLinkedList.h"
#include <iostream>

int main()
{
    SinglyLinkedList list;

    list.printListFromNodeN(list.head);

    list.head = new Node(10);
    list.head->next = new Node(20);
    list.head->next->next = new Node(30);

    list.printListFromNodeN(list.head);
    list.printListFromNodeN(list.head->next);
    list.printListFromNodeN(list.head->next->next);

    return 0;
}
