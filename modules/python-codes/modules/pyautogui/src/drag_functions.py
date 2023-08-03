import pyautogui

pyautogui.dragTo(195, 311, button='left', duration=2)     # drag mouse to X of 100, Y of 200 while holding down left mouse button.
pyautogui.dragTo(300, 400, 2, button='left', duration=2)  # drag mouse to X of 300, Y of 400 over 2 seconds while holding down left mouse button.
pyautogui.drag(30, 0, 2, button='right', duration=2)      # drag the mouse left 30 pixels over 2 seconds while holding down the right mouse button.
