#include <iostream>

int main()
{
    std::cout << "Value of __cplusplus: " << __cplusplus << "\n";
    std::cout << "Value of __LINE__: " << __LINE__ << "\n";
    std::cout << "Value of __FILE__: " << __FILE__ << "\n";
    std::cout << "Value of __DATE__: " << __DATE__ << "\n";
    std::cout << "Value of __TIME__: " << __TIME__ << "\n";
    std::cout << "Value of __STDC__: " << __STDC__ << "\n";
    std::cout << "Value of __STDC_HOSTED__: " << __STDC_HOSTED__ << "\n";

    return 0;
}
