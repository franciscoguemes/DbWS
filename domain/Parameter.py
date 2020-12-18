#!/usr/bin/env python3

from abc import ABC, abstractmethod

from domain.Context import transform_string_to_array_of_strings, the_string_is_empty, \
    the_string_represents_an_array_of_strings


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


class CallToApplicationParameter(Parameter):
    """
    The overall parameter is the result of calling to an external application object defined in the place of a
     parameter object.

    The result of a CallToApplicationParameter is an array of strings that simply represents the results of the
    application. In this case the user has the entire responsibility of providing an external application call
    whose result is a valid (or a sequence of valid) parameter for the given command. The following
    outcome examples are handled gracefully by the application:

    1 parameter   --->  hello world!
    1 parameter   --->  ["hello world!"]
    N parameters  --->  hello world!
                        My name is Francisco
                        21.1
    N parameters  --->  ["parameter1", "parameter2", ..., "parameterN"]
    """
    def __init__(self, application):
        self.__application = application

    def get_value(self):
        result = self.__application.get_result_as_string()
        result = result.strip()
        if the_string_is_empty(result):
            raise ValueError("The result of the application can not be empty!!!")

        if the_string_represents_an_array_of_strings(result):
            result = transform_string_to_array_of_strings(result)
        else:
            # Is the string a multiline string (contains at least one character '\n') ?
            # https://stackoverflow.com/questions/24237524/how-to-split-a-python-string-on-new-line-characters
            multiple_lines = list(filter(bool, result.splitlines()))
            if len(multiple_lines) > 1:
                result = map(lambda x: x.strip(), multiple_lines)

        return result

