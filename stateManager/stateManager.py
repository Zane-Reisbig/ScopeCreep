from typing import Union
import uuid


class StateManager:
    def __init__(self, initalState:object = None):
        """
        Creates a state manager
        :initalState: the inital keys and values to add to the state manager
        :return: None
        """
        
        
        self.state_dictonary = {}
        self.id = uuid.uuid4()
        if initalState is not None:
            if isinstance(initalState, dict):
                for key in initalState:
                    self.add_or_update_state(key, initalState[key])
            elif isinstance(initalState, list):
                for item in initalState:
                    self.add_or_update_state(item[0], item)
            elif isinstance(initalState, tuple):
                for item in initalState:
                    self.add_or_update_state(item[0], item)
            else:
                raise TypeError(f"Type {type(initalState)} is not supported")

        

    def report_id(self):
        """
        Returns the id of the state manager
        I still don't believe python is making different objects
        """
        
        return self.id

    def add_or_update_state(self, stateName: str, state: object):
        """
        Adds or updates a state
        """
        
        if stateName in self.state_dictonary:
            if isinstance(self.state_dictonary[stateName], list):
                self.state_dictonary[stateName].append(state)
            else:
                self.state_dictonary[stateName] = state
        else:
            self.state_dictonary[stateName] = state


    def remove_state(self, stateName: str):
        
        if stateName in self.state_dictonary:
            del self.state_dictonary[stateName]
        else:
            raise KeyError(f"State {stateName} does not exist")


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

    def check_if_state_exists(self, stateName: str) -> bool|object:
        """
        Checks if a state exists
        :stateName: the name of the state
        :return: a tuple containing a bool and the state
        """

        if stateName in self.state_dictonary:
            return self.state_dictonary[stateName]
        else:
            return False
    
    def check_if_state_exists_and_invoke(self, stateName: str, *args, **kwargs) -> bool|object:
        """
        Checks if a state exists and invokes it if it does
        :stateName: the name of the state
        :*args: the args to pass to the state
        :**kwargs: the kwargs to pass to the state
        :return: a tuple containing a bool and the state
        """

        if stateName in self.state_dictonary:
            return self.state_dictonary[stateName](*args, **kwargs)
        else:
            return False, False
    
    def interpret_callable_state(self, stateName: str, *args, **kwargs) -> object|None:
        """
        Interprets a callable state
        :stateName: the name of the state
        :*args: the args to pass to the callable state
        :**kwargs: the kwargs to pass to the callable state
        :return: the result of the callable state
                if the key does not exist, None is returned
        _______________________
        WARNING WARNING WARNING 
        
        THIS IS NOT SAFE
        THIS IS USING EVAL
        THIS WILL DO WHAT EVER YOU TELL IT TO DO
        DEAL ACCORDINGLY
        
        WARNING WARNING WARNING 
        -----------------------
        """
        
        if stateName in self.state_dictonary:
            return eval(self.state_dictonary[stateName])(*args, **kwargs)
        else:
            return None

    def _interpret_and_call_functionType_list(self, list):
        """
        !This is an internal method!
        Interprets and calls all the functions in a list
        :list: the list of functions to interpret and call
        :return: None
        """
        
        for func in list:
            func()