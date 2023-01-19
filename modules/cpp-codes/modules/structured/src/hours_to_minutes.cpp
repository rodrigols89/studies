#include <iostream>
using namespace std;

#define SECONDS_PER_HOUR 3600

int main()
{
    int seconds, hours;

    cout << "Enter hours amount: ";
    cin >> hours;

    seconds = hours * SECONDS_PER_HOUR;
    cout << hours << " hours have " << seconds << " seconds.\n";

    return 0;
}
