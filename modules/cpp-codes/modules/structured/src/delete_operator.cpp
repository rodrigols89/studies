#include <iostream>
using namespace std;

int main()
{
    int *iptr = new int; // Allocate memory for an Integer.
    *iptr = 30;          // Save a value (using "*" operator | Indirection Operator)

    cout << "Memory Address save in 'iptr' pointer: " << iptr << endl;
    cout << "Value save in the Memory Address save in 'iptr' pointer: " << *iptr << endl;
    cout << "Memory Address of 'iptr' pointer: " << &iptr << endl << endl;
    delete iptr;
    cout << "After use 'delete' operator in 'iptr' pointer: " << endl;
    cout << "Memory Address save in 'iptr' pointer: " << iptr << endl;
    cout << "Value save in the Memory Address save in 'iptr' pointer: " << *iptr << endl;
    cout << "Memory Address of 'iptr' pointer: " << &iptr << endl;

    return 0;
}
