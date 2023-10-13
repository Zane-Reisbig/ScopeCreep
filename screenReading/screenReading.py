import mouse
import keyboard
import pytesseract
import pyperclip
from PIL import Image, ImageGrab


def capture_window_area(rectangle: tuple) -> Image:
    """
    Captures a window area and returns it as an Image object.
    :rectangle: A tuple containing the coordinates of the window area.
    :return: An Image object containing the window area.
    """
    return ImageGrab.grab(bbox=rectangle)


def get_text_from_image(image: Image, pytessPath: str) -> str:
    """
    Gets the text from an Image object.
    :image: An Image object.
    :return: A string containing the text from the image.
    """
    pytesseract.pytesseract.tesseract_cmd = pytessPath
    return pytesseract.pytesseract.image_to_string(image, config="--psm 7")


def get_text_from_rectangle(
    rectangle: tuple, pytessPath: str, debug: object = None
) -> str:
    """
    Gets the text from a window area.
    :rectangle: A tuple containing the coordinates of the window area.
    :return: A string containing the text from the window area.
    :debug:? {
        "savePicture": bool,
    }

    """
    if debug:
        if debug["savePicture"]:
            image = capture_window_area(rectangle)
            image.save(f"getTextFromRec{rectangle[0]}{rectangle}{rectangle[2]}.png")

    image = capture_window_area(rectangle)
    return get_text_from_image(image, pytessPath)


def create_rectangle_from_two_clicks(options: object) -> tuple:
    """
    Creates a rectangle from two clicks.
    :return: A tuple containing the coordinates of the rectangle.
    :options:? {
        "copyToClipboard": Bool,
    }
    """

    print("Click the top left corner of the rectangle.")
    mouse.wait()
    currentPosition = mouse.get_position()
    mouse.wait()

    print("Click the bottom right corner of the rectangle.")
    mouse.wait()
    currentPosition2 = mouse.get_position()
    mouse.wait()

    if options:
        if options["copyToClipboard"]:
            pyperclip.copy(
                f"var = ({currentPosition[0]}, {currentPosition}, {currentPosition2[0]}, {currentPosition2})"
            )
