############################ ( Game Code ) ############################

"""     try:
        # Game Loop.
        while True:
            if checkIfTheBattleIsOpen():
                print("Battle found...")
                sleep(1)
                # If the return is None, has monster on the battle.
                while checkIfTheBattleIsEmpty() == None:
                    print("Monster found...")
                    pyautogui.press("1")  # Active chatoff.
                    pyautogui.press("2")  # Atk the target.
                    sleep(1)
                    while checkIfTheTargetIsclicked(conf=0.7):
                        print("Killing a monster...")
                        sleep(1)
            else:
                print("Plese, open the Battle list...")
                sleep(1)
    except KeyboardInterrupt:
        print("", end=" ") """





############################ ( Test code ) ############################


"""     try:
        while True:
            # Test checkIfTheBattleIsOpen()
            test_battleIsOpen = checkIfTheBattleIsOpen()
            if test_battleIsOpen:
                print("Battle coordinates:", test_battleIsOpen)
                sleep(1)
            else:
                print("Battle does not found:", test_battleIsOpen)
                sleep(1)

            # Test checkIfTheBattleIsEmpty()
            test_battleIsEmpty = checkIfTheBattleIsEmpty()
            if test_battleIsEmpty:
                print("Battle is empty:", test_battleIsEmpty)
                sleep(1)
            else:
                print("Has monter on the battle:", test_battleIsEmpty)
                sleep(1)

            # Test checkIfTheTargetIsclicked()
            test_target = checkIfTheTargetIsclicked(conf=0.7)
            if test_target:
                print("Killing a monster on:", test_target)
                sleep(1)
            else:
                print("No target clicked:", test_target)
                sleep(1)
    except KeyboardInterrupt:
        print("")
 """


"""     while True:
        lootStatus = checkLoot()
        print(lootStatus)
        pyautogui.sleep(1)
        if lootStatus:
            for loot in lootStatus:
                print(loot) """


############################ ( Complete Codes ) ############################

import pyautogui
import keyboard

LOOT_REGION = (738, 354, 217, 199)


def checkIfTheBattleIsOpen(reg=None, conf=0.9):
    box = pyautogui.locateOnScreen(
        "assets/checkIfTheBattleIsOpen.png", region=reg, confidence=conf
    )
    if box:
        coordinates = (box.left, box.top, box.width, box.height)
        return coordinates
    else:
        return box


def checkIfTheBattleIsEmpty(reg=None, conf=0.9):
    box = pyautogui.locateOnScreen(
        "assets/checkIfTheBattleIsEmpty.png", region=reg, confidence=conf
    )
    if box:
        coordinates = (box.left, box.top, box.width, box.height)
        return coordinates
    else:
        return box


def checkIfTheTargetIsclicked(reg=None, conf=0.9):
    box = pyautogui.locateOnScreen(
        "assets/checkIfTheTargetIsclicked.png", confidence=conf
    )
    if box:
        coordinates = (box.left, box.top, box.width, box.height)
        return coordinates
    else:
        return box


def checkLoot(reg=None, conf=0.9):
    """
    NOTE:
    Para executar essa função, primeiro você deve remove os logs:
     - No OBS:
         - Remova "capturar cursor".
     - No Tibia:
         - Clique em settings > Interface > Game Window > [Remove as 2 primeiras opções]
         - Por fim, aperte CTRL+n para remove o nome dos personagens.

    A função locateAllOnScreen() sempre retorna uma lista com todas as imagens
    referente a busca, diferente the locateOnScreen() que só retorna uma opção.

    Ela sempre retorna um iterator (list) mesmo que ele não encontre nada.
    Ou seja, não retorna None se não encontrar.

    Para testar:

        loots_list = pyautogui.locateAllOnScreen()
        for loot in loots_list:
            print(loot)

        <generator object _locateAll_opencv at 0x000001620C1ED4E0>
        Box(left=909, top=442, width=27, height=15)
        Box(left=782, top=443, width=27, height=15)
        Box(left=909, top=443, width=27, height=15)
        Box(left=781, top=506, width=27, height=15)
        Box(left=782, top=506, width=27, height=15)
        Box(left=845, top=506, width=27, height=15)
        Box(left=846, top=506, width=27, height=15)
    """
    loots_list = pyautogui.locateAllOnScreen(
        "assets/wasp-loot.png", region=LOOT_REGION, confidence=conf
    )
    for loot in loots_list:
        x, y = pyautogui.center(loot)
        pyautogui.click(x=x, y=y, button="right", clicks=2, duration=1)


if __name__ == "__main__":
    print("Press 'Insert' to start the script...")
    keyboard.wait("insert")

    checkLoot()

"""     try:
        # Game Loop.
        while True:
            if checkIfTheBattleIsOpen():
                print("Battle found...")
                pyautogui.sleep(1)
                # If the return is None, has monster on the battle.
                while checkIfTheBattleIsEmpty() == None:
                    print("Monster found...")
                    pyautogui.press("1")  # Active chatoff.
                    pyautogui.press("2")  # Atk the target.
                    pyautogui.sleep(1)
                    while checkIfTheTargetIsclicked(conf=0.7):
                        print("Killing a monster...")
                        pyautogui.sleep(1)
            else:
                print("Plese, open the Battle list...")
                pyautogui.sleep(1)
    except KeyboardInterrupt:
        print("", end=" ") """
