#include "SinglyLinkedList.h"
#include <iostream>

int main()
{
    SinglyLinkedList list;

    std::cout << "Try delete a Node 'n' in an Empty List:\n";
    list.deleteNodeN(0);

    std::cout << "\nList = 8->2->3->1->7:\n";
    list.append(8);
    list.append(2);
    list.append(3);
    list.append(1);
    list.append(7);
    list.printListFromHead(); // Print Nodes values.

    std::cout << "\nList = (8->2->3->1->7) + deleteNodeN(4):\n";
    list.deleteNodeN(4);
    list.printListFromHead(); // Print Nodes values after delete Node position 1.

    std::cout << "\nTry to delete a Node 'n' that position is more than the number of nodes:\n";
    list.deleteNodeN(4);

    return 0;
}
