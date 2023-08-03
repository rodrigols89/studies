from time import sleep

import pyautogui

sleep(5)

# 99% confidence.
windowsMenuObject = pyautogui.locateOnScreen("../images/windows-menu.png", confidence=0.99)
try:
    while True:
        print(windowsMenuObject)
except KeyboardInterrupt:
    print("\n")
