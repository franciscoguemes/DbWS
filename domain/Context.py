#!/usr/bin/env python3
import subprocess
import tkinter.messagebox


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

