#include "GameWithConstructor.h"

int main()
{
	Game gow = { "Gears", 50.0f };

	// Call methods of Game (gow) object.
	gow.showInformation();

	// Call methods of Game (gow) object.
	gow.play(5);
	gow.showInformation();

	// Call methods of Game (gow) object.
	gow.play(3);
	gow.showInformation();
}
