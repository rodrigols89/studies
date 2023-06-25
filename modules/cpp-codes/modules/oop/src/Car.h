<<<<<<< HEAD:modules/cpp-codes/modules/oop/src/Car.h
#include <string>
using std::string;

class Car
{
private:
    // Encapsulation.
    int color;
    string type;
    float velocity;

public:
    // Interfaces.
    void turnOn();
    void turnOff();
    void speed();
    void brake();
};
=======
#include <string>

class Car
{
private:
    // Encapsulation.
    int color;
    std::string type;
    float velocity;

public:
    // Interfaces.
    void turnOn();
    void turnOff();
    void speed();
    void brake();
};
>>>>>>> cpp-codes:modules/cpp-codes/modules/oop/classes/src/Car.h
