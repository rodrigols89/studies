#include <iostream>

void countCalls()
{
    static int count = 1;
    // This increment is after cout print (count++).
    std::cout << "The number of calls from this function is: " << count++ << "\n";
}
