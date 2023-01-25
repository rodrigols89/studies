#include <iostream>

// Global variable.
int num;

// Function prototypes
int f();
int g();

int main()
{
    num = 1;
    std::cout << f() + g() + num << "\n";
}

int f()
{
    num = num + 3;
    return num;
}

int g()
{
    num = 2;
    return num;
}
