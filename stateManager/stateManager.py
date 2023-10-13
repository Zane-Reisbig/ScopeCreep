from typing import Union
import uuid


class StateManager:
    def __init__(self):
        self.state_dictonary = {}
        self.id = uuid.uuid4()

    def report_id(self):
        """
        Returns the id of the state manager
        I still don't believe python is making different objects
        😆
        """
        
        return self.id

    def add_or_update_state(self, state_name: str, state: object):
        """
        Adds or updates a state
        """
        
        self.state_dictonary[state_name] = state

    def get_state(self, state_name: str) -> object:
        """
        Returns the state object
        :state_name: the name of the state
        :return: the state object
        """
        
        return self.state_dictonary[state_name]

    def get_state_names(self) -> list:
        """
        Returns a list of all the state names
        :return: a list of all the state names (keys)
        """
        
        return self.state_dictonary.keys()

    def get_state_values(self) -> list:
        """
        Returns a list of all the values in the state dictonary
        :return: a list of all the values in the state dictonary
        """

        return self.state_dictonary.values()

    def check_if_state_exists(self, stateName: str) -> Union[bool, object]:
        """
        Checks if a state exists
        :stateName: the name of the state
        :return: a tuple containing a bool and the state
        """

        if stateName in self.state_dictonary:
            return True, self.state_dictonary[stateName]
        else:
            return False, False
