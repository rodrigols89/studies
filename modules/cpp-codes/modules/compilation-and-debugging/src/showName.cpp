#include <iostream>
#include <string>
#include <sstream>

std::string showName(const int &age, const std::string &name)
{
    std::ostringstream ss;
    ss << "Name: " << name << ", Age: " << age;
    return ss.str();
}

int main()
{
    int age = 30;
    std::string name = "Rodrigo";

    std::string result = showName(age, name);
    std::cout << result << "\n";
    return 0;
}
