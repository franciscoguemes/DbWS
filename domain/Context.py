#!/usr/bin/env python3

import re


def the_string_represents_an_array_of_strings(string_to_test):
    """
    Tells whether the given string represents an string array or not. I.e:
    string_to_test = "" # False
    string_to_test = "''" # False
    string_to_test = "foo" # False
    string_to_test = "'foo', 'and', 'foo'" # False
    string_to_test = "[]" # True
    string_to_test = "['']" # True
    string_to_test = "['string1', 'string2', ... ,'stringN']" # True

    :param string_to_test: The string to check.
    :return: True if the given string represents an array of strings otherwise False.
    """
    return (string_to_test[0:2] == "['" and string_to_test[-2:] == "']") or (
                len(string_to_test) == 2 and string_to_test == "[]")


def the_string_is_empty(string_to_test):
    return string_to_test == "" or string_to_test is None


def transform_string_to_array_of_strings(result):
    result = result.strip()
    array_of_strings = []
    if result == "[]" or result == "['']" or result == '[""]':
        return array_of_strings

    result = result[1:-1]  # Delete the first and last character ("[" and "]")
    result = result.strip()
    # logging.debug(result)
    strings = None
    if (result[0] == "\"" and result[-1] == "\"") or (result[0] == "'" and result[-1] == "'"):
        strings = re.split(", |,", result)
        # strings = result.split(", ")
    else:
        raise ValueError(f"The given string: \"{result}\" do not represent an array of strings!!!")

    for string in strings:
        array_of_strings.append(string[1:-1])
    # return " ".join(array_of_strings)
    return array_of_strings


class Context:
    """
    The Context class. This class represents a Context in the domain of the logic.
    """

    def __init__(self, name, applications):
        self.__name = name
        self.__applications = applications

    def get_name(self):
        return self.__name

    def switch(self):
        for application in self.__applications:
            application.execute()
