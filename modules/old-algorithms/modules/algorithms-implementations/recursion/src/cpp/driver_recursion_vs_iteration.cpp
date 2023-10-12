#include <iostream>

// ----- Recursion -----
// method to find factorial of given number.
unsigned long long int factorialUsingRecursion(int n)
{
    if (n == 0) // Base case.
        return 1;
    return n * factorialUsingRecursion(n - 1); // Recursion call
}

// ----- Iteration -----
// Method to find the factorial of a given number.
unsigned long long int factorialUsingIteration(int n)
{
    unsigned long long int res = 1, i;
    for (i = 2; i <= n; i++) // Using iteration.
        res *= i;
    return res;
}

// Driver method.
int main()
{
    unsigned long long int num;

    std::cout << "Enter a number to find the factorial: ";
    std::cin >> num;

    std::cout << "Factorial of " << num << " using Recursion is: " << factorialUsingRecursion(num) << "\n";
    std::cout << "Factorial of " << num << " using Iteration is: " << factorialUsingIteration(num);

    return 0;
}
