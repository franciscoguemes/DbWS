#!/usr/bin/env python3


class Application:
    """
    The Context class. This class represents a Context in the domain of the logic.
    """

    def __init__(self, name, path, arguments=None, parameters=None):
        self.__name = name
        self.__path = path
        self.__arguments = arguments
        self.__parameters = parameters

    def get_name(self):
        return self.__name

