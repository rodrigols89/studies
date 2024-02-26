#include <iostream>
#include <vector>

int main()
{
    std::vector<int> v = {10, 20, 30, 40, 50};

    std::cout << "Print Vector elements using at() function: ";
    for (int i = 0; i < v.size(); i++)
        std::cout << v.at(i) << " ";

    std::cout << "\nsize(): " << v.size();
    std::cout << "\nmax_size(): " << v.max_size();
    std::cout << "\ncapacity(): " << v.capacity();
    std::cout << "\nfront(): " << v.front();
    std::cout << "\nback(): " << v.back();
    std::cout << "\ndata(): " << v.data();

    v.assign(5, 0);
    std::cout << "\nPrint Vector elements after use 'assing(5, 0)' function: ";
    for (int i = 0; i < v.size(); i++)
        std::cout << v.at(i) << " ";
    
    v.push_back(10);
    std::cout << "\nPrint the Vector after 'push_back(10)': ";
    for (int i = 0; i < v.size(); i++)
        std::cout << v.at(i) << " ";

    return 0;
}
