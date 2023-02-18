#include <string>

class Game
{
private:
    // Encapsulation.
    std::string name; // Game name.
    float price;      // Game price.
    int hours;        // Hours played.
    float cost;       // Cost per hour player.

    inline void calculate(); // Prototype.

public:
    // Interfaces.
    void purchase(const std::string &title, float value); // Fill the information.
    void update(float value);                             // Update game price.
    void play(int time);                                  // Record (save) the hours played.
    void showInformation();                               // show information.
};

// Calculate the cost to played hours (Inline function/Method).
void Game::calculate() { if (hours > 0) cost = price / hours; }
