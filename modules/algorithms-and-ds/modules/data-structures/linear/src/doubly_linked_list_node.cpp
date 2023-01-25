#include <iostream>
using namespace std;

// Node of a doubly linked list
class Node {
public:
    int data;
    Node *next; // Pointer to next node in DLL.
    Node *prev; // Pointer to previous node in DLL.
};
