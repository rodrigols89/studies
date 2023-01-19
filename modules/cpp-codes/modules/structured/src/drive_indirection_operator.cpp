#include <iostream>

using namespace std;

int main()
{
    int number = 100;
    int * iptr = &number;

    cout << "Value stored in 'number' variable: " << number << endl;
    cout << "Memory Address of 'number' variable: " << &number << endl;
    cout << "Memory Addres saved in 'iptr' pointer: " << iptr << endl;
    cout << "Value stored at 'number' variable referenced by a 'iptr' pointer: "<< *iptr;

    return 0;
}
