#include <iostream>

// Recursive function.
void Geek(int N)
{
    if (N == 0) // Base case.
        return;
    std::cout << N << " "; // Print the current value of "N".
    Geek(N - 1);           // Call itself recursively.
}

// Driver code.
int main()
{
    int N = 5; // Initial value of "N".
    Geek(N);   // Call the recursive function.

    return 0;
}
