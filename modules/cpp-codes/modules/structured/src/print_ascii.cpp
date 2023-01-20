#include <iostream>

using namespace std;

void printASCII(char ch)
{
    int *p = new int{ch};
    cout << "The ASCII number is: " << *p << endl;
}
