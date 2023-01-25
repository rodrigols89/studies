#include <iostream>

int main()
{
    std::string cat = "Myke";
    std::string &animal = cat;
    std::string *location = &animal;

    // Get values.
    std::cout << "The name of the 'cat' is: " << cat << "\n";
    std::cout << "The name of the 'animal' is: " << animal << "\n";
    std::cout << "The name 'animal/cat' get from a pointer is: " << *location << "\n"
              << "\n";

    // Get memory addresses.
    std::cout << "The Memory Address of 'cat' variable is: " << &cat << "\n";
    std::cout << "The Memory Address of 'animal' reference is: " << &animal << "\n";
    std::cout << "The Memory Address of 'location' pointer is: " << &location << "\n";

    return 0;
}
