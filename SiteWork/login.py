import pyautogui
import time
import webbrowser
import config
from SiteWork import routeNew

def StartGame():
    webbrowser.open('https://www.rail-nation.com')
    time.sleep(3)
    pyautogui.click(x=100, y=200)
    time.sleep(2)

    pyautogui.typewrite(config.LOGIN)  # Login
    pyautogui.press('tab')
    pyautogui.typewrite(config.PASSWORD)  # Password
    pyautogui.press('enter')

    time.sleep(10)
    routeNew.ClickGame()
