#!/usr/bin/env python3


class Argument:
    """
    The Argument class. This class represents an argument that is used when executing a command.
    """

    TYPE_GNU = "GNU"
    TYPE_POSIX = "POSIX"

    def __init__(self, type, argument, value=None):
        self.check_type(type)
        self.__type = type
        self.__argument = argument
        self.__value = value

    @staticmethod
    def check_type(type):
        if type != Argument.TYPE_GNU and type != Argument.TYPE_POSIX:
            msg = f"The given value for the argument type: \"{type}\" is invalid"
            raise ValueError(msg)

    def as_string(self):
        argument = None
        if self.__value:
            if type == self.TYPE_GNU:
                argument = self.__argument + "=" + self.__value
            elif self.__type == self.TYPE_POSIX:
                argument = self.__argument + " " + self.__value
            else:  # It should not enter here since there is only those types of arguments
                # TODO: Throw an error here
                pass
        else:  # There is no value so it does not matter the type of argument...
            argument = self.__argument

        return argument


