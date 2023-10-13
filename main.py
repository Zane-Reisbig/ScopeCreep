import keyboard
import mouse
import pytesseract
import PIL
import os
from time import sleep

from screenReading import screenReading
from windowHandlers import facetsWindowHandler
from stateManager.stateManager import StateManager
from stateManager.types import WindowSizes, MainWindowTabs


def main():
    tessPath = poorMansEnv("tessPath")
    myManager = StateManager()

    out = facetsWindowHandler.check_if_duplicate(tessPath, WindowSizes.large, myManager)

    sleep(1)
    facetsWindowHandler.activate_duplicate_claim_tab(WindowSizes.large, myManager)
    sleep(1)
    facetsWindowHandler.activate_line_item_tab(WindowSizes.large, myManager)

    print(out)


def getRect():
    screenReading.create_rectangle_from_two_clicks({"copyToClipboard": True})


def poorMansEnv(key):
    # I can't get the whl of dotenv to install on my venv so here we are

    folderPath = os.path.dirname(os.path.abspath(__file__))
    filePath = os.path.join(folderPath, ".env")

    with open(filePath, "r") as f:
        lines = f.readlines()
        for line in lines:
            if line.startswith(key):
                return line.split("=")[1].strip().strip('"')
        return None


main()
