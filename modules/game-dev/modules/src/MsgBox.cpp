// Set to ignore 16 bits resources from <windows.h>.
#define WIN32_LEAN_AND_MEAN
#include <windows.h>

// Get <sstream> "C" library.
#include <sstream>
using std::stringstream; // "stringstream" is inside  "<sstream>" to save texts.


int APIENTRY WinMain(_In_ HINSTANCE hInstance,
                     _In_opt_ HINSTANCE hPrevInstance,
                     _In_ LPSTR lpCmdLine,
                     _In_ int nCmdShow)
{
    // Ask user if he wants to see your screen size (width and height).
    int messageBoxResponse = MessageBox(NULL,
                                        "You want to see the screen size (width and height)?", // Text for user.
                                        "Window Title...",                                     // Title.
                                        // Set yes button + set second button as default + Add question icon.
                                        MB_YESNO | MB_DEFBUTTON2 | MB_ICONQUESTION);

    // Check if the use clicked in the Button Yes (Return = 6 = IDYES)
    if (messageBoxResponse == IDYES)
    {
        // GetSystemMetrics get information from the system.
        int cxScreen = GetSystemMetrics(SM_CXSCREEN); // Get window width.
        int cyScreen = GetSystemMetrics(SM_CYSCREEN); // Get window height.

        // Create text variable.
        stringstream text;
        // Pass information to the text variable, like "cout" function.
        text << "Window dimensions: " << cxScreen << " x " << cyScreen;

        // Create a MessageBox to show the Window dimensions.
        MessageBox(NULL,
                   text.str().c_str(), // Message from "text" variable.
                   "Window dimensions",
                   // Set Ok Button + Information Icon.
                   MB_OK | MB_ICONINFORMATION);
    }
    else
    {
        MessageBox(NULL,
                   "A game must know the screen size!",
                   "Title...",
                   MB_OK | MB_ICONWARNING);
    }
    return 0;
}
