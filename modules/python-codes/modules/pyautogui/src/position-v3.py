import pyautogui

print('Press Ctrl-C to quit.')
try:
    while True:
        current_mouse_position = pyautogui.position()
        print(current_mouse_position)
except KeyboardInterrupt:
    print('\n')
