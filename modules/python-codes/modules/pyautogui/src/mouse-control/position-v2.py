import pyautogui

current_mouse_position = pyautogui.position()
print("Current mouse position: ", current_mouse_position)

x, y = current_mouse_position
print("x: ", x)
print("x type: ", type(x))
print("x: ", y)
print("x type: ", type(y))
