#Logging file

The logging file is supposed to supply the logging configuration to the DbWS.
If you do not know anything about logging configurations, do not get worry.
Just simply create a file like the one in the next section (Default configuration),
with just a couple of changes, that will work fine to you.

##Default configuration

Below you have the default configuration. This configuration will log all the 
statements in the console and in a file. 

If you do not want to have a logging file in your system simply remove the 
definition of fileHandler ([handler_fileHandler]), and any reference to it in the file. 
That will cause that DbWS will only log the output in the console.

On the other hand side if you only want to have logging output in the file but
not in the console, then remove any reference to consoleHandler from the file,
included the definition ([handler_consoleHandler]).

In case of going for the option fo the fileHandler, please remember to create
first the directory structure where the logging file will be and ensure the
application will have enough permissions to write and create files in that 
directory.

```bash

[loggers]
keys=root,DbWS

[handlers]
keys=consoleHandler, fileHandler

[formatters]
keys=simpleFormatter

[logger_root]
level=INFO
handlers=consoleHandler, fileHandler
propagate=0

[logger_DbWS]
level=DEBUG
handlers=consoleHandler, fileHandler
qualname=DbWS
propagate=0

[handler_consoleHandler]
class=StreamHandler
level=INFO
formatter=simpleFormatter
args=(sys.stdout,)

[handler_fileHandler]
class=FileHandler
level=DEBUG
formatter=simpleFormatter
args=('/var/log/DbWS/DbWS.log', 'a', 'UTF-8',)

[formatter_simpleFormatter]
format=%(asctime)s.%(msecs)d - %(levelname)s - %(filename)s - %(lineno)d - %(funcName)s - %(message)s
datefmt=%Y%m%d %H:%M:%S

```

##Customized configuration

If you have more practice with Python logging or you want to simply try to customize the
logging in your system you can check the following resources and adapt the logging of DbWS
entirely to your needs.

  - [Logging HOWTO](https://docs.python.org/3.6/howto/logging.html)
  - [Logging cookbook](https://docs.python.org/3.6/howto/logging-cookbook.html#logging-cookbook)
  - [Time and date formatting](https://docs.python.org/3.6/library/time.html#time.strftime)
