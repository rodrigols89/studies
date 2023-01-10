#include <iostream>
using namespace std;

int main()
{
    unsigned char state = 1;

    cout << "Initial number: " <<  (int) state;
    state = state << 3;
    cout << "\nAfter apply LEFT SHIFT (<<) operator: " << (int) state;

    return 0;
}
