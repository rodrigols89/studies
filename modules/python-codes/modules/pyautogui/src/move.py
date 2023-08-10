import pyautogui

pyautogui.moveTo(100, 200, 2)  # moves the mouse to X = 100, Y = 200 over 2 seconds.
pyautogui.move(0, 50, 2)       # move  the mouse down 50 pixels over 2 seconds.
pyautogui.move(-30, 0, 2)      # move  the mouse left 30 pixels over 2 seconds.
pyautogui.move(-30, None, 2)   # move  the mouse left 30 pixels over 2 seconds.
