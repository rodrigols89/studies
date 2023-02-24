#include <iostream>
#include "employee.h"

int main()
{
    Employee myObj;
    myObj.setSalary(50000);

    std::cout << "The Employee salary is: " << myObj.getSalary();

    return 0;
}
