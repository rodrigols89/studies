#include <iostream>
#include <vector>

int sumElements(std::vector<int> list)
{
    int sum = 0;
    for (int element : list)
        sum += element;
    return sum;
}

int main()
{
    std::vector<int> myList = {1, 3, 5, 7, 9};
    std::cout << "The sum of all element is: " << sumElements(myList);
    return 0;
}
