import mouse
import keyboard
import pytesseract
import pyscreenshot
import pyperclip
from PIL import Image


def capture_window_area(rectangle: tuple) -> Image:
    """
    Captures a window area and returns it as an Image object.
    :param rectangle: A tuple containing the coordinates of the window area.
    :return: An Image object containing the window area.
    """
    return pyscreenshot.grab(bbox=rectangle)


def get_text_from_image(image: Image, py_tess_path: str) -> str:
    """
    Gets the text from an Image object.
    :param image: An Image object.
    :return: A string containing the text from the image.
    """
    pytesseract.pytesseract.tesseract_cmd = py_tess_path
    return pytesseract.pytesseract.image_to_string(image, config="--psm 7")


def get_text_from_rectangle(
    rectangle: tuple, py_tess_path: str, debug: object = None
) -> str:
    """
    Gets the text from a window area.
    :param rectangle: A tuple containing the coordinates of the window area.
    :return: A string containing the text from the window area.
    :op debug: {
        "savePicture": Bool,
    }

    """
    if debug:
        if debug["savePicture"]:
            image = capture_window_area(rectangle)
            image.save(f"getTextFromRec{rectangle[0]}{rectangle[1]}{rectangle[2]}.png")

    image = capture_window_area(rectangle)
    return get_text_from_image(image, py_tess_path)


def create_rectangle_from_two_clicks(debug: object) -> tuple:
    """
    Creates a rectangle from two clicks.
    :return: A tuple containing the coordinates of the rectangle.
    :op debug: {
        "copyToClipboard": Bool,
    }
    """

    print("Click the top left corner of the rectangle.")
    mouse.wait()
    current_position = mouse.get_position()
    mouse.wait()

    print("Click the bottom right corner of the rectangle.")
    mouse.wait()
    current_position2 = mouse.get_position()
    mouse.wait()

    if debug:
        if debug["copyToClipboard"]:
            pyperclip.copy(
                f"var = ({current_position[0]}, {current_position[1]}, {current_position2[0]}, {current_position2[1]})"
            )
