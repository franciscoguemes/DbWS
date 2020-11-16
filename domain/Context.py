#!/usr/bin/env python3


def the_string_is_empty(string_to_test):
    return string_to_test == "" or string_to_test is None

def transform_string_to_array_of_strings(self, result):
    array_of_strings = []
    if result == "[]" or result == "['']" or result == '[""]':
        return array_of_strings

    result = result[1:-1]  # Delete the first and last character...
    urls = result.split(", ")
    for url in urls:
        array_of_strings.append(url[1:-1])
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
        # tkinter.messagebox.showinfo(title="Executing context...", message=f"{self.__name}")

        for application in self.__applications:
            application.execute()

