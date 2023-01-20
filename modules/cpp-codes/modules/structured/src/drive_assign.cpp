#include <iostream>

using namespace std;

int main()
{
    int vSize = 5;

    int *vec = new int[vSize];
    vec[0] = 15;
    vec[1] = 5;
    vec[2] = 30;
    vec[3] = 28;
    vec[4] = 40;

    cout << "The first value get by 'vec[0]': " << vec[0] << endl;
    cout << "The first value get by '*vec': " << *vec << endl;

    for (int i = 0; i < vSize; i++)
        cout << "Value in index " << i << " is " << vec[i] << endl;

    delete []vec;
    return 0;
}
