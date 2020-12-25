#!/usr/bin/python3
import argparse
import logging
import os
import sys
from json import JSONDecodeError
from pathlib import Path
import configparser
from time import sleep

import jsonschema
from jsonschema import ValidationError

from error import InvalidContextFileError
from error.InvalidContextFileError import InvalidContextFileError
from tkinter import Tk, PhotoImage
from gui.MainWindow import MainWindow
from jsonparser.JsonReader import JsonReader
from jsonparser.ContextParser import ContextParser

DEFAULT_CONFIG_FILE = "DbWS.conf"
DEFAULT_CONFIG_DIR = "/home/francisco/.config/DbWS"

CONFIG_KEY_LOCAL = "LOCAL"
CONFIG_KEY_CONTEXTS_FILES = "CONTEXTS_FILE"
CONFIG_KEY_ENVIRONMENT = "ENVIRONMENT"

SCHEMA_ROOT_NAME = "DbWS_context_schema_"
JSON_EXTENSION = ".json"
SCHEMA_DIRECTORY = "schemas"


def get_schema_file(schema_version):
    schema_file_name = SCHEMA_ROOT_NAME + str(schema_version) + JSON_EXTENSION
    schema_file = SCHEMA_DIRECTORY + os.path.sep + schema_file_name
    return schema_file


def main():
    logging.basicConfig(level=logging.DEBUG)

    try:

        logging.info("Parse command line arguments...")
        parser = argparse.ArgumentParser()
        parser.add_argument("--config", help="Path to the general configuration file")
        parser.add_argument("--logging", help="Path to the logging configuration file")
        args = parser.parse_args()

        if args.logging:
            logging.info(f"Logging configuration file {args.logging} has been supplied")
            # TODO: Parse the supplied configuration
            #   https://docs.python.org/3.6/howto/logging.html#configuring-logging
        else:
            logging.info("Using the default logging configuration...")
            #TODO: Define the default configuration
            #   https://docs.python.org/3.6/howto/logging.html#configuring-logging
            pass

        config_file_path = None
        if args.config:
            # DbWS --config=/path/to/my/config_file
            logging.info(f"Configuration file {args.config} has been supplied")
            config_file_path = Path(args.config).absolute()
            check_configuration_file_exists(config_file_path)
        else:
            # if no arguments are supplied then the application will take the config from .config/DbWS/DbWS.conf
            logging.info("Using the default configuration...")
            config_file_path = get_default_configuration_path()

        logging.info("Load configuration...")
        config = load_configuration(config_file_path)
        contexts_file = config[CONFIG_KEY_LOCAL][CONFIG_KEY_CONTEXTS_FILES]
        # print(contexts_file)

        logging.info("Validate against schema...")
        context_parser = ContextParser(contexts_file, get_config_section_as_dictionary(config, CONFIG_KEY_ENVIRONMENT))
        schema_version = context_parser.get_schema_version()

        schema_file = get_schema_file(schema_version)
        json_reader = JsonReader(schema_file)
        schema_json_data = json_reader.read_all_data()

        context_json_data = context_parser.read_all_data()
        # print(context_json_data)
        # print(schema_json_data)
        jsonschema.validate(context_json_data, schema_json_data)
        # print("It validates correctly...")


        logging.info("Parse Contexts...")
        # TODO: Parse contexts
        # http://commons.apache.org/proper/commons-cli/
        #   When parsing context arguments remember that:
        #       GNU --> Need the "=" character
        #       POSIX --> Do not need to add any characters
        #   When building up the entire command from the parsed JSON remember that:
        #       You need to substitute the defined variables in the configuration file...
        #       Some profiles of Chromium have scaped double quotes in the Context definition because
        #       the quotes are needed for the command line
        contexts = context_parser.get_all_contexts()
        # for context in contexts:
        #     print(context.get_name())

        logging.info("Show initial window...")
        root = Tk()
        # icon = PhotoImage(file="schemas/webserver.png")
        # root.iconphoto(True, icon)
        root.title("DbWS")
        root.resizable(0, 0)
        main_window = MainWindow(root, contexts)
        main_window.pack()
        root.mainloop()

    except JSONDecodeError as e:
        print(e)
    except InvalidContextFileError as e:
        print(e)
    except ValidationError as e:
        print(e)


def get_default_configuration_path():
    # Check if the config dir exists...
    configuration_directory = Path(DEFAULT_CONFIG_DIR).absolute()
    if not configuration_directory.is_dir():
        msg = "The configuration directory: " + str(configuration_directory) + " does not exists." \
              + " Please read the app documentation and fix the issue."
        raise NotADirectoryError(msg)

    # Check if the config file exists...
    configuration_file = configuration_directory / DEFAULT_CONFIG_FILE
    check_configuration_file_exists(configuration_file)
    return configuration_file


def check_configuration_file_exists(configuration_file):
    if not configuration_file.is_file():
        msg = "The configuration file: " + str(configuration_file) + " does not exists." \
              + " Please read the app documentation and fix the issue."
        raise FileNotFoundError(msg)


def load_configuration(configuration_file):
    config = configparser.ConfigParser()
    # Preserves the case sensitive in the parser...
    config.optionxform = str
    config.read(configuration_file.absolute())
    # print_configuration(config)
    check_config(config)
    return config


def print_configuration(config):
    for key in config:
        print(key)
        for inner_key in config[key]:
            print(f"\t{inner_key}")


def check_config(config):
    if 'LOCAL' not in config:
        msg = "The configuration file must have a section called [LOCAL]." + "\n "
        msg += """Please have a look at the documentation of the project and edit the config file in the pertinent way.
        More info about config files on: https://docs.python.org/3/library/configparser.html
        """
        raise Exception(msg)
        # sys.exit(msg)
    # TODO: Check the rest of the configuration parameters here...


def get_config_section_as_dictionary(config, section_key):
    """
    Given a configuration and a Section key, it returns a dictionary
    :param section:
    :return:
    :see: https://gist.github.com/amitsaha/3065184
    """
    temp_dict = {}
    section = config[section_key]
    for section_key in section:
        temp_dict[section_key] = str(section[section_key])
    return temp_dict


if __name__ == "__main__":
    main()
