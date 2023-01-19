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
