import pyautogui

# 75% confidence.
dota2Object = pyautogui.locateOnScreen("../images/dota2.png", confidence=0.75)
x_coordinate, y_coordinate = pyautogui.center(dota2Object)

pyautogui.click(
    x=x_coordinate, y=y_coordinate, duration=1, clicks=2
)  # double-click the left mouse button.
