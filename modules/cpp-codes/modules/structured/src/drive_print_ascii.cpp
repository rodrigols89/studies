#include <iostream>
#include "print_ascii.h"

using namespace std;

int main()
{
    char ch;

    cout << "Enter a character: ";
    cin >> ch;

    printASCII(ch);

    return 0;
}
