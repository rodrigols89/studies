#include <string>

class Person
{
private:
    std::string name;
    int age;

public:
    Person(std::string name, int age); // Constructor prototype.

    // Setters
    void setName(std::string name);
    void setAge(int age);

    // Getters
    std::string getName();
    int getAge();
};
