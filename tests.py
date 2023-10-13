import threading
import keyboard
import os
from time import sleep

from windowHandlers import facetsWindowHandler
from screenReading import screenReading
from stateManager.stateManager import StateManager
from stateManager.types import WindowSizes, MainWindowTabs


line_item_results = []
state_manager_results = []


def line_item_test():
    global line_item_results

    tessPath = poorMansEnv("tessPath")

    facetsWindowHandler.activate_duplicate_claim_tab(WindowSizes.large)
    sleep(0.5)

    facetsWindowHandler.activate_line_item_tab(WindowSizes.large)
    sleep(0.5)

    result = facetsWindowHandler.check_if_duplicate(tessPath, WindowSizes.large)

    line_item_results.append(result)


def state_manager_test():
    global state_manager_results

    manager = StateManager()
    tessPath = poorMansEnv("tessPath")

    facetsWindowHandler.activate_duplicate_claim_tab(WindowSizes.large, manager)

    if (
        manager.check_if_state_exists("activeMainWindowTab")[1]
        != MainWindowTabs.duplicate.value
    ):
        state_manager_results.append(False)
        return
    else:
        state_manager_results.append(True)
        print("We are on the Duplicate Tab")

    facetsWindowHandler.activate_line_item_tab(WindowSizes.large, manager)

    if (
        manager.check_if_state_exists("activeMainWindowTab")[1]
        != MainWindowTabs.lineItem.value
    ):
        state_manager_results.append(False)
        return
    else:
        state_manager_results.append(True)
        print("We are on the Line Items Tab")


def threader(function, runAmount):
    for _ in range(runAmount):
        t = threading.Thread(target=function)
        t.start()
        t.join()


def print_results(array, expected):
    total_equal_to_expected = 0

    for result in array:
        print(f"Expected: {expected}, Actual: {result}")
        if result == expected:
            total_equal_to_expected += 1

    print(f"Total Success: {total_equal_to_expected}")
    print(f"Total Fail: {len(array) - total_equal_to_expected}")


def poorMansEnv(key):
    folderPath = os.path.dirname(os.path.abspath(__file__))
    filePath = os.path.join(folderPath, ".env")

    with open(filePath, "r") as f:
        lines = f.readlines()
        for line in lines:
            if line.startswith(key):
                return line.split("=")[1].strip()
        return None


threader(line_item_test, 4)
threader(state_manager_test, 4)

print_results(line_item_results, True)
print_results(state_manager_results, True)
