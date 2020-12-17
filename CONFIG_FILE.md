#Configuration file

##Default location
The default location for the configuration file is:
```
~/.config/DbWS/DbWS.conf 
```
So if no configuration file is specified in the command line during the
execution, the application will try to read the default one.

##Format
The configuration of DbWS is based on the [configparser Python module](https://docs.python.org/3.6/library/configparser.html)
which expects to parse files with the [INI File Structure](https://docs.python.org/3.6/library/configparser.html#supported-ini-file-structure).

###Sections
The DbWS expects to have at least the following sections:

| Section     | Mandatory          |
| ----------- | ------------------ |
| LOCAL       | :heavy_check_mark: |
| ENVIRONMENT | :heavy_check_mark: |

####LOCAL
The _LOCAL_ section is mandatory, and it must contain the following variables:

| Section       | Mandatory   | Example value                 | Meaning                              |
| ------------- | ----------- | ----------------------------- | ------------------------------------ |
| CONTEXTS_FILE | :heavy_check_mark:         | ~/.config/DbWS/contexts.json  | Path to the context file definition  |

####ENVIRONMENT
The _ENVIRONMENT_ section is mandatory, but the variables contained inside are
optional since you have to define here the properties (key-value pairs) that will be 
used to interpolate the environment variables in your context definition.

I.e. You could define as property the following:
```
MY_APP=/home/myUser/path/to/my/app/executable.file
```

Later on, in your context definition you might mention multiple times the path
to the application _MY_APP_, so instead of scattering your context definition
by copying/pasting the path, you can use _$MY_APP_ as environment variable in your 
context. 

DbWS interpolates environment variables (environment variables start with the character 
"$") in the context definition against property definitions contained in the _ENVIRONMENT_ 
section of the configuration file.


##Example
The following configuration file is the one I personally use. My environment
properties might not be of any use to you, but you can have an idea of how it
looks like a configuration file and what can you achieve with it.

```
# ----------------------------------------------------------------------
#                   LOCAL CONFIGURATION
# ----------------------------------------------------------------------
[LOCAL]
CONTEXTS_FILE = /home/francisco/.config/DbWS/contexts.json


# ----------------------------------------------------------------------
#                   ENVIRONMENT VARIABLES
# ----------------------------------------------------------------------
[ENVIRONMENT]
ECLIPSE_PATH=/home/francisco/eclipse/java-photon/eclipse
ECLIPSE_UNISCON_WORKSPACE=/home/francisco/workspaces/uniscon
ECLIPSE_PERSONAL_WORKSPACE=/home/francisco/workspaces/personal-projects
ECLIPSE_BAELDUNG_WORKSPACE=/home/francisco/workspaces/baeldung

LEFT_UPPER_CORNER_XPS13=110x24+86+110
RIGHT_UPPER_CORNER_XPS13=80x24+1180+110
LEFT_DOWN_CORNER_XPS13=80x24+86+610
RIGHT_DOWN_CORNER_XPS13=80x24+1180+610

THIRD_MONITOR_LEFT_UPPER_CORNER_XPS=3900,0


CHROME_BOOKMARKS_APP_DIR=/home/francisco/git/Francisco/github/chrome_bookmarks
CHROME_BOOKMARKS_APP_CONFIG_FILE=/home/francisco/conf/chrome_bookmarks/chrome_bookmarks.conf

CHROMIUM_PROFILE_FRANCISCO=Default
CHROMIUM_PROFILE_UNISCON=Profile\ 1

GMAIL=https://mail.google.com/mail/u/0/#inbox
EVERNOTE=https://www.evernote.com/Login.action
UNISCON_OUTLOOK=https://outlook.office.com/owa/?realm=uniscon.net
IDGARD=https://my.idgard.de/#/login
AHA=https://uniscon.aha.io/products/SP/strategic_imperatives
UNISCON_CONFLUENCE=https://confluence.uniscon-rnd.de/display/BAC/Backoffice
UNISCON_JIRA=https://jira.uniscon-rnd.de/browse/PM-33
OLD_UNISCON_GITLAB=https://gitlab.uniscon-rnd.de/users/sign_in
UNISCON_GITLAB=https://gitlab.com/uniscon/sp/backlog
LEO=https://dict.leo.org/spanisch-deutsch
WORDREFERENCE=http://www.wordreference.com/es/en/translation.asp
```