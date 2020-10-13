#!/usr/bin/python3

import sys
from pathlib import Path
import configparser

DEFAULT_CONFIG_FILE = "DbWS.conf"
DEFAULT_CONFIG_DIR = "/home/francisco/.config/DbWS"

def main():
    print("Parse arguments...")
    # TODO: Parse arguments
    print("Load configuration...")
    load_configuration()
    print("Parse Contexts...")
    # TODO: Parse contexts
    # http://commons.apache.org/proper/commons-cli/
    #   When parsing context arguments remember that:
    #       GNU --> Need the "=" character
    #       POSIX --> Do not need to add any characters
    #   When building up the entire command from the parsed JSON remember that:
    #       You need to substitute the defined variables in the configuration file...
    #       Some profiles of Chromium have scaped double quotes in the Context definition because the quotes are needed for the command line
    print("Show initial window...")

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
    config.read(cfile.absolute())
    check_config(config)

    #chrome_bookmarks_file = config['LOCAL']['CHROME_BOOKMARKS_FILE']


def check_config(config):
    if 'LOCAL' not in config:
        msg = "The configuration file must have a section called [LOCAL]." + "\n "
        msg += """Please have a look at the documentation of the project and edit the config file in the pertinent way.
        More info about config files on: https://docs.python.org/3/library/configparser.html
        """
        sys.exit(msg)
    #TODO: Check the rest of the configuration parameters here...


if __name__ == "__main__":
    main()
