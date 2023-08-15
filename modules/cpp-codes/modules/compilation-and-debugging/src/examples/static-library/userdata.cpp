#include <iostream>
#include <fstream>

#include "userdata.h"

UserData::UserData() {}

void UserData::captureUserData()
{
    std::cout << "Enter your name: ";
    std::cin >> name;

    std::cout << "Enter your password: ";
    std::cin >> password;
}

void UserData::saveToFile(const char *filename)
{
    std::ofstream outFile(filename);
    if (outFile.is_open())
    {
        outFile << name << ", " << password << std::endl;
        outFile.close();
        std::cout << "User data saved to " << filename << std::endl;
    }
    else
    {
        std::cerr << "Unable to open file for writing." << std::endl;
    }
}
