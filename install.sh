#!/usr/bin/env bash


get_python3_version () {
  string_array=(`python3 --version`)
  major=$(echo ${string_array[1]} | cut -d. -f1)
  minor=$(echo ${string_array[1]} | cut -d. -f2)
  echo $major.$minor
}

get_package_name () {
  package_name="python$(get_python3_version)-venv"
  echo $package_name
}

# Create the logging directory (Must match the one defined in file logging.conf)
LOGGING_DIR=/var/log/DbWS
sudo mkdir -p $LOGGING_DIR
sudo chgrp $USER $LOGGING_DIR
sudo chmod 775 $LOGGING_DIR

# Install the package to create virtual environments (if needed)
sudo apt-get install $(get_package_name)

# Install tkinter package in your system. It is not possible to install tkinter with pip
# See: https://stackoverflow.com/a/65288593/1866109
sudo apt-get install python3-tk

# Create the virtual environment
DbWS_DIRECTORY=`dirname $0`
DbWS_VENV=$DbWS_DIRECTORY/venv

# Delete the virtual environment if it already exists
rm -Rf $DbWS_VENV
# Create the environment
python3 -m venv $DbWS_VENV
source $DbWS_VENV/bin/activate

# Install the necessary packages in the virtual environment
python3 -m pip install -r $DbWS_DIRECTORY/requirements.txt

#****************************************************************************************************
# Debug
#****************************************************************************************************
# Prints the executables that are being used (You may have multiple installations or virtual environments)
# which pip
# which python3


# List installed pip modules. If pip is not installed (it depends which one
# it trying to use the one in venv or in your OS) you will see the following output:
# /usr/bin/python3: No module named pip
python3 -m pip list