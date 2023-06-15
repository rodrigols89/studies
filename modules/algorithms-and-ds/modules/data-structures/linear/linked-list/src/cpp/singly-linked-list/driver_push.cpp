#include "SinglyLinkedList.h"
#include <iostream>

int main()
{
    SinglyLinkedList sll;

    /**
     * Remember, we are using the push() approach, that's,
     * the new Node is added in the front of the Singly Linked List.
    */
    sll.push(25); // 25(head)
    sll.push(20); // 20(head)->25
    sll.push(15); // 15(head)->20->25
    sll.push(10); // 10(head)->15->20->25
    sll.push(5);  // 5 (head)->10->15->20->25

    std::cout << "Data in the first (head) Node: " << sll.head->data << "\n";
    std::cout << "Data in the second Node: " << sll.head->next->data << "\n";
    std::cout << "Data in the third Node: " << sll.head->next->next->data << "\n";
    std::cout << "Data in the four Node: " << sll.head->next->next->next->data << "\n";
    std::cout << "Data in the fifth Node: " << sll.head->next->next->next->next->data << "\n";

    return 0;
}
