import pyautogui
import time


def ClickGame() -> None:
    pyautogui.click(x=910, y=714) # Play now
    time.sleep(20)
    pyautogui.click(x=1233, y=968)  # Trains menu
    time.sleep(5)
    pyautogui.click(x=1023, y=1340) # Trains menu
    time.sleep(5)
    RecomendWay()


def RecomendWay() -> None:
    pyautogui.click(x=399, y=259)  # Play now
    time.sleep(4)
    pyautogui.click(x=359, y=560)  # Trains menu
    time.sleep(4)
    pyautogui.click(x=79, y=411)
    time.sleep(4)
    pyautogui.click(x=287, y=670)
    time.sleep(4)
    pyautogui.click(x=1219, y=828)
    time.sleep(4)
    pyautogui.click(x=295, y=507)
    time.sleep(4)
    pyautogui.click(x=352, y=651)
    time.sleep(4)
    pyautogui.click(x=1381, y=909)
    time.sleep(4)
    pyautogui.click(x=240, y=640)


def NewPosition():
    try:
        while True:
            cursor_pos = pyautogui.position()

            print(cursor_pos)

            time.sleep(0.1)

    except KeyboardInterrupt:
        print("\nВыход из программы.")

