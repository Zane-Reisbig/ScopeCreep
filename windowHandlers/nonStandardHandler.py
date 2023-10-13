import PIL.Image as Image
import pyautogui as pag


def center_on_image(image: Image, click: bool = None, options: object = None) -> bool|tuple:
    """
    Centers the mouse on the anchor of an image
    :param image: the image to center on
    :param click:? whether or not to click on the anchor
    :param options:? {
        "confidence": float,
        "returnCoords": bool
    }
    :return: default - whether or not the image was found
             click                  = True - whether or not the image was found and clicked
             options["returnCoords"]= True - the coordinates of the image 
    """
    if options is None:
        options = {"confidence": 0.8}

    x, y = pag.locateCenterOnScreen(
        image, grayscale=True, confidence=options["confidence"]
    )
    
    if x is None or y is None:
        return False

    pag.moveTo(x, y)
    if click:
        pag.click()
    
    if options["returnCoords"]:
        return (x, y)
    
    return True
