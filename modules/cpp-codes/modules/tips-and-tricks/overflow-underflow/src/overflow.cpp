#include <iostream>
#include <climits>
using namespace std;

int main()
{
    short john = SHRT_MAX;
    unsigned short mary = SHRT_MAX;

    cout << "john have " << john << " dollars." << endl;
    cout << "Maria have " << mary << " dollars." << endl;

    cout << endl
         << "Added 1 dollar to each..." << endl
         << endl;
    john = john + 1;
    mary = mary + 1;

    cout << "Agora john have " << john << " dollars." << endl;
    cout << "Agora Maria have " << mary << " dollars." << endl;

    return 0;
}
