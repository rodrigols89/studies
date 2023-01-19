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
