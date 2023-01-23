// C++ program to demonstrate nesting of namespaces
#include <iostream>
using namespace std;

// Nested namespace
namespace out
{
    int val = 5;
    namespace in
    {
        int val2 = val;
    }
}

// Driver code
int main()
{
    cout << out::in::val2; // prints 5
    return 0;
}
