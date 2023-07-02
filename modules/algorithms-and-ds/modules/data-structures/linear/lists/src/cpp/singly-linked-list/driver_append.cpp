#include "SinglyLinkedList.h"
#include <iostream>

int main()
{

    std::cout << "List1 = 5->10->15->20->25 + append(30):\n";
    SinglyLinkedList list1;
    list1.head = new Node(5);
    list1.head->next = new Node(10);
    list1.head->next->next = new Node(15);
    list1.head->next->next->next = new Node(20);
    list1.head->next->next->next->next = new Node(25);
    list1.append(30);
    list1.printListFromHead(); // Print new Node value.

    std::cout << "\nList2 = append(30): \n";
    SinglyLinkedList list2;
    list2.append(30);
    list2.printListFromHead(); // Print new Node value.

    std::cout << "\nList3 = append(1) + append(2) + append(3): \n";
    SinglyLinkedList list3;
    list3.append(1);
    list3.append(2);
    list3.append(3);
    list3.printListFromHead();

    return 0;
}
