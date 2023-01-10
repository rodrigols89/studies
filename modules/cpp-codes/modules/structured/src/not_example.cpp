#include <iostream>
using namespace std;

int main()
{
    unsigned char state = 1;

    cout << "Initial number: " <<  (int) state;
    state = ~state;
    cout << "\nAfter apply NOT (~) operator: " << (int) state;

    return 0;
}
