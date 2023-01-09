#pragma once
#include <string>
using std::string;

class Game
{
private:
    string m_name;
    float m_price;
    int m_hours;
    float m_cost;

    // Inline function.
    void calculate() { if (m_hours > 0) m_cost = m_price / m_hours; }

public:
    // Constructor prototype (with default parameters).
    Game(const string &name = "Gears", float price = 100, int hours = 0, float cost = 0);

    void update(float cost);
    void play(int hours);
    void showInformation();
};
