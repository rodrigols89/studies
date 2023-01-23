#include <iostream>

int sum(int x, int y, int z = 0, int w = 0)
{
    return (x + y + z + w);
}

int sum(int x, int y, float z = 0, float w = 0)
{
    return (x + y + z + w);
}

int main()
{
    std::cout << sum(10, 15) << "\n";
    std::cout << sum(10, 15, 25) << "\n";
    std::cout << sum(10, 15, 25, 30) << "\n";

    return 0;
}
