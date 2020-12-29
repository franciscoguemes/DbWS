#Troubleshooting

During the usage of DbWS might appear weird problems that are not always easy to solve. Sometimes will be bugs in DbWS,
but some other times is due to the way we use DbWS. DbWS has been designed to be the most similar than using a command
line, but still there are many differences that are not obvious when it comes to the usage time.

This section contains the most common errors/problems that appears when using DbWS in a production environment.

## [Errno 2] No such file or directory
The error message is pretty obvious, the 
Please ensure that in your context file you are using the Python's module in charge of executing subprocesses 
([subprocess.Popen](https://docs.python.org/3.6/library/subprocess.html)) is not able to find the file you are
pointing at.

The following are the most common causes:
  - A typo in the path
  - A typo in an environment variable
      - You forgot to precede the environment variable with the "$" in the [CONTEXTS_FILE.md](https://github.com/franciscoguemes/DbWS/blob/master/CONTEXTS_FILE.md).
  - You forgot to add the environment variable to the [CONFIG_FILE.md](https://github.com/franciscoguemes/DbWS/blob/master/CONFIG_FILE.md),
therefore no interpolation is taking place.

## [Errno 8] Exec format error
[This error](https://stackoverflow.com/questions/27606653/oserror-errno-8-exec-format-error) is usually triggered 
because the Python's module in charge of executing subprocesses ([subprocess.Popen](https://docs.python.org/3.6/library/subprocess.html)) 
do not know how to really execute the script. The error is typically triggered by scripts that lacks of a proper 
[shebang](https://en.wikipedia.org/wiki/Shebang_(Unix)).

The solution is very simple, just add the [proper shebang](https://en.wikipedia.org/wiki/Shebang_(Unix)#Examples) to your script and try again.