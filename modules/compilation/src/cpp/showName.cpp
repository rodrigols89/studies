#include <iostream>
#include <string>
#include <sstream>

std::string showName(const std::string &name, const std::string &lastName)
{
    std::string msg = "Name: " + name + " " + lastName;
    return msg;
}

int main()
{
    std::string name = "Rodrigo";
    std::string lastName = "Leite";

    std::string result = showName(name, lastName);
    std::cout << result << "\n";
    return 0;
}
