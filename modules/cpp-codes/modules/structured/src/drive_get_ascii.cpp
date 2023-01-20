#include <iostream>
#include "get_ascii.h"

using namespace std;

int main()
{
    char ch;

    cout << "Enter a character: ";
    cin >> ch;

    // Pointer (*pnum) var to save memory address returned by getASCII() function.
    int *pnum = getASCII(ch);

    cout << "Value saved in '*pnum' pointer allocated inside getASCII() function: " << *pnum << endl;
    delete pnum; // delete allocated memory inside getASCII() function.
    cout << "Value saved in '*pnum' pointer after delete allocated memory: " << *pnum << endl;

    return 0;
}
