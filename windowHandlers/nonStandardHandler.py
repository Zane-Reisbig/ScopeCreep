import PIL.Image as Image
import pyautogui as pag


def center_on_image(image: Image, click: bool = None, options: object = None) -> bool|tuple:
    """
    Centers the mouse on the anchor of an image
    :param image: the image to center on
    :param click:? whether or not to click on the anchor
    :param options:? {
        "confidence": float = 0.8,
        "returnCoords": bool = False,
    }
    :return: default - whether or not the image was found
             click                  = True - whether or not the image was found and clicked
             options["returnCoords"]= True - the coordinates of the image 
    """
    if options is None:
        options = {"confidence": 0.8, "returnCoords": False}
    elif "confidence" not in options:
        options["confidence"] = 0.8
    elif "returnCoords" not in options:
        options["returnCoords"] = False

    
    hasCV2 = False
    try:
        import cv2
        hasCV2 = True
    except:
        print("OpenCV is not installed, cannot use 'confidence' option")
        
    if hasCV2:
        x, y = pag.locateCenterOnScreen(image, grayscale=True, confidence=options["confidence"])
    else:
        x, y = pag.locateCenterOnScreen(image, grayscale=True)

    
    if x is None or y is None:
        return False

    pag.moveTo(x, y)
    if click:
        pag.click()
    
    if options and options["returnCoords"]:
        return (x, y)
    
    return True
