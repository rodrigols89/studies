#include <iostream>
using namespace std;

int main()
{
    char character;

    cout << "Enter the character: ";
    cin >> character;

    cout << "\nThe passed character was: " << character << endl;

    // Get (convert) the passed character number.
    int ascii_number = character;

    cout << "The ASCII number to " << character << " letter is "
         << ascii_number;

    return 0;
}
