#!/usr/bin/env bash

DbWS_DIRECTORY=`dirname $0`
DbWS_APP=$DbWS_DIRECTORY/DbWS.py
DbWS_VENV=$DbWS_DIRECTORY/venv
CONFIG_DIRECTORY=/home/francisco/.config/DbWS

# Setup the virtual environment as default python3 environment
source $DbWS_VENV/bin/activate

#****************************************************************************************************
# Debug
#****************************************************************************************************
# Prints the executables that are being used (You may have multiple installations or virtual environments)
# which pip
# which python3

# Start the application
$DbWS_APP --config=$CONFIG_DIRECTORY/DbWS.conf --logging=$CONFIG_DIRECTORY/logging.conf