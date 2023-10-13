import PIL.Image as Image
import pyautogui as pag


def center_on_image(image: Image, click: bool = None, options: object = None):
    """
    Centers the mouse on the anchor of an image
    :param image: the image to center on
    :?param click: whether or not to click on the anchor
    :?param options: {
        "confidence": float,
    }
    :return: None
    """
    if options is None:
        options = {"confidence": 0.8}

    x, y = pag.locateCenterOnScreen(
        image, grayscale=True, confidence=options["confidence"]
    )
    pag.moveTo(x, y)
    if click:
        pag.click()
