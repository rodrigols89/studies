#pragma once
#include <string>
using std::string;

class Game
{
private:
	// Encapsulation.
	string name;                                        // Game name.
	float price;                                        // Game price.
	int hours;                                          // Hours played.
	float cost;                                         // Cost per hour player.

	// Calculate the cost to played hours (Inline function/Method).
	void calculate() { if (hours > 0) cost = price / hours; }

public:
	// Interfaces.
	void purchase(const string& title, float value);    // Fill the information.
	void update(float value);                           // Update game price.
	void play(int time);                                // Record (save) the hours played.
	void showInformation();                             // show information.
};
