#!/usr/bin/env python3
import logging
from abc import ABC, abstractmethod

from domain.Context import transform_string_to_array_of_strings, the_string_is_empty, \
    the_string_represents_an_array_of_strings


class Argument(ABC):
    """
    The Argument class. This class represents an abstraction of what an Argument can be.
    A parameter can be a value that is part of an application call inside a Context or a parameter
    can be a call to another application that is embbeded as a parameter in an application call.
    """

    TYPE_GNU = "GNU"
    TYPE_POSIX = "POSIX"

    @staticmethod
    def check_type(arg_type):
        if arg_type != RealArgument.TYPE_GNU and arg_type != RealArgument.TYPE_POSIX:
            msg = f"The given value for the argument type: \"{arg_type}\" is invalid"
            raise ValueError(msg)

    @staticmethod
    def build_argument(argument, value, arg_type):
        build_arg = []
        if arg_type == Argument.TYPE_GNU:
            if value:
                build_arg.append(argument + "=" + value)
            else:
                build_arg.append(argument)
        elif arg_type == Argument.TYPE_POSIX:
            build_arg.append(argument)
            if value:
                build_arg.append(value)
        else:  # It should not enter here since there is only those types of arguments
            raise ValueError(f"Only types: '{Argument.TYPE_GNU}' and '{Argument.TYPE_POSIX}' are allowed!")

        return build_arg

    @abstractmethod
    def as_string_array(self):
        pass


class RealArgument(Argument):
    """
    The Argument class. This class represents an argument that is used when executing a command.
    """

    def __init__(self, arg_type, argument, value=None):
        self.check_type(arg_type)
        self.__type = arg_type
        self.__argument = argument
        self.__value = value

    def as_string_array(self):
        # raise NotImplementedError("This should return an array of strings...")
        return self.build_argument(self.__argument, self.__value, self.__type)


class CallToApplicationArgumentValue(Argument):
    """
    The overall argument is calculated as a combination of processing the fields "type" and "argument" plus calling
    to an external application object embedded in the value of the field "value".

    The result of a CallToApplicationArgumentValue is an array of strings in the following way:
    GNU   --->  ["argument=value"]
    POSIX --->  ["argument", "value"]

    In order to calculate the "value" of both expressions it is necessary to call to an external application.
    """

    def __init__(self, arg_type, argument, application):
        self.check_type(arg_type)
        self.__type = arg_type
        self.__argument = argument
        self.__application = application

    def as_string_array(self):
        application_result = self.__application.get_result_as_string()
        application_result = application_result.strip()
        if the_string_is_empty(application_result):
            raise ValueError("The result of the application can not be empty!!!")

        if the_string_represents_an_array_of_strings(application_result):
            raise ValueError("The result of the application must be a single value. "
                             "It can not be an array of values. Otherwise replace the entire argument definition by"
                             "an application call definition and ensure the application returns a valid argument for"
                             "the given parent application")

        return self.build_argument(self.__argument, application_result, self.__type)


class CallToApplicationArgument(Argument):
    """
    The overall argument is the result of calling to an external application object defined in the place of an
    argument object.

    The result of a CallToApplicationArgument is an array of strings that simply represents the results of the
    application. In this case the user has the entire responsibility of providing an external application call
    whose result is a valid (or a sequence of valid) GNU or POSIX argument(s) for the given command. The following
    outcome examples are handled gracefully by the application:
    GNU   --->  --argument=value
    GNU   --->  ["--argument=value"]
    GNU   --->  --argument1=value1
                --argument2=value2
                --argument3=value3
    GNU   --->  ["--argument1=value1", "--argument2=value2", ..., "--argumentN=valueN"]
    POSIX --->  ["-argument", "value"]
    POSIX --->  ["-argument1", "value1", "-argument2", "value2", ..., "-argumentN", "valueN"]
    """

    def __init__(self, application):
        self.__application = application

    def as_string_array(self):
        application_result = self.__application.get_result_as_string()
        application_result = application_result.strip()
        if the_string_is_empty(application_result):
            raise ValueError("The result of the application can not be empty!!!")

        if the_string_represents_an_array_of_strings(application_result):
            application_result = transform_string_to_array_of_strings(application_result)
        else:  # The string is a single string, so wrap it into an array
            # Is the string a multiline string (contains at least one character '\n') ?
            # https://stackoverflow.com/questions/24237524/how-to-split-a-python-string-on-new-line-characters
            multiple_lines = list(filter(bool, application_result.splitlines()))
            if len(multiple_lines) > 1:
                application_result = map(lambda x: x.strip(), multiple_lines)
            else:
                application_result = [application_result]

        return application_result
