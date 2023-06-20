#include "SinglyLinkedList.h"
#include <iostream>

int main()
{
    SinglyLinkedList sll;

    sll.head = new Node(5);                    // 5(head)
    sll.head->next = new Node(10);             // 5(head)->10
    sll.head->next->next = new Node(20);       // 5(head)->10->20
    sll.head->next->next->next = new Node(25); // 5(head)->10->20->25

    std::cout << "Singlye Linked List before insert the new Node:" << "\n";
    std::cout << "Data in the first (head) Node: " << sll.head->data << "\n";
    std::cout << "Data in the second Node: " << sll.head->next->data << "\n";
    std::cout << "Data in the third Node: " << sll.head->next->next->data << "\n";
    std::cout << "Data in the four Node: " << sll.head->next->next->next->data << "\n";

    // 5(head)->10(passed_node)->new_node(15)->20->25
    sll.insertAfterPassedNode(sll.head->next, 15);

    std::cout << "\nSinglye Linked List after insert the new Node:" << "\n";
    std::cout << "Data in the first (head) Node: " << sll.head->data << "\n";
    std::cout << "Data in the second Node: " << sll.head->next->data << "\n";
    std::cout << "Data in the third Node: " << sll.head->next->next->data << "\n";
    std::cout << "Data in the four Node: " << sll.head->next->next->next->data << "\n";
    std::cout << "Data in the fifth Node: " << sll.head->next->next->next->next->data << "\n";

    return 0;
}
