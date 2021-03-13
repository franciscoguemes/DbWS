#!/usr/bin/env python3
import logging
import subprocess

logger = logging.getLogger('DbWS')

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

    def get_result_as_string(self):
        logger.debug(f"Method application={self.__name}")
        full_command = self.get_full_command()
        logger.debug(f"full_command: {full_command}")

        application = subprocess.Popen(full_command, stdout=subprocess.PIPE)
        application.wait()
        result = application.communicate()[0]
        logger.debug(f"result: {result}")
        result = result.decode("utf-8")
        return result
        #
        # application = subprocess.run(full_command, stdout=subprocess.PIPE)
        # result = application.stdout.decode("utf-8")
        # # print(result)
        # # print(type(result))
        # return result

    def execute(self):
        logger.debug(f"Method application={self.__name}")
        full_command = self.get_full_command()
        logger.debug(full_command)
        # list_files = subprocess.run(full_command)
        # print("The exit code was: %d" % list_files.returncode)

        application = subprocess.Popen(full_command)

    def get_full_command(self):
        """
        Returns the command as an array of strings. I.e ["ls", "-a", "-l", "-h"]
        :return: An array of strings that represents the command the arguments (options and values (if needed) and
        the parameters (if any)
        """
        command = [self.__path]
        if self.__arguments:
            for argument in self.__arguments:
                # print(argument.as_string())
                arg_array = argument.as_string_array()
                for arg in arg_array:
                    command.append(arg)

        if self.__parameters:
            for parameter in self.__parameters:
                value = parameter.get_value()
                # print(type(value))
                if isinstance(value, str):
                    command.append(value)
                elif isinstance(value, list):
                    for element in value:
                        command.append(element)
                else:
                    # TODO: Throw exception here, there is no parameter other than a string or a list of strings...
                    pass

        return command

