
#What is a Context for DbWS?
A so called context in the universe of DbWS is a project or a set of tasks you are working on.
For DbWS there it is even more straight forward, a context is all the applications (and their respective 
configurations), commands and any other operations that you need to perform in your computer when you switch 
from one project (context) to another.  

#The Contexts file
The context file is a file that contains all the definitions of your different contexts in **JSON** format.
The contexts file can have any name and it can be in any directory, you just need to specify which is your contexts
file in the [configuration file](https://github.com/franciscoguemes/DbWS/blob/master/CONFIG_FILE.md).

#Formatting
The context file must be in **JSON** format.

##Validation
The context file will be validated internally against the corresponding [JSON Schema](https://json-schema.org/) 
stored in the directory _schemas_ inside DbWS code. Thus, if you already know the JSON Schema syntax, you can
directly go and see in the schema what is allowed and how the context file will look like. If not, do not worry
this page explains in detail all important aspects about the latest and greatest features available in the context
file.

__IMPORTANT NOTE__: The different JSON schemas are backwards compatible, this means that all that is valid for the 
schema 0.1 is valid in the newer versions of the schema. But for compliance reasons I recommend you to try to always 
stick to the latest version of the schema, due to at some point in the future the backwards compatibility might be 
broken. 

##Header
The file starts with a [JSON object](https://www.w3schools.com/js/js_json_objects.asp) that contains the header fields
which are simply some general purpose information fields. In the table below you can see a description of the fields:

| Field          | Mandatory          | Example value    | Description                                                                               |
|----------------|--------------------|------------------|-------------------------------------------------------------------------------------------|
| schema_version | :heavy_check_mark: | 0.3              | This field specifies against which schema version is gonna be the context file validated. |
| creator        | :x:                | Francisco Güemes | The author of the context file                                                            |
| date           | :x:                | 20201112         | The creation/last modification date of the file in 'YYYYmmdd' format                      |
| contexts       | :heavy_check_mark: |                  | An array of objects where each object correspond to a different context.                  |

Below you can see a JSON example of the header, with the fields described above that illustrates how would look like 
the skeleton of a contexts file.

```json
{
  "schema_version": 0.3,
  "creator": "Francisco Güemes",
  "date": "20201112",
  "contexts": [
    {
      Context object 1
    },
    {
      Context object 2
    },
    ...
    {
      Context object N
    }
  ]
}
```

##Context Object Definition
The context object definition contains the following fields:

| Field        | Mandatory          | Example value | Description                                                                                            |
|--------------|--------------------|---------------|--------------------------------------------------------------------------------------------------------|
| name         | :heavy_check_mark: | "Project X"   | The name you want to assign to the specific context                                                    |
| applications | :heavy_check_mark: |               | An array of JSON objects which each object of the array represent an application (command) to execute. |

##Application Object Definition
The application object represents an application (or command) to be executed by DbWS and is composed by the following
fields:

| Field      | Mandatory          | Example value                 | Description                                                                                       |
|------------|--------------------|-------------------------------|---------------------------------------------------------------------------------------------------|
| name       | :heavy_check_mark: | Eclipse                       | The name of the application. It can be any name not neccessarly the name of the real application. |
| path       | :heavy_check_mark: | /path/to/the/excecutable/file | Path to the executable file of the application                                                    |
| arguments  | :x:                |                               | An array of JSON objects on which each object of the array represent an argument.                 |
| parameters | :x:                |                               | An array of JSON objects on which each object of the array represent a parameter.                 |

##The *NIX command metaphor
For DbWS each application object is equivalent to a command that is executed in the terminal of the OS (Operative 
System), therefore each application object has the same structure as a command would have in the OS's terminal:

```bash
command -argument1 -argument2 list_of_parameters
```
I.e. 

```bash
ls -la /home/myuser/Documents
```

__NOTE__: Same as with the commands of the Linux terminal, the arguments and parameters of the application objects in 
DbWS are optional. I.e. You can just type in your Linux terminal: "_ls_", and the command is executed despite it 
contains no arguments or parameters. Is the responsibility of the final user to supply the right arguments and 
parameters. 

The metaphor is not just limited to copy the structure of the commands in the terminal, it also allows to chain multiple
commands (application objects). In the terminal you might chain multiple commands by using pipes like in the following
example:

```bash
cat sample.txt | grep -v a | sort - r
```

With DbWS you could achieve the same by chaining multiple application objects like you will see in the final example of
this file. Not only that but DbWS also allows you to use the output of an application as argument of another, or to use
an application as parameter of another.

##Argument Object Definition
The argument object contains the following fields:

| Field      | Mandatory          | Example value     | Description                                                                       |
|------------|--------------------|-------------------|-----------------------------------------------------------------------------------|
| type       | :heavy_check_mark: | GNU               | The type of the argument. There are only 2 types: "GNU" and "POSIX".              |
| argument   | :heavy_check_mark: | --argument_option | The argument option                                                               |
| value      | :x:                | argument_value    | The value for the argument                                                        |

I.e. A GNU argument definition in the command line would look like
```bash
command --gnu_argument argument_value
```

The equivalent in DbWS would be:
```json
...
            {
              "type": "GNU",
              "argument": "--gnu_argument",
              "value": "argument_value"
            },
...
```

--NOTE__: In the previous example of argument definition the hyphens are included in the value of the field "argument"
. It is mandatory that you include the right amount of hyphens in the "argument" field of the Argument object due to
sometimes is one single hyphen, and some other times is two, therefore it is impossible for DbWS to automatically add
the hyphens to the arguments.


I.e. A POSIX argument definition in the command line would look like
```bash
command -posix_argument=argument_value
```

The equivalent in DbWS would be:
```json
...
            {
              "type": "POSIX",
              "argument": "-posix_argument",
              "value": "argument_value"
            }
...
```

__NOTE__: In the previous example of POSIX argument definition the "=" sign that separates the argument from its value
is not included anywhere in the JSON definition. Since the equals sign is always there, DbWS will automatically add it
for you in the terminal when executing the application.


##Parameter Object Definition
The paramter object contains the following fields:

| Field      | Mandatory          | Example value     | Description                                                                       |
|------------|--------------------|-------------------|-----------------------------------------------------------------------------------|
| value      | :heavy_check_mark: | my_value          | The value of the argument as string of text                                       |

I.e. A parameter definition in the command line would look like
```bash
command parameter1 parameter2 ... parameterN
```

The equivalent in DbWS would be:
```json
...
            {
              "value": "parameter1"
            },
            {
              "value": "parameter2"
            },
            ...
            {
              "value": "parameterN"
            },
...
```


#Example
Below you have an example that illustrates the different possibilities, and the flexibility that offers the context file
in DbWS

```json
{
  "schema_version": 0.3,
  "creator": "Francisco Güemes",
  "date": "20201112",
  "contexts": [
    {
      "name": "App call as argument 0",
      "applications": [
        {
          "name": "Eclipse",
          "path": "$ECLIPSE_PATH/eclipse",
          "arguments": [
            {
              "name": "echo",
              "path": "echo",
              "arguments": [
                {
                  "type": "POSIX",
                  "argument": "-e"
                }
              ],
              "parameters": [
                {
                  "value": "-data\n"
                },
                {
                  "value": "$ECLIPSE_PERSONAL_WORKSPACE"
                }
              ]
            }
          ]
        }
      ]
    },
    {
      "name": "App call as argument",
      "applications": [
        {
          "name": "Eclipse",
          "path": "$ECLIPSE_PATH/eclipse",
          "arguments": [
            {
              "name": "echo",
              "path": "echo",
              "arguments": [
                {
                  "type": "POSIX",
                  "argument": "-e"
                }
              ],
              "parameters": [
                {
                  "value": "['-data','$ECLIPSE_PERSONAL_WORKSPACE']"
                }
              ]
            }
          ]
        }
      ]
    },
    {
      "name": "App call in arg value",
      "applications": [
        {
          "name": "Eclipse",
          "path": "$ECLIPSE_PATH/eclipse",
          "arguments": [
            {
              "type": "POSIX",
              "argument": "-data",
              "value": {
                "name": "echo",
                "path": "echo",
                "parameters": [
                  {
                    "value": "$ECLIPSE_PERSONAL_WORKSPACE"
                  }
                ]
              }
            }
          ]
        }
      ]
    },
    {
      "name": "Eclipse Test",
      "applications": [
        {
          "name": "Eclipse",
          "path": "$ECLIPSE_PATH/eclipse",
          "arguments": [
            {
              "type": "POSIX",
              "argument": "-data",
              "value": "$ECLIPSE_PERSONAL_WORKSPACE"
            }
          ]
        }
      ]
    },
    {
      "name": "Simple thingy",
      "applications": [
        {
          "name": "Eclipse",
          "path": "$ECLIPSE_PATH/eclipse",
          "arguments": [
            {
              "type": "POSIX",
              "argument": "-data",
              "value": "$ECLIPSE_PERSONAL_WORKSPACE"
            }
          ]
        },
        {
          "name": "Chromium",
          "path": "chromium",
          "arguments": [
            {
              "type": "GNU",
              "argument": "--window-position",
              "value": "$THIRD_MONITOR_LEFT_UPPER_CORNER_XPS"
            },
            {
              "type": "GNU",
              "argument": "--profile-directory",
              "value": "$CHROMIUM_PROFILE_FRANCISCO"
            },
            {
              "type": "GNU",
              "argument": "--new-window"
            }
          ],
          "parameters": [
            {
              "name": "open_bookmarks",
              "path": "$CHROME_BOOKMARKS_APP_DIR/chrome_bookmarks.py",
              "arguments": [
                {
                  "type": "GNU",
                  "argument": "--config",
                  "value": "$CHROME_BOOKMARKS_APP_CONFIG_FILE"
                }
              ],
              "parameters": [
                {
                  "value": "/Personal/Login screen"
                }
              ]
            }
          ]
        }
      ]
    },
    {
      "name": "Other projects",
      "applications": []
    }
  ]
}
```




----

----

```json
[
  {
    "name": "Context 1",
    "applications": [
      {
        "name": "Eclipse",
        "path": "/path/to/eclipse/executable",
        "arguments": [
          {
            "type": "POSIX",
            "argument": "-data",
            "value": "/path/to/eclipse/workspace"
          }
        ]
      },
      {
        "name": "Chromium",
        "path": "/path/to/chromium/executable",
        "arguments": [
          {
            "type": "GNU",
            "argument": "--profile-directory",
            "value": "chromium_profile"
          },
          {
            "type": "GNU",
            "argument": "--new-window",
            "value": ""
          }
        ],
        "parameters": [
          {
            "name": "Some optional name",
            "value": "some_url_1"
          },
          {
            "name": "Some optional name",
            "value": "some_url_2"
          },
          {
            "name": "Some optional name",
            "value": "some_url_3"
          },
          {
            "name": "Some optional name",
            "value": "some_url_4"
          }
        ]
      }
    ]
  },
  {
    "name": "Context 2",
    "applications": [
      {}
    ]
  }
]
```

#Troubleshooting
In order to create a good and efficient context file it is important to understand what is allowed and not allowed to do
in the context definitions for DbWS.

##Application call as argument
An argument object definition can be fully replaced by an application object definition. See the example below.

```json
    {
      "name": "App call as argument",
      "applications": [
        {
          "name": "Eclipse",
          "path": "$ECLIPSE_PATH/eclipse",
          "arguments": [
            {
              "name": "echo",
              "path": "echo",
              "arguments": [
                {
                  "type": "POSIX",
                  "argument": "-e"
                }
              ],
              "parameters": [
                {
                  "value": "['-data','$ECLIPSE_PERSONAL_WORKSPACE']"
                }
              ]
            }
          ]
        }
      ]
    }
```
The result of a calling the application supplied as argument is an array of strings that simply represents the results 
of the application call. In this case the user has the entire responsibility of providing an application definition
whose result call is a valid (or a sequence of valid) GNU or POSIX argument(s) for the given command. The following
outcome examples are handled gracefully by the application:

```
    GNU   --->  ["argument=value"]
    GNU   --->  ["argument1=value1", "argument2=value2", ..., "argumentN=valueN"]
    POSIX --->  ["argument", "value"]
    POSIX --->  ["argument1", "value1", "argument2", "value2", ..., "argumentN", "valueN"]
```

The example above would produce as result the code below, which would be handled gracefully by the application.
```bash
['-data','$ECLIPSE_PERSONAL_WORKSPACE']
```


##Application call as argument value
Let's assume we have the application object definition showed below. 

__NOTE__: The application object definition below produces the same result as the example in the previous section.

```json
        {
          "name": "Eclipse",
          "path": "$ECLIPSE_PATH/eclipse",
          "arguments": [
            {
              "type": "POSIX",
              "argument": "-data",
              "value": {
                "name": "echo",
                "path": "echo",
                "parameters": [
                  {
                    "value": "$ECLIPSE_PERSONAL_WORKSPACE"
                  }
                ]
              }
            }
          ]
        }
```

In the example we can see that the application object has a single argument object definition.
The argument object definition instead of supplying a value, it gets the value as result of calling a different
application object. In this case the user is fully responsible for warranting that the application will return a single
value and not an array of values.


##Application call as parameter
In the code following example we have an application object definition on which the parameter object definition has 
been replaced by another application object definition.

In other words the results of an application call can be used as the parameter of another application.

```json
        {
          "name": "Chromium",
          "path": "chromium",
          "arguments": [
            {
              "type": "GNU",
              "argument": "--window-position",
              "value": "$THIRD_MONITOR_LEFT_UPPER_CORNER_XPS"
            },
            {
              "type": "GNU",
              "argument": "--profile-directory",
              "value": "$CHROMIUM_PROFILE_FRANCISCO"
            },
            {
              "type": "GNU",
              "argument": "--new-window"
            }
          ],
          "parameters": [
            {
              "name": "open_bookmarks",
              "path": "$CHROME_BOOKMARKS_APP_DIR/chrome_bookmarks.py",
              "arguments": [
                {
                  "type": "GNU",
                  "argument": "--config",
                  "value": "$CHROME_BOOKMARKS_APP_CONFIG_FILE"
                }
              ],
              "parameters": [
                {
                  "value": "/Personal/Login screen"
                }
              ]
            }
          ]
        }
```

__NOTE__: The application object definition used as parameter of the main application object can return a single value
, a string representation of a Python array of values or multiple strings. All will be handled gracefully by DbWS.