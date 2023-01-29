#include <iostream>
using namespace std;

// Node class representation.
class Node {
public:
    int data;
    Node *next;
};

void printList(Node* n); // Function prototype.

// Driver's code.
int main()
{
    Node *head = NULL;
    Node *second = NULL;
    Node *third = NULL;

    // allocate 3 nodes in the heap.
    head = new Node();
    second = new Node();
    third = new Node();

    head->data = 1;       // assign data in first node.
    head->next = second;  // Link first node with second.

    second->data = 2;     // assign data to second node.
    second->next = third; // Link second node with third.

    third->data = 3;      // assign data to third node.
    third->next = NULL;   // Pointer next to NULL.

    // Function call
    printList(head);

    return 0;
}

// This function prints contents of linked list
void printList(Node* node_n)
{
    while (node_n != NULL)
    {
        cout << node_n->data << " ";
        node_n = node_n->next;
    }
}
