#!/usr/bin/env python3

from abc import ABC, abstractmethod


class Argument(ABC):
    """
    The Argument class. This class represents an abstraction of what an Argument can be.
    A parameter can be a value that is part of an application call inside a Context or a parameter
    can be a call to another application that is embbeded as a parameter in an application call.
    """

    TYPE_GNU = "GNU"
    TYPE_POSIX = "POSIX"

    @staticmethod
    def check_type(type):
        if type != RealArgument.TYPE_GNU and type != RealArgument.TYPE_POSIX:
            msg = f"The given value for the argument type: \"{type}\" is invalid"
            raise ValueError(msg)

    @staticmethod
    def build_argument(argument, value, arg_type):
        build_arg = argument
        if value:
            if arg_type == Argument.TYPE_GNU:
                build_arg += "=" + value
            elif arg_type == Argument.TYPE_POSIX:
                build_arg += " " + value
            else:  # It should not enter here since there is only those types of arguments
                raise ValueError(f"Only types: '{Argument.TYPE_GNU}' and '{Argument.TYPE_POSIX}' are allowed!")
        return build_arg

    @abstractmethod
    def as_string(self):
        pass


class RealArgument(Argument):
    """
    The Argument class. This class represents an argument that is used when executing a command.
    """

    def __init__(self, type, argument, value=None):
        self.check_type(type)
        self.__type = type
        self.__argument = argument
        self.__value = value

    def as_string(self):
        raise NotImplementedError("This should return an array of strings...")
        return self.build_argument(self.__argument, self.__value, self.__type)
        # argument = self.__argument
        # if self.__value:
        #     if self.__type == self.TYPE_GNU:
        #         argument += "=" + self.__value
        #     elif self.__type == self.TYPE_POSIX:
        #         argument += " " + self.__value
        #     else:  # It should not enter here since there is only those types of arguments
        #         raise ValueError(f"Only types: '{self.TYPE_GNU}' and '{self.TYPE_POSIX}' are allowed!")
        #
        # return argument


class CallToApplicationArgumentValue(Argument):
    """
    The argument is calculated as a combination of processing the paramters "type" and "argument" plus calling
    to an external application represented by the last paramter "application".

    The result of a CallToApplicationArgumentValue is an array of strings in the following way:
    GNU   --->  ["argument=value"]
    POSIX --->  ["argument", "value"]

    In order to calculate the "value" of both expressions it is necessary to call to an external application.
    """

    def __init__(self, type, argument, application):
        self.check_type(type)
        self.__type = type
        self.__argument = argument
        self.__application = application

    def as_string(self):
        raise NotImplementedError("This should return an array of strings...")
        application_result = self.__application.get_result_as_string()
        application_result = application_result.strip()
        if application_result[0:2] == "['" and application_result[
                                               -2:] == "']":  # The string represents an array of strings...
            raise ValueError("The result of the application must be a single value not an array of values")
            # result = self.__transform_string_to_array_of_strings(result)
            # print(result)

        return self.build_argument(self.__argument, application_result, self.__type)

        # if result:
        #     if self.__type == self.TYPE_GNU:
        #         argument += "=" + result
        #     elif self.__type == self.TYPE_POSIX:
        #         argument += " " + result
        #     else:  # It should not enter here since there is only those types of arguments
        #         raise ValueError(f"Only types: '{self.TYPE_GNU}' and '{self.TYPE_POSIX}' are allowed!")
        #
        # return argument


class CallToApplicationArgument(Argument):
    """
    The entire argument is the result of calling to an external application.
    The result of a CallToApplicationArgument is an array of strings that simply represents the results of the
    application. In this case the user has the entire responsibility of providing an external application call
    whose result is a valid (or a sequence of valid) GNU or POSIX argument(s) for the given command. The following
    outcome examples are handled gracefully by the application:
    GNU   --->  ["argument=value"]
    GNU   --->  ["argument1=value1", "argument2=value2", ..., "argumentN=valueN"]
    POSIX --->  ["argument", "value"]
    POSIX --->  ["argument1", "value1", "argument2", "value2", ..., "argumentN", "valueN"]
    """

    def __init__(self, application):
        self.__application = application

    def as_string(self):
        raise NotImplementedError("This should return an array of strings...")
        application_result = self.__application.get_result_as_string()
        application_result = application_result.strip()
        if application_result[0:2] == "['" and application_result[
                                               -2:] == "']":  # The string represents an array of strings...
            raise ValueError("The result of the application must be a single value not an array of values")
            # result = self.__transform_string_to_array_of_strings(result)
            # print(result)

        return application_result
