from constants import LOOT_REGION

import pyautogui


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
        pyautogui.click(x=x, y=y, button="right", clicks=2, duration=0.1)
    pyautogui.moveTo(x=30, y=60)  # Tira o mouse da frente do loot.
