#include <iostream>
#include "sum_library.h"

int main()
{
    int result = SumLibrary::sum(3, 4);
    std::cout << "The sum is: " << result << std::endl;

    return 0;
}
