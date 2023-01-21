#include <iostream>
using namespace std;

int main()
{
    try
    {
        throw 'a';
    }
    catch (int x)
    {
        cout << "Caught ";
    }

    cout << "Never printed!";
    return 0;
}
