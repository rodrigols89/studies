#include <iostream>

#include "animal.h"
#include "dog.h"
#include "cat.h"
#include "print.h"

int main()
{
    Animal *animal_obj = new Animal();
    Animal *dog_obj = new Dog();
    Animal *cat_obj = new Cat();

    print_type(animal_obj);
    print_type(dog_obj);
    print_type(cat_obj);

    return 0;
}
