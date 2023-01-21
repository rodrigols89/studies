#include <iostream>
#include "div_throw.h"

using namespace std;

double div(double x, double y)
{
    if (y == 0)
        throw "Division by zero not allowed!";
    return (x / y);
}

int main()
{
    double x, y, z;

    cout << "Enter the first number: ";
    cin >> x;
    cout << "Enter the second number: ";
    cin >> y;

    try
    {
        z = div(x, y);
        cout << "The divsion is: " << z << endl;
    }
    catch (const char *msg)
    {
        cerr << msg << endl;
    }

    return 0;
}
