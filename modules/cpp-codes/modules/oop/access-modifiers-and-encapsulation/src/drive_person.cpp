#include <iostream>
#include "person.h"

int main()
{

    Person person("Rodrigo Leite da Silva", 33);

    std::cout << "Name and Age of Person passed to construct was: "
              << "\n";
    std::cout << "Person name: " << person.getName() << "\n";
    std::cout << "Person age: " << person.getAge() << "\n";

    person.setName("Sir Isaac Newton");
    person.setAge(84);
    std::cout << "\nAfter set name and age:"
              << "\n";

    std::cout << "Name: " << person.getName() << "\n";
    std::cout << "Age: " << person.getAge() << "\n";

    return 0;
}
