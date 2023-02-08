#include <iostream>

int main()
{
    int vSize;

    std::cout << "Enter the Vector size: ";
    std::cin >> vSize;

    int *vec = new int[vSize];
    delete vec;

    return 0;
}
