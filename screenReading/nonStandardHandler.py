import PIL.Image as Image
import pyautogui as pag
from .options import Options


def center_on_image(
    image: Image, click: bool = None, options: Options = None
) -> bool | tuple:
    """
    Centers the mouse on the anchor of an image
    :param image: the image to center on
    :param click:? whether or not to click on the anchor
    :param options:? options to modify and customize behavior
                    - see options.py
    :return: bool|tuple
    """
    if options is None:
        options = {"confidence": 0.8, "returnCoords": False}
    elif "confidence" not in options:
        options["confidence"] = 0.8
    elif "returnCoords" not in options:
        options["returnCoords"] = False

    try:
        import cv2

        x, y = pag.locateCenterOnScreen(
            image, grayscale=True, confidence=options["confidence"]
        )
    except:
        print("OpenCV is not installed, cannot use 'confidence' option")
        x, y = pag.locateCenterOnScreen(image, grayscale=True)

    if x is None or y is None:
        return False

    pag.moveTo(x, y)
    if click:
        pag.click()

    if options and options["returnCoords"]:
        return (x, y)

    return True
