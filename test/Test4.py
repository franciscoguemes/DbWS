#!/usr/bin/python3
import subprocess

# The command only works if each item is a string in the array
# See examples: https://www.programcreek.com/python/example/50/subprocess.Popen
full_command = [
    'ls',
    '-l', '-a', '--block-size=M']

application = subprocess.Popen(full_command, stdout=subprocess.PIPE)
application.wait()
result = application.communicate()[0]
print(type(result))
result = result.decode("utf-8")
print(result)

exit("Hawai")