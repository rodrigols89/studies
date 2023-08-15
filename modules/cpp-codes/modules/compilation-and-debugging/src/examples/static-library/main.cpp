#include <iostream>
#include <SDL2/SDL.h> // Inclua o cabeçalho da SDL
#include "userdata.h"

int main()
{
    if (SDL_Init(SDL_INIT_VIDEO) != 0)
    {
        std::cerr << "SDL initialization failed: " << SDL_GetError() << std::endl;
        return 1;
    }

    UserData userData;
    userData.captureUserData();
    userData.saveToFile("userdata.txt");

    SDL_Quit();
    return 0;
}
