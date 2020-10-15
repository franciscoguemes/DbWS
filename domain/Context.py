#!/usr/bin/env python3


class Context:
    """
    The Context class. This class represents a Context in the domain of the logic.
    """

    def __init__(self, name, applications):
        self.__name = name
        self.__applications = applications

    def get_name(self):
        return self.__name


