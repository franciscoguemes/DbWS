



## Proposal for a context structure

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
