import keyboard
import pyautogui
import actions

if __name__ == "__main__":
    print("Press 'Insert' to start the script...")
    keyboard.wait("insert")

    try:
        # Game Loop.
        while True:
            if actions.checkIfTheBattleIsOpen():
                print("Battle found...")
                pyautogui.sleep(1)
                # If the return is None, has monster on the battle.
                while actions.checkIfTheBattleIsEmpty() == None:
                    print("Monster found...")
                    pyautogui.press("1")  # Active chatoff.
                    pyautogui.press("2")  # Atk the target.
                    pyautogui.sleep(1)
                    while actions.checkIfTheTargetIsclicked(conf=0.7):
                        print("Killing a monster...")
                        pyautogui.sleep(1)
                    actions.checkLoot()
            else:
                print("Plese, open the Battle list...")
                pyautogui.sleep(1)
    except KeyboardInterrupt:
        print("", end=" ")
