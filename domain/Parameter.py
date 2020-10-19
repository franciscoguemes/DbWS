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
        # if " " in self.__value:
        #     # return "'" + self.__value + "'"
        #     value = self.__value.replace(" ", "\\ ")
        #     value = value.replace("\"", "")
        #     return "\"" + value + "\""
        # else:
        #     return self.__value


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
        result = self.__application.get_result_as_string()
        result = result.strip()
        if result[0:2] == "['" and result[-2:] == "']":  # The string represents an array of strings...
            result = self.__transform_string_to_array_of_strings(result)
            # print(result)
        return result

    def __transform_string_to_array_of_strings(self, result):
        array_of_strings = []
        result = result[1:-1]  # Delete the first and last character...
        urls = result.split(", ")
        for url in urls:
            array_of_strings.append(url[1:-1])
        # return " ".join(array_of_strings)
        return array_of_strings

