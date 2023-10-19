import keyboard
import mouse
import pytesseract
import os
from time import sleep
from PIL import Image, ImageGrab

from screenReading import screenReading
from stateManager.stateManager import StateManager
from stateManager.types import WindowSizes, MainWindowTabs


if __name__ == "__main__":

    def main():
        # full screen vs code application
        # obv you wouldnt have the bbox and you would use a saved image
        # however for the sake of testing, and useability, this works
        vsCodeFileTabRect = (36, 0, 70, 28)

        tessPath = poorMansEnv("tessPath")
        myManager = StateManager(
            {"afterFunctionActions": [lambda: sleep(1), lambda: print("done")]}
        )

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
    # getRect()
