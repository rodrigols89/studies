#include <iostream>

class Base
{
public:
    virtual void print()
    {
        std::cout << "Base function called\n";
    }
};

class Derived : public Base
{
public:
    void print()
    {
        std::cout << "Derived function called\n";
    }
};

int main()
{
    Derived derived_obj;
    Base *base_obj_pointer = &derived_obj;

    base_obj_pointer->print();

    return 0;
}
