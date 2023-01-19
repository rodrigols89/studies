#include <iostream>
#include "swap.h"
using namespace std;


int main()
{
    int x, y;

    cout << "Enter the first value: ";
    cin >> x;

    cout << "Enter the second value: ";
    cin >> y;

    cout << "Initial values:\n" <<
    "First value: " << x << 
    "\nSecond value: " << y << endl;

    // Call the swap() function.
    swap(x, y);

    cout << "\nAfter swapping:\n" <<
    "First value: " << x << 
    "\nSecond value: " << y << endl;


    return 0;
}
