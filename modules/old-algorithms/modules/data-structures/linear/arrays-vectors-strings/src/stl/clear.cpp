#include <iostream>
#include <array>
#include <vector>
#include <string>

int main()
{
    std::cout << "------------- ( Vecto example ) --------------\n";
    std::vector<int> myvector = {1, 2, 3, 4, 5};
    std::cout << "Vector elements before apply clear() function:\n";
    for (int element : myvector)
        std::cout << element << " ";
    myvector.clear();
    std::cout << "\nVector elements before after clear() function:\n";
    for (int element : myvector)
        std::cout << element << " ";

    std::cout << "\n------------- ( String example ) --------------";
    std::string mystring = "Hello World!";
    std::cout << "\nString elements before apply clear() function:\n";
    std::cout << mystring;
    mystring.clear();
    std::cout << "\nString elements before after clear() function:\n";
    std::cout << mystring;

    return 0;
}
