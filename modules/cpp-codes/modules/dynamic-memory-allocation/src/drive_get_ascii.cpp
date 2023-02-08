#include <iostream>
#include "get_ascii.h"

int main()
{
    char ch;

    std::cout << "Enter a character: ";
    std::cin >> ch;

    // Pointer (*pnum) var to save memory address returned by getASCII() function.
    int *pnum = getASCII(ch);

    std::cout << "Value saved in '*pnum' pointer allocated inside getASCII() function: " << *pnum << "\n";
    delete pnum; // delete allocated memory inside getASCII() function.
    std::cout << "Value saved in '*pnum' pointer after delete allocated memory: " << *pnum << "\n";

    return 0;
}
