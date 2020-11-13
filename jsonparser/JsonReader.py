#!/usr/bin/env python3

import json
from json import JSONDecodeError
from string import Template

from domain.Application import Application
from domain.Argument import Argument
from domain.Context import Context
from domain.Parameter import RealParameter, CallToApplication
from error.InvalidContextFileError import InvalidContextFileError


class JsonReader:
    """
    A Generic JSON reader class.
    The class is aimed to read the JSON content from the file.
    The class has a internal buffer so the reading operation is performed only the first time.
    """

    def __init__(self, json_file):
        self.__json_file = json_file
        self.__json_data = None

    def get_file(self):
        return self.__json_file

    def read_all_data(self):
        if self.__json_data is None:
            with open(self.__json_file) as f:
                self.__json_data = json.load(f)

        return self.__json_data

