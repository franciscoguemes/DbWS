#!/usr/bin/env python3

import json
from json import JSONDecodeError
from string import Template

from domain.Application import Application
from domain.Argument import RealArgument, CallToApplicationArgumentValue, CallToApplicationArgument
from domain.Context import Context
from domain.Parameter import RealParameter, CallToApplicationParameter
from error.InvalidContextFileError import InvalidContextFileError
from jsonparser.JsonReader import JsonReader


class ContextParser(JsonReader):
    """
    A JSON parser for the Contexts file.
    This class contains specific functionality to parse the context files.
    """

    def __init__(self, json_file, interpolation_dict=None):
        super().__init__(json_file)
        self.__interpolation_dict = interpolation_dict
        self.__json_data = None

    def get_schema_version(self):
        """
        The method search for the property "schema_version" in the root of the JSON document.
        If the property exists it returns the value if not it throws an InvalidContextFileError
        :return: The version of the schema used in the document.
        """
        data = super().read_all_data()

        schema_version = data.get("schema_version")
        if schema_version:
            return schema_version
        else:
            raise InvalidContextFileError(f"The given contexts file:'{super().get_file()}' does not contain the "
                                          f"attribute 'schema_version' and therefore is an invalid file")

    def get_all_contexts(self):
        data = self.read_all_data()

        json_contexts = data["contexts"]
        # print(json_contexts)

        contexts = []
        for json_context in json_contexts:
            context = self.parse_context(json_context)
            contexts.append(context)

        return contexts

    def parse_context(self, json_context):
        # print(json_context)

        name = json_context["name"]
        applications_json = json_context["applications"]
        applications = []
        for application_json in applications_json:
            application = self.parse_application(application_json)
            applications.append(application)

        return Context(name, applications)

    def parse_application(self, application_json):

        application = None

        # print(application_json)
        name = application_json["name"]
        path = self.__interpolate(application_json["path"])

        # https://realpython.com/python-keyerror/#the-rare-solution-checking-for-keys
        parameters = None
        arguments = None

        arguments_json = application_json.get("arguments")
        if arguments_json:
            # Parse the arguments...
            arguments = []
            for argument_json in arguments_json:
                argument = self.parse_argument(argument_json)
                arguments.append(argument)

        parameters_json = application_json.get("parameters")
        if parameters_json:
            # Parse the parameters...
            parameters = []
            for parameter_json in parameters_json:
                parameter = self.parse_parameter(parameter_json)
                parameters.append(parameter)

        application = Application(name, path, arguments, parameters)
        return application

    def parse_argument(self, argument_json):
        arg = None
        if self.__is_an_application_call(argument_json):
            arg = CallToApplicationArgument(self.parse_application(argument_json))
        else: # Is either a 100% defined argument or an argument with a call in the value
            arg_type = argument_json["type"]
            argument = self.__interpolate(argument_json["argument"])
            json_value = argument_json.get("value")
            # print(type(json_value))
            if json_value:
                if self.__is_an_application_call(json_value):
                    arg = CallToApplicationArgumentValue(arg_type, argument, self.parse_application(json_value))
                else:
                    json_value = self.__interpolate(json_value)
                    arg = RealArgument(arg_type, argument, json_value)
            else:
                arg = RealArgument(arg_type, argument)

        return arg

    def __is_an_application_call(self, json_value):
        # print(json_value)
        # print(type(json_value))

        if isinstance(json_value, dict):
            path = json_value.get("path")
            if path:
                return True

        return False

    def parse_parameter(self, parameter_json):
        parameter = None
        if self.__is_an_application_call(parameter_json):  # Then it is a CallToParameter ...
            parameter = CallToApplicationParameter(self.parse_application(parameter_json))
        else:  # Normal parameter
            parameter = RealParameter(parameter_json["value"])
        return parameter

    def __interpolate(self, non_interpolated_value):
        # for key in self.__interpolation_dict:
        #     print(f"{key} : {self.__interpolation_dict[key]}")

        # print(self.__interpolation_dict)

        # print(non_interpolated_value)
        if self.__interpolation_dict is None:
            return non_interpolated_value

        template = Template(non_interpolated_value)
        interpolated_value = template.substitute(self.__interpolation_dict)
        return interpolated_value
