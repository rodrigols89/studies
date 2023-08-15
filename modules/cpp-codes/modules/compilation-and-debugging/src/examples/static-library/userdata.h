#ifndef USERDATA_H
#define USERDATA_H

#include <SDL2/SDL.h> // Inclua o cabeçalho da SDL

class UserData
{
public:
    UserData();
    void captureUserData();
    void saveToFile(const char *filename);

private:
    std::string name;
    std::string password;
};

#endif // USERDATA_H
