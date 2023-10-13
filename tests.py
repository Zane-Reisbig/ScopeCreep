import threading
import keyboard
import os
from time import sleep, time

from windowHandlers import facetsWindowHandler
from screenReading import screenReading
from stateManager.stateManager import StateManager
from stateManager.types import WindowSizes, MainWindowTabs

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
        manager.check_if_state_exists("activeMainWindowTab")
        != MainWindowTabs.duplicate.value
    ):
        state_manager_results.append(False)
        return
    else:
        state_manager_results.append(True)
        print("We are on the Duplicate Tab")

    facetsWindowHandler.activate_line_item_tab(WindowSizes.large, manager)

    if (
        manager.check_if_state_exists("activeMainWindowTab")
        != MainWindowTabs.lineItem.value
    ):
        state_manager_results.append(False)
        return
    else:
        state_manager_results.append(True)
        print("We are on the Line Items Tab")

def state_manager_inital_state_lineItem_test():
    global state_manager_inital_state_lineItem_results
    
    myState = StateManager({"activeMainWindowTab": "lineItem"})

    if (
        myState.check_if_state_exists("activeMainWindowTab")
        != MainWindowTabs.lineItem.value
    ):
        state_manager_inital_state_lineItem_results.append(False)
    else:
        state_manager_inital_state_lineItem_results.append(True)

def state_manager_inital_state_duplicate_test():
    global state_manager_inital_state_duplicate_results

    myState = StateManager({"activeMainWindowTab": "duplicate"})
    
    if (
        myState.check_if_state_exists("activeMainWindowTab")
        != MainWindowTabs.duplicate.value
    ):
        state_manager_inital_state_duplicate_results.append(False)
    else:
        state_manager_inital_state_duplicate_results.append(True)

def state_manager_callable_state_printMe_test():
    global state_manager_callable_state_printMe_results
    myState = StateManager()

    myState.add_or_update_state("printMe", lambda:print("Hello World"))
    
    if (
        type(myState.check_if_state_exists("printMe")) == type(lambda:print("Hello World"))
    ):
        myState.check_if_state_exists("printMe")()
        state_manager_callable_state_printMe_results.append(True)
    else:
        state_manager_callable_state_printMe_results.append(False)
    
def state_manager_callable_state_sleep_test():
    global state_manager_callable_state_sleep_results
    myState = StateManager()
    
    myState.add_or_update_state("sleep", lambda:sleep(1))
    
    if (
        type(myState.check_if_state_exists("sleep")) == type(lambda:sleep(1))
    ):
        timeBefore = time()
        myState.check_if_state_exists("sleep")()
        timeAfter = time()
        print("Time it took to sleep for 1 second: ")
        print(timeAfter - timeBefore)
        state_manager_callable_state_sleep_results.append(True)
    else:
        state_manager_callable_state_sleep_results.append(False)



def threader(function, runAmount):
    for _ in range(runAmount):
        t = threading.Thread(target=function)
        t.start()
        t.join()

def print_results(array, expected):
    global total_tests, passed_tests
    total_equal_to_expected = 0
    total_tests += len(array)

    for result in array:
        print(f"Expected: {expected}, Actual: {result}")
        if result == expected:
            total_equal_to_expected += 1
            passed_tests += 1

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

# line_item_results = []
state_manager_results = []
state_manager_callable_state_printMe_results = []
state_manager_callable_state_sleep_results = []
state_manager_inital_state_lineItem_results = []
state_manager_inital_state_duplicate_results = []

total_tests = 0
passed_tests = 0

# threader(line_item_test, 4)
threader(state_manager_test, 4)
threader(state_manager_callable_state_printMe_test, 4)
threader(state_manager_callable_state_sleep_test, 4)
threader(state_manager_inital_state_lineItem_test, 4)
threader(state_manager_inital_state_duplicate_test, 4)

# print_results(line_item_results, True)
print_results(state_manager_results, True)
print_results(state_manager_callable_state_printMe_results, True)
print_results(state_manager_callable_state_sleep_results, True)
print_results(state_manager_inital_state_lineItem_results, True)
print_results(state_manager_inital_state_duplicate_results, True)

print(f"Total Tests: {total_tests}")
print(f"Passed Tests: {passed_tests}")
