#!/usr/bin/env python3

from abc import ABC, abstractmethod


class Parameter(ABC):
    """
    The Parameter class. This class represents an abstraction of what a Parameter can be.
    A parameter can be a value that is part of an application call inside a Context or a parameter
    can be a call to another application that is embbeded as a parameter in an application call.
    """
    @abstractmethod
    def get_value(self):
        pass


class RealParameter(Parameter):

    def __init__(self, value):
        self.__value = value

    def get_value(self):
        return self.__value


class CallToApplication(Parameter):
    """
    If we would translate the CallToApplication parameter as pure JSON, the result would be an array of
    JSON objects of type parameter. See in the JSON configuration file examples of the value "parameters".
    "parameters": [
              {
                "value": "/Personal/\"Login screen\""
              }
            ]
    """
    def __init__(self, application):
        self.__application = application

    def get_value(self):
        return self.__application.get_result()
