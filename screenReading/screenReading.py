import mouse
import keyboard
import pytesseract
import pyperclip
import pyautogui

from .options import (
    TextFromImageOptions,
    RectangleFromTwoClicksOptions,
    TextFromRectangleOptions,
)

from PIL import Image, ImageGrab

# from options import textFromImageOptions, textFromRectangleOptions, rectangleFromTwoClicksOptions


def capture_window_area(
    rectangle: tuple, options: TextFromImageOptions = None
) -> Image:
    """
    Captures a window area and returns it as an Image object.
    :rectangle: A tuple containing the coordinates of the window area.
    :return: An Image object containing the window area.
    """
    savePicture = _get_config(options, "savePicture", False)
    if savePicture:
        image = capture_window_area(rectangle)
        imageName = _get_config(options, "savePictureName", "capture_window_area.png")
        if imageName:
            image.save(imageName)
        else:
            image.save(f"getTextFromRec{rectangle[0]}{rectangle}{rectangle[2]}.png")
    return ImageGrab.grab(bbox=rectangle)


def _get_config(options: object, key: str, default) -> object:
    """
    Gets a config value from the options object.
    :options: An object containing options.
    :key: The key of the config value.
    :default: The default value if the key is not found.
    :return: The value of the config.
    """
    if options:
        if key in options:
            return options[key]
    return default


def get_text_from_image(
    image: Image, pytessPath: str, options: TextFromImageOptions = None
) -> str:
    """
    Gets the text from an Image object.
    :image: An Image object.
    :options:? An object containing options/kwargs.
    :return: A string containing the text from the image.
    """
    psmValue = _get_config(options, "psm", 7)
    pytesseract.pytesseract.tesseract_cmd = pytessPath
    return pytesseract.pytesseract.image_to_string(image, config=f"--psm {psmValue}")


def get_text_from_rectangle(
    rectangle: tuple, pytessPath: str, options: TextFromRectangleOptions = None
) -> str:
    """
    Gets the text from a window area.
    :rectangle: A tuple containing the coordinates of the window area.
    :pytessPath: The path to the pytesseract executable.
    :options:? An object containing options/kwargs.
    :return: A string containing the text from the window area.
    """

    savePicture = _get_config(options, "savePicture", False)
    if savePicture:
        image = capture_window_area(rectangle)
        image.save(f"getTextFromRec{rectangle[0]}{rectangle}{rectangle[2]}.png")

    image = capture_window_area(rectangle)
    return get_text_from_image(image, pytessPath)


def create_rectangle_from_two_clicks(
    options: RectangleFromTwoClicksOptions = None,
) -> tuple:
    """
    Creates a rectangle from two clicks.
    :return: A tuple containing the coordinates of the rectangle.
    :options:? An object containing options/kwargs.
    :return: A tuple containing the coordinates of the rectangle.
    """

    print("Click the top left corner of the rectangle.")
    mouse.wait()
    currentPosition = mouse.get_position()
    mouse.wait()

    print("Click the bottom right corner of the rectangle.")
    mouse.wait()
    currentPosition2 = mouse.get_position()
    mouse.wait()

    copyToClipboard = _get_config(options, "copyToClipboard", False)
    if copyToClipboard:
        pyperclip.copy(
            f"var = ({currentPosition[0]}, {currentPosition[0]}, {currentPosition2[0]}, {currentPosition2[0]})"
        )


def image_matches_known_active_window_state(
    activeImage: Image, currentWindowCoords: tuple
):
    """
    if window cannot be verifed thru code whether pyautogui, pywinauto or other
    last resort is to take a screenshot of an "anchor" state while the window is
    active. Then compare that image to the current window image. If they match
    then the window is active. (in theroy)

    :activeImage: Image object of the known active state
    :currentWindowCoords: tuple of the current window coordinates, matching the activeImage
    """

    currentWindowImage = capture_window_area(currentWindowCoords)
    return pyautogui.locate(activeImage, currentWindowImage, confidence=0.9)
