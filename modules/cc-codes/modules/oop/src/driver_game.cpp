#include "Game.h"

int main()
{
	Game gow; // Variable of type "Game".

	// Call methods of Game (gow) object.
	gow.purchase("Gow", 160.0f);
	gow.showInformation();

	// Call methods of Game (gow) object.
	gow.play(5);
	gow.showInformation();

	// Call methods of Game (gow) object.
	gow.play(3);
	gow.showInformation();
}
