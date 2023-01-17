#include <iostream>
using namespace std;

int main()
{
    int *iptr = new int; // Allocate memory for an Integer.
    *iptr = 1001;        // Save a value (using "*" operator | Indirection Operator)
    cout << "Integer value: " << *iptr << endl;
    cout << "Location: " << iptr << endl;
    cout << "Size of 'iptr': " << sizeof(iptr) << endl;
    cout << "Size of '*iptr': " << sizeof(*iptr) << endl;

    double *dprt = new double;     // Allocate memory for a double
    *dprt = 500.35;                // Save a value (using "*" operator | Indirection Operator)
    cout << "\nFloating-point value: " << *dprt << endl;
    cout << "Location: " << dprt << endl;
    cout << "Size of 'dprt': " << sizeof(dprt) << endl;
    cout << "Size of '*dprt': " << sizeof(*dprt) << endl;

    return 0;
}
