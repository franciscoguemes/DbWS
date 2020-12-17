
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

##Context Object




#Example
Below you have an example that illustrates the different possibilities and the flexibility that offers the context file
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
