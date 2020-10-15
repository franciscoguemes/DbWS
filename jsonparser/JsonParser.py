#!/usr/bin/env python3

import json
from json import JSONDecodeError
from string import Template

from domain.Application import Application
from domain.Argument import Argument
from domain.Context import Context
from domain.Parameter import RealParameter, CallToApplication


class JsonParser:
    """ A JSON parser for the Contexts file.
    """

    PATH_SEPARATOR = "/"

    def __init__(self, contexts_file, interpolation_dict=None):
        self.__contexts_file = contexts_file
        self.__interpolation_dict = interpolation_dict

    def get_all_contexts(self):
        with open(self.__contexts_file) as f:
            data = json.load(f)

        #print(data[0])

        contexts = []
        for json_context in data:
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
        arg_type = argument_json["type"]
        argument = argument_json["argument"]
        value = argument_json.get("value")

        if value:
            value = self.__interpolate(value)
            arg = Argument(arg_type, argument, value)
        else:
            arg = Argument(arg_type, argument)

        return arg

    def parse_parameter(self, parameter_json):
        parameter = None
        path = parameter_json.get("path")
        if path:  # Then it is a CallToParameter ...
            parameter = CallToApplication(self.parse_application(parameter_json))
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

