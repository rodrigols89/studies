import pyautogui

dota2Object = None

while dota2Object is None:
    try:
        dota2Object = pyautogui.locateOnScreen("../images/dota2.png", confidence=0.75)
        if dota2Object:
            print("Image found on the screen:", dota2Object)
            x_coordinate, y_coordinate = pyautogui.center(dota2Object)
            pyautogui.click(x=x_coordinate, y=y_coordinate, duration=1, clicks=2)
        else:
            print("Image not found on the screen.")
    except Exception as e:
        print(f"Error while trying to locate the image: {e}")
        break
