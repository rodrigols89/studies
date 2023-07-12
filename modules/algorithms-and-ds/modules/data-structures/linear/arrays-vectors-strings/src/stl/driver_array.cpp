#include <iostream>
#include <array>

int main()
{
    std::array<int, 6> arr = {1, 2, 3, 4, 5, 6};

    // Printing array elements using at() functions.
    std::cout << "Print Array elements using at() function: ";
    for (int i = 0; i < arr.size(); i++)
        std::cout << arr.at(i) << " ";

    std::cout << "\nPrint the first element using '[index]' operator: " << arr[0];
    std::cout << "\nPrint the second element using '[index]' operator: " << arr[1];
    std::cout << "\nPrint the third element using '[index]' operator: " << arr[2];

    std::cout << "\nempty() = True to empty list or False to not empty list: " << arr.empty();
    std::cout << "\nsize(): " << arr.size();
    std::cout << "\nmax_size(): " << arr.max_size();
    std::cout << "\nfront(): " << arr.front();
    std::cout << "\nback(): " << arr.back();

    std::array<int, 5> arr_two = {10, 20, 30, 40, 50};
    std::array<int, 5> arr_three = {60, 70, 80, 90, 100};

    std::cout << "\nElements of the array_two: ";
    for (int i = 0; i < arr_two.size(); i++)
        std::cout << arr_two.at(i) << " ";

    std::cout << "\nElements of the arr_three: ";
    for (int i = 0; i < arr_three.size(); i++)
        std::cout << arr_three.at(i) << " ";

    arr_two.swap(arr_three);
    std::cout << "\nAfter swap() the array elements:";

    std::cout << "\nElements of the array_two: ";
    for (int i = 0; i < arr_two.size(); i++)
        std::cout << arr_two.at(i) << " ";

    std::cout << "\nElements of the arr_three: ";
    for (int i = 0; i < arr_three.size(); i++)
        std::cout << arr_three.at(i) << " ";

    std::array<int, 10> zeros;
    zeros.fill(0);
    std::cout << "\nArray filled with zeros: ";
    for (int i = 0; i < zeros.size(); i++)
        std::cout << zeros.at(i) << " ";

    return 0;
}
