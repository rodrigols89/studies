# Programming for Windows

## Contents

 - [WinMain() function](#winmain)
 - [MessageBox function (winuser.h)](#message-box-function)
 - **Examples:**
   - [Simple CreateWindow example](#cw-01)
 - **Tips & Tricks:**
   - [Hungarian Notation](#hn-w)

---

<div id="winmain"></div>

## WinMain() function

 - **WinMain():**
   - **WinMain()** is the *entry point for every Windows program*.
   - just (assim) as **main()** is the *entry point for console programs in text mode*.
 - **APIENTRY:**
   - Tells to the compiler how to pass arguments to **WinMain()** function.
 - **`_In_` and `_In_opt_`:**
   - They are part of Microsoft's source code annotations language​
 - **WinMain() parameters:**
   - **HINSTANCE hInstance:**
     - *hInstance* is something called a "handle to an instance" or "handle to a module." The operating system uses this value to identify the executable (EXE) when it is loaded in memory. The instance handle is needed for certain Windows functions—for example, to load icons or bitmaps.
     - A handle (identificador) to the current instance of the application.
   - **HINSTANCE hPrevInstance:**
     - *hPrevInstance* has no meaning. It was used in 16-bit Windows, but is now always zero.
     - A handle (identificador) to the previous instance of the application.
     - This parameter is always *NULL*.
     - If you need to detect whether another instance already exists, create a uniquely named mutex using the [CreateMutex](https://learn.microsoft.com/en-us/windows/win32/api/synchapi/nf-synchapi-createmutexa) function.
   - **LPSTR lpCmdLine:**
     - The command line for the application, excluding the program name.
   - **int nCmdShow:**
     - Defines how the program should be started *(maximized, minimized, full screen)​*.

You can see a simple Window with Windows API below:

[HelloMsg.cpp](src/HelloMsg.cpp)
```cpp
#include <windows.h>

int APIENTRY WinMain(_In_ HINSTANCE hInstance,
                     _In_opt_ HINSTANCE hPrevInstance,
                     _In_ LPSTR lpCmdLine,
                     _In_ int nCmdShow)
{
    MessageBox(NULL, "Msg here...", "Title here...", 0);
    return 0;
}
```

**COMPILATION AND RUN:**
```cpp
g++ HelloMsg.cpp -o MyFirstWindow

./MyFirstWindow
```

[You can see all WinMain() function settings here...](https://learn.microsoft.com/en-us/windows/win32/learnwin32/winmain--the-application-entry-point)

---

<div id="message-box-function"></div>

## MessageBox function (winuser.h)

The **MessageBox() function** displays a modal dialog box that contains:

 - System icon.
 - Set of buttons.
 - And a brief application-specific message:
   - Such as status or error information.

> **NOTE:**  
> The message box returns an integer value that indicates which button the user clicked.

[You can see all MessageBox() function settings here...](https://learn.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-messagebox)

But, to practice see the example below:

[MsgBox.cpp](src/MsgBox.cpp)
```cpp
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
```

**COMPILATION AND RUN:**
```cpp
g++ MsgBox.cpp -o checkScreenSize

./checkScreenSize
```

---

<div id="cw-01"></div>

## Simple CreateWindow example

[WinProc.h](src/WinProc.h)
```cpp
#pragma once

// Prorotype to window procedure (WinProc).
LRESULT CALLBACK WinProc(HWND, UINT, WPARAM, LPARAM);
```

[WinProc.cpp](src/WinProc.cpp)
```cpp
// Set to ignore 16 bits resources from <windows.h>.
#define WIN32_LEAN_AND_MEAN
#include <windows.h>

#include "WinProc.h"


// procedimento da janela
LRESULT CALLBACK WinProc(HWND hwnd,
                         UINT message,
                         WPARAM wParam,
                         LPARAM lParam)
{
    HDC hdc;
    PAINTSTRUCT ps;
    RECT rect;

    switch (message)
    {
    case WM_PAINT:
        hdc = BeginPaint(hwnd, &ps);

        GetClientRect(hwnd, &rect);
        DrawText(hdc, "Hello Window!", -1, &rect, DT_SINGLELINE | DT_CENTER | DT_VCENTER);

        EndPaint(hwnd, &ps);
        return 0;

    case WM_DESTROY:
        PostQuitMessage(0);
        return 0;
    }
    return DefWindowProc(hwnd, message, wParam, lParam);
}
```

[ProgWindows.cpp](src/ProgWindows.cpp)
```cpp
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
```

**COMPILATION AND RUN:**
```cpp
g++ WinProc.cpp ProgWindows.cpp -o window -lgdi32

./window
```

**NOTE:**  
 - We used **"-lgdi32"** to say to the program add *DLL* to our program.
 - [You can see on StackOverflow why...](https://stackoverflow.com/questions/1340824/undefined-reference-to-getstockobject4#comment105944965_1340836)

---

<div id="hn-w"></div>

## Hungarian Notation

> Windows uses a naming convention of variables known as **Hungarian Notation**.

For example:

![img](images/hungarian-notation.png)  

---

**REFERENCES:**  
[Programação de Jogos | C++ | DirectX | Aula 01 - Programação Windows | Criar Janelas | API Win32](https://www.youtube.com/watch?v=NGoOrH-3tAc)  

---

Ro**drigo** **L**eite da **S**ilva - **drigols**
