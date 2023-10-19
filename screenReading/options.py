from typing import TypedDict


class Options(TypedDict):
    psm: int
    copyToClipboard: bool
    savePictureName: str | None
    savePicture: bool
    confidence: float
    returnCoords: bool


class TextFromImageOptions(Options):
    psm: int


class TextFromRectangleOptions(Options):
    savePictureName: str | None
    savePicture: bool


class RectangleFromTwoClicksOptions(Options):
    copyToClipboard: bool
