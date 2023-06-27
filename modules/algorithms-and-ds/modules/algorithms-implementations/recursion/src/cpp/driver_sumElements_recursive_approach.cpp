#include <iostream>
#include <vector>

int sumElementsRecursive(std::vector<int> list)
{
    if (list.size() == 1) {  // Base case.
        return list[0];
    } else {
        int lastElement = list.back();  // Get the last element.
        list.pop_back();  // Remove the last element from the list.
        int sum = lastElement + sumElementsRecursive(list);  // Recursive call.
        return sum;
    }
}

int main()
{
    std::vector<int> myList = {1, 3, 5, 7, 9};
    std::cout << "The sum of all element is: " << sumElementsRecursive(myList);
    return 0;
}
