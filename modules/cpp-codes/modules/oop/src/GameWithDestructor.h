#pragma once
#include <string>
using std::string;

class Game
{
private:
    // Encapsulation.
    string m_name; // Game name.
    float m_price; // Game price.
    int m_hours;   // Hours played.
    float m_cost;  // Cost per hour player.

    // Calculate the cost to played hours (Inline function/Method).
    void calculate()
    {
        if (m_hours > 0)
            m_cost = m_price / m_hours;
    }

public:
    // Interfaces.
    Game(const string &name, float cost = 0); // Constructor prototype.
    ~Game(); // Destructor prototype.

    void update(float cost);                  // Update game price.
    void play(int hours);                     // Record (save) the hours played.
    void showInformation();                   // show information.
};
