#!/bin/bash

DbWS_DIRECTORY=/home/francisco/git/Francisco/github/DbWS
CONFIG_DIRECTORY=/home/francisco/.config/DbWS

cd $DbWS_DIRECTORY
./DbWS.py --config=$CONFIG_DIRECTORY/DbWS.conf --logging=$CONFIG_DIRECTORY/logging.conf