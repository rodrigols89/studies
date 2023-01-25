#include <iostream>

int main()
{
    std::string cat = "Myke";
    std::string &animal = cat;

    std::cout << "\nThe name of the 'cat' is: " << cat << "\n";
    std::cout << "The Memory Address of 'cat' variable is: " << &cat << "\n";
    std::cout << "The name of the 'animal' is: " << animal << "\n";
    std::cout << "The Memory Address of 'animal' variable reference is: " << &animal << "\n";

    animal = "Jhon";

    std::cout << "\nThe name of the 'cat' is: " << cat << "\n";
    std::cout << "The Memory Address of 'cat' variable is: " << &cat << "\n";
    std::cout << "The name of the 'animal' is: " << animal << "\n";
    std::cout << "The Memory Address of 'animal' variable reference is: " << &animal << "\n";

    return 0;
}
