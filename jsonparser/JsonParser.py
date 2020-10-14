#!/usr/bin/env python3

import json
from json import JSONDecodeError

from domain.Application import Application
from domain.Argument import Argument
from domain.Context import Context


class JsonParser:
    """ A JSON parser for the Contexts file.
    """

    PATH_SEPARATOR = "/"

    def __init__(self, contexts_file):
        self.__contexts_file = contexts_file

    def get_all_contexts(self):
        with open(self.__contexts_file) as f:
            data = json.load(f)

        #print(data[0])

        contexts = []
        for json_context in data:
            context = self.__parse_context(json_context)
            contexts.append(context)

        return contexts

    def __parse_context(self, json_context):
        # print(json_context)

        name = json_context["name"]
        applications_json = json_context["applications"]
        applications = []
        for application_json in applications_json:
            application = self.__parse_application(application_json)
            applications.append(application)

        return Context(name, applications)

    def __parse_application(self, application_json):

        application = None

        # print(application_json)
        name = application_json["name"]
        path = application_json["path"]

        # https://realpython.com/python-keyerror/#the-rare-solution-checking-for-keys
        arguments_json = application_json.get("arguments")
        if arguments_json:
            # Parse the arguments...
            arguments_json = application_json["arguments"]
            arguments = []
            for argument_json in arguments_json:
                argument = self.__parse_argument(argument_json)
                arguments.append(argument)

            application = Application(name, path, arguments)
        else:
            # No arguments are defined for this application...
            application = Application(name, path)

        return application

    def __parse_argument(self, argument_json):
        arg = None
        type = argument_json["type"]
        argument = argument_json["argument"]
        value = argument_json.get("value")

        if value:
            arg = Argument(type, argument, value)
        else:
            arg = Argument(type, argument)

        return arg