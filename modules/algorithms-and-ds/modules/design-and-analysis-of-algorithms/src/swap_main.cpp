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

    // Call the swap() function.
    swap(x, y);

    cout << "After swapping " <<
    "the first value is " << x <<
    ", the second value is " << y << ".";


    return 0;
}
