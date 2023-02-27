#include <iostream>
#include "bus.h"
#include "car.h"
#include "truck.h"

int main()
{
    Bus bus;
    std::cout << "'Bus' object examples:"
              << "\n";
    bus.fuelAmount();
    bus.capacity();
    bus.applyBrakes();

    Car car;
    std::cout << "\n'Car' object examples:"
              << "\n";
    car.fuelAmount();
    car.capacity();
    car.applyBrakes();

    Truck truck;
    std::cout << "'\nTruck' object examples:"
              << "\n";
    truck.fuelAmount();
    truck.capacity();
    truck.applyBrakes();

    return 0;
}
