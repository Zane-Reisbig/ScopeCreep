from typing import TypedDict


class Options(TypedDict):
    """
    kwarg options for windowHandlers
    confidence: float = 0.8
    returnCoords: bool = False
    """
    
    confidence : float
    returnCoords : bool