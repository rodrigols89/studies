#include <iostream>
#include "div_throw.h"

using namespace std;

int main()
{
    double x, y, z;

    cout << "Enter the first number: ";
    cin >> x;
    cout << "Enter the second number: ";
    cin >> y;

    z = div(x, y);
    cout << "The divsion is: " << z << endl;

    return 0;
}
