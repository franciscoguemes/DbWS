

----

    If we would translate the CallToApplication parameter as pure JSON, the result would be an array of
    JSON objects of type parameter. See in the JSON configuration file examples of the value "parameters".
    "parameters": [
              {
                "value": "/Personal/\"Login screen\""
              }
            ]


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
1. Improve the error message when an environment variable in the contexts.json file can not be interpolated 
   because it does not exist in the DbWS.config file. Handle this case gracefully.
2. Improve the error handling (and message) when a comma (or any other element) is missing in the JSON file
   and the application fails on parsing the contexts.json file.
3. In the class Application line 70. Review the error case.
4. Look at the console errors when selecting the option "Simple thingy".
5. Improve the [logging](https://docs.python.org/3.6/howto/logging.html)
    4. Save context data with the errors in the logging file.
6. Create test cases
    1. Create a test case that includes a call to the method Context.transform_string_to_array_of_strings
7. Once the user selects an option the application closes automatically
8. The icon shows in the launcher the right icon
9. Remove the limitation of contexts that the UI can handle (WindowBuilder.py)

#Documentation

## README.md
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
- Close opened contexts:
    - [Get a list of open windows in Linux](https://superuser.com/questions/176754/get-a-list-of-open-windows-in-linux?answertab=votes#tab-top)
    - [How can I get a list of all open windows in the command line?](https://askubuntu.com/questions/23427/how-can-i-get-a-list-of-all-open-windows-in-the-command-line)
    - [Close active window from terminal](https://askubuntu.com/questions/183771/close-active-window-from-terminal)

    
----
	
   
# Future Lines of Work
- Integrate this project with the iworkin project. Inside the concept of Context, the project _iworkin_ can be 
seen as just another application more to execute when the user switch to that context.
- Integrate with Dragonfire
	- https://medium.com/@hkdb/siri-alternative-for-ubuntu-a6bc6825b9ad
	- http://dragon.computer/

#Contexts to create

##my Website:
    Open the browser showing the page in desktop
    Open the browser showing the page in mobile