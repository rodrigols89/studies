#include "Game_this.h"

int main()
{
	Game gears = { "Gears", 50.0f };

    // Call methods of Game (gow) object.
	gears.showInformation();

	// Call methods of Game (gow) object.
	gears.play(5);
	gears.showInformation();

	// Call methods of Game (gow) object.
	gears.play(3);
	gears.showInformation();
}
