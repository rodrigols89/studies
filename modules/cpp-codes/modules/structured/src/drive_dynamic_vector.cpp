#include <iostream>

using namespace std;

int main()
{
    int vSize;

    cout << "Enter the Vector size: ";
    cin >> vSize;

    int *vec = new int[vSize];
    delete vec;

    return 0;
}
