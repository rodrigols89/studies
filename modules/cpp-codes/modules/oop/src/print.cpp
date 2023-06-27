#include <iostream>
#include "print.h"

void print_type(Animal* ani) {
    std::cout << "Animal: " << ani->getType() << "\n";
}
