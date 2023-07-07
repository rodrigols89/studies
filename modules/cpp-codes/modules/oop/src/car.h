// updated: 06/07/2023
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
