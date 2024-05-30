from time import sleep
import pyautogui

sleep(5)
pyautogui.hotkey('ctrl', 'a') # ctrl - a to select all.
pyautogui.hotkey('ctrl', 'c') # ctrl - c to copy.
pyautogui.hotkey('ctrl', 'v') # ctrl - v to paste.
