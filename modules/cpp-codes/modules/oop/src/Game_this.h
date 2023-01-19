#pragma once
#include <string>
using std::string;

class Game
{
private:
    // Encapsulation.
    string name; // Game name.
    float price; // Game price.
    int hours;   // Hours played.
    float cost;  // Cost per hour player.

    // Calculate the cost to played hours (Inline function/Method).
    void calculate()
    {
        if (this->hours > 0)
            this->cost = this->price / this->hours;
    }

public:
    // Interfaces.
    Game(const string &name, float cost = 0); // Constructor prototype.
    void update(float cost);                  // Update game price.
    void play(int hours);                     // Record (save) the hours played.
    void showInformation();                   // show information.
};
