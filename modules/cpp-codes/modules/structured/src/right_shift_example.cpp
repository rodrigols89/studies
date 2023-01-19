#include <iostream>
using namespace std;

int main()
{
    unsigned char state = 8;

    cout << "Initial number: " <<  (int) state;
    state = state >> 1;
    cout << "\nAfter apply RIGHT SHIFT (<<) operator: " << (int) state;

    return 0;
}
