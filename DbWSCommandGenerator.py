#!/usr/bin/python3

# This script you can copy/paste your command like you would use it in your command line and
# you will get as result the same command but inside an array like DbWS would transform it in
# order to use it.
#
# See:
#   https://docs.python.org/3.6/library/shlex.html
#   https://www.endpoint.com/blog/2015/01/28/getting-realtime-output-using-python
#
##########################################################################################
import shlex

# Copy here your command:
command = 'chromium --window-position=3900,0 --profile-directory=Default --new-window https://github.com/franciscoguemes/online-tools https://franciscoguemes.com/'
dbws_command = shlex.split(command)
print(dbws_command)