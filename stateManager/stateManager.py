import uuid


class StateManager:
    def __init__(self):
        self.state_dictonary = {}
        self.id = uuid.uuid4()

    def report_id(self):
        return self.id

    def add_or_update_state(self, state_name: str, state: object):
        self.state_dictonary[state_name] = state

    def get_state(self, state_name: str) -> object:
        return self.state_dictonary[state_name]

    def get_state_names(self) -> list:
        return self.state_dictonary.keys()

    def get_state_values(self) -> list:
        """
        Returns a list of all the values in the state dictonary
        :return: a list of all the values in the state dictonary
        """

        return self.state_dictonary.values()

    def check_if_state_exists(self, state_name: str) -> (bool, object):
        """
        Checks if a state exists
        :state_name: the name of the state
        :return: a tuple containing a bool and the state
        """

        if state_name in self.state_dictonary:
            return True, self.state_dictonary[state_name]
        else:
            return False, False
