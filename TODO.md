----


    Allow the Argument to be a call to an Application
        The application call can be in the "value" attribute of the argument --> One single value
            GNU or POSIX
        The application call can be the entire argument definition --> Array of values (with 1 single value GNU or multiple values POSIX)

        The application can return
            a single string ("value" attribute as application call)
                The right part of a GNU argument (single string)
                The value of a POSIX argument (array of strings)
            an array of strings (entire argument definition as application call)
                The entire argument is basically the outcome of the application, this array of string may contain:
                1 single value --> GNU argument
                multiple values --> 1 POSIX argument
                                    N POSIX arguments
                                    N GNU arguments


    Define "Context" JSON schema
    Validate "Context" file against JSON schema
        https://json-schema.org/understanding-json-schema/reference/numeric.html#number
        https://www.jsonschemavalidator.net/
        https://jsoneditoronline.org/#left=local.guqefa&right=local.kowije
        https://github.com/Julian/jsonschema/issues/260
        https://stackoverflow.com/questions/63735271/do-we-have-a-concept-of-checked-and-unchecked-exceptions-in-python
        https://stackoverflow.com/questions/1319615/proper-way-to-declare-custom-exceptions-in-modern-python



    Have a look at the different regex in Python:
        https://www.w3resource.com/python-exercises/re/python-re-exercise-47.php

/**********************************************************************************************************************/

----


#Application
1. In the class Application line 70. Review the error case.
1. In the class Parameter test the method "getValue" and inside this the call to : the_string_represents_an_array_of_strings
1. Parse command line arguments 
    1. Parse the argument for the configuration file "--config"
    2. Parse the argument for the logging configuration file "--logging"
2. Improve the [logging](https://docs.python.org/3.6/howto/logging.html)
``` 
        if no logging configuration file is supplied
            Establish a default logging configuration
        else
            Read the logging configuration from a file
```

#Documentation

## README.md
1. Explain the Context definition in the CONTEXT.md file. Do not forget to mention the JSON
   schema versions.
1. After the "Usage" section create a section explaining how to execute DBwS automatically
after login in the OS.
1. Create a file with the takeaways of the project.


#Future functionality
- Recognise the Network you are connected at
    - i.e. Start the VPN when I am connected at home and I work at Uniscon
		    https://askubuntu.com/questions/57339/connect-disconnect-from-vpn-from-the-command-line
    - i.e. Start the VPN when I am connected anywhere outside of the office and I work at Uniscon
    - i.e. Do NOT start the VPN when I am at the office
- Think about the different Workflows:
    - The computer starts and the user decides on what to work (Usual case scenario)
    - The user is working in a Context and decides to start working in a different Context
        - Store the last Context you were working in
        - Offer the option of closing the Context
        - Offer the option to switch to another Context
        - See when was the last reboot: https://unix.stackexchange.com/questions/131775/how-long-has-my-linux-system-been-running


    
----
	
   
# Future Lines of Work
- Integrate this project with the iworkin project. Inside the concept of Context, the project _iworkin_ can be 
seen as just another application more to execute when the user switch to that context.
- Integrate with Dragonfire
	- https://medium.com/@hkdb/siri-alternative-for-ubuntu-a6bc6825b9ad
	- http://dragon.computer/

#Contexts to create

##my Website:
    Open the Hosting page
    Open Filezilla
    Open the browser showing the page in desktop
    Open the browser showing the page in mobile
    Docker container with the Apache web server + PHP installed ???

##MDWiki:
    Open a terminal in the directory of the project
    Open [VS Code](https://code.visualstudio.com/docs/editor/command-line) with the wiki project
    Open the Hosting page
    Open the Manage packet in the hosting area
    Open the browser showing the wiki in the hosting (the real one)
    Start the python_web_server in the directory of the MDWiki project in local
    Open the browser showing the wiki in the local environment

##DbWS:
    Open [PyCharm](https://www.jetbrains.com/help/pycharm/working-with-the-ide-features-from-command-line.html) with the DbWS project
    Open a terminal in the directory of the project
    Open with the text editor the files
        contexts.json
        DbWS.conf
        logging.conf ???
    Open the browser showing the Markdown Bookmarks