#include "derived.h"

int main()
{
    Derived derived_obj;
    derived_obj.print();       // Access print() method in derived class.

    derived_obj.Base::print(); // Access print() method in base class.

    return 0;
}
