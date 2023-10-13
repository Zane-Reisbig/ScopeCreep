import json
import os
import sys
import mouse
import keyboard

from screenReading import screenReading

from stateManager.stateManager import StateManager
from stateManager.types import WindowSizes, MainWindowTabs


def check_if_duplicate(
    pytesspath: str, windowSize: WindowSizes, stateManager: StateManager = None
) -> bool:
    """
    Checks if the current claim is a duplicate
    :facets_handle: the handle to the facets window
    :?stateManager?: the state manager
    ___
    :stateKeys used: {
        "activeMainWindowTab",
        "isCurrentClaimDuplicate",
    }
    """

    if stateManager is not None:
        if currentState := stateManager.check_if_state_exists(
            "isCurrentClaimDuplicate"
        ):
            if currentState[1]:
                return True

    config_file = os.path.join(os.path.dirname(__file__), "config.json")
    with open(config_file, "r") as f:
        config = json.load(f)

    if stateManager is not None:
        stateManager.add_or_update_state(
            "activeMainWindowTab", MainWindowTabs.duplicate.value
        )

    activate_line_item_tab(windowSize)
    duplicate_claim_text = screenReading.get_text_from_rectangle(
        config[windowSize.value]["duplicateStaticAreaLocation"],
        pytesspath,
        # debug={"savePicture": True},
    )

    # print(duplicate_claim_text)
    return duplicate_claim_text == "CDD _ Definite Duplicate Claim\n"


def activate_line_item_tab(windowSize: WindowSizes, stateManager: StateManager = None):
    """
    Activates the line item tab
    :facets_handle: the handle to the facets window
    :?stateManager?: the state manager
    ___
    :stateKeys used: {
        "activeMainWindowTab",
    }
    """
    config_file = os.path.join(os.path.dirname(__file__), "config.json")
    with open(config_file, "r") as f:
        config = json.load(f)

    mouse.move(
        config[windowSize.value]["lineItemTabPoint"][0],
        config[windowSize.value]["lineItemTabPoint"][1],
        absolute=True,
        duration=0.1,
    )
    mouse.click(button="left")

    if stateManager is not None:
        stateManager.add_or_update_state(
            "activeMainWindowTab", MainWindowTabs.lineItem.value
        )


def activate_duplicate_claim_tab(
    windowSize: WindowSizes, stateManager: StateManager = None
):
    """
    Activates the duplicate claim tab
    :facets_handle: the handle to the facets window

    """
    config_file = os.path.join(os.path.dirname(__file__), "config.json")
    with open(config_file, "r") as f:
        config = json.load(f)

    mouse.move(
        config[windowSize.value]["duplicateTabPoint"][0],
        config[windowSize.value]["duplicateTabPoint"][1],
        absolute=True,
        duration=0.1,
    )
    mouse.click(button="left")

    if stateManager is not None:
        stateManager.add_or_update_state(
            "activeMainWindowTab", MainWindowTabs.duplicate.value
        )
