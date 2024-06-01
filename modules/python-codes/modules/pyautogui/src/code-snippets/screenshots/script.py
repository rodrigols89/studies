import pyautogui
import keyboard
import time
import os


def take_screenshot(count):
    # Define the path to save the screenshot
    screenshot_name = f"source-here/{count:03}.png"

    # Create directories if they don't exist
    os.makedirs(os.path.dirname(screenshot_name), exist_ok=True)

    # Save the screenshot
    pyautogui.screenshot().save(screenshot_name)
    print(f"Screenshot saved as {screenshot_name}")


def main():
    count = 1
    while True:
        print("Program running...", end="\r")
        if keyboard.is_pressed("esc"):
            print("'ESC' pressed...")
            take_screenshot(count)
            count += 1
            time.sleep(1)  # Small pause to avoid multiple captures at once
        elif keyboard.is_pressed("F1"):
            print("'F1' pressed...")
            print("Exiting the program.")
            # Clean the CLI.
            if os.name == "nt":  # Windows
                os.system("cls")
            else:  # Unix (Linux and macOS)
                os.system("clear")
            break


if __name__ == "__main__":
    main()
