#include "SinglyLinkedList.h"
#include <iostream>

int main()
{
    SinglyLinkedList list;
    list.printListFromHead(list);

    list.head = new Node(10);
    list.printListFromHead(list);

    list.head->next = new Node(20);
    list.printListFromHead(list);

    list.head->next->next = new Node(30);
    list.printListFromHead(list);

    return 0;
}
