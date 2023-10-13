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
    :pytesspath: the path to pytesseract
    :windowSize: the size of desktop monitor
                - config in types.py
    :stateManager:? the state manager
        :stateKeys used: {
            "activeMainWindowTab",
            "isCurrentClaimDuplicate",
        }
    :return: True if the current claim is a duplicate, False otherwise
    """

    config_file = os.path.join(os.path.dirname(__file__), "config.json")
    with open(config_file, "r") as f:
        config = json.load(f)

    activate_line_item_tab(windowSize)
    duplicate_claim_text = screenReading.get_text_from_rectangle(
        config[windowSize.value]["duplicateStaticAreaLocation"],
        pytesspath,
    )
    
    if stateManager is not None:
        if (list := stateManager.check_if_state_exists("afterFunctionActions")):
            stateManager._interpret_and_call_functionType_list(list)

        if currentState := stateManager.check_if_state_exists(
            "isCurrentClaimDuplicate"
        ):
            if currentState:
                return True

        stateManager.add_or_update_state(
            "activeMainWindowTab", MainWindowTabs.duplicate.value
        )

    return duplicate_claim_text == "CDD _ Definite Duplicate Claim\n"


def activate_line_item_tab(windowSize: WindowSizes, stateManager: StateManager = None):
    """
    Activates the line item tab
    :windowSize: the size of desktop monitor
                - config in types.py
    :stateManager:? the state manager
        :stateKeys used: {
            "activeMainWindowTab",
        }
    :return: None
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
        if (list := stateManager.check_if_state_exists("afterFunctionActions")):
            stateManager._interpret_and_call_functionType_list(list)

        stateManager.add_or_update_state(
            "activeMainWindowTab", MainWindowTabs.lineItem.value
        )



def activate_duplicate_claim_tab(
    windowSize: WindowSizes, stateManager: StateManager = None
):
    """
    Activates the duplicate claim tab
    :windowSize: the size of desktop monitor
                - config in types.py
    :stateManager:? the state manager
        :stateKeys used: {
            "activeMainWindowTab",
        }
    :return: None

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
        if (list := stateManager.check_if_state_exists("afterFunctionActions")):
            stateManager._interpret_and_call_functionType_list(list)

        stateManager.add_or_update_state(
            "activeMainWindowTab", MainWindowTabs.duplicate.value
        )
        