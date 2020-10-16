#!/usr/bin/env python3
import subprocess


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

    def execute(self):
        full_command = self.get_full_command()
        # list_files = subprocess.run(full_command)
        # print("The exit code was: %d" % list_files.returncode)

        application = subprocess.Popen(full_command)

    def get_full_command(self):
        """
        Returns the command as an array of strings. I.e ["ls", "-a", -"l", "-h"]
        :return: An array of strings that represents the command the options and the arguments
        """
        command = [self.__path]
        if self.__arguments:
            for argument in self.__arguments:
                command.append(argument.as_string())

        if self.__parameters:
            for parameter in self.__parameters:
                command.append(parameter.get_value())
        return command

