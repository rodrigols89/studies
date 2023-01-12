// Set to ignore 16 bits resources from <windows.h>.
#define WIN32_LEAN_AND_MEAN
#include <windows.h>

#include "WinProc.h"


int APIENTRY WinMain(_In_ HINSTANCE hInstance,
                     _In_opt_ HINSTANCE hPrevInstance,
                     _In_ LPSTR lpCmdLine,
                     _In_ int nCmdShow)
{

    HWND hwnd;         // Window handle (or Window identify).
    MSG msg;           // Received message.
    WNDCLASS wndclass; // Window class.

    // Define WindowClass, called "BasicWindow".
    wndclass.style = CS_HREDRAW | CS_VREDRAW;
    wndclass.lpfnWndProc = WinProc;
    wndclass.cbClsExtra = 0;
    wndclass.cbWndExtra = 0;
    wndclass.hInstance = hInstance;
    wndclass.hIcon = LoadIcon(NULL, IDI_APPLICATION);
    wndclass.hCursor = LoadCursor(NULL, IDC_ARROW);
    wndclass.hbrBackground = (HBRUSH)GetStockObject(WHITE_BRUSH);
    wndclass.lpszMenuName = NULL;
    wndclass.lpszClassName = "BasicWindow";

    // Register WindowClass "BasicWindow".
    if (!RegisterClass(&wndclass))
    {
        // MessageBox to say user we have an error to create the Window.
        MessageBox(NULL, "Error creating window!", "Application", MB_ICONERROR);
        return 0;
    }

    // Create a Window based on "BasicWindow" class.
    hwnd = CreateWindow("BasicWindow",       // Window class.
                        "Application",       // Window title.
                        WS_OVERLAPPEDWINDOW, // Window style.
                        CW_USEDEFAULT,       // x initial position.
                        CW_USEDEFAULT,       // x initial position.
                        CW_USEDEFAULT,       // initial width.
                        CW_USEDEFAULT,       // initial height.
                        NULL,                // parent window identifier.
                        NULL,                // identificador do menu.
                        hInstance,           // menu identifier.
                        NULL);               // creation parameters.

    // Show and update the Window.
    ShowWindow(hwnd, nCmdShow);
    UpdateWindow(hwnd);

    // Handling (tratamento) messages destined for the application window.
    while (GetMessage(&msg, NULL, 0, 0))
    {
        TranslateMessage(&msg);
        DispatchMessage(&msg);
    }

    // END the Program.
    return int(msg.wParam);
}
