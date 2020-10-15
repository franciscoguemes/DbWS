#!/usr/bin/python3

import sys
from json import JSONDecodeError
from pathlib import Path
import configparser
from time import sleep

from jsonparser.JsonParser import JsonParser

DEFAULT_CONFIG_FILE = "DbWS.conf"
DEFAULT_CONFIG_DIR = "/home/francisco/.config/DbWS"

CONFIG_KEY_LOCAL = "LOCAL"
CONFIG_KEY_CONTEXTS_FILES = "CONTEXTS_FILE"
CONFIG_KEY_ENVIRONMENT = "ENVIRONMENT"


def main():
    try:
        print("Parse arguments...")
        # TODO: Parse arguments
        # DbWS --config=/path/to/my/config_file
        # if no arguments are supplied then the application will take the config from .config/DbWS/DbWS.conf

        print("Load configuration...")
        config = load_configuration()
        contexts_file = config[CONFIG_KEY_LOCAL][CONFIG_KEY_CONTEXTS_FILES]
        # print(contexts_file)

        print("Parse Contexts...")
        # TODO: Parse contexts
        # http://commons.apache.org/proper/commons-cli/
        #   When parsing context arguments remember that:
        #       GNU --> Need the "=" character
        #       POSIX --> Do not need to add any characters
        #   When building up the entire command from the parsed JSON remember that:
        #       You need to substitute the defined variables in the configuration file...
        #       Some profiles of Chromium have scaped double quotes in the Context definition because
        #       the quotes are needed for the command line

        parser = JsonParser(contexts_file, get_config_section_as_dictionary(config,CONFIG_KEY_ENVIRONMENT))
        contexts = parser.get_all_contexts()
        for context in contexts:
            print(context.get_name())

        print("Show initial window...")

    except JSONDecodeError as e:
        print(e)


def load_configuration():

    # Check if the config dir exists...
    cdir = Path(DEFAULT_CONFIG_DIR).absolute()
    if not cdir.is_dir():
        msg = "The configuration directory: " + str(cdir) + " does not exists." \
              + " Please read the app documentation and fix the issue."
        raise NotADirectoryError(msg)

    # Check if the config file exists...
    cfile = cdir / DEFAULT_CONFIG_FILE
    if not cfile.is_file():
        msg = "The configuration file: " + str(cfile) + " does not exists." \
              + " Please read the app documentation and fix the issue."
        raise FileNotFoundError(msg)

    config = configparser.ConfigParser()
    # Preserves the case sensitive in the parser...
    config.optionxform = str
    config.read(cfile.absolute())
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
    Given a ConfigParser and a Section key, it returns a dictionary
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
