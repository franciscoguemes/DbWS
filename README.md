
# DbWS (Develop by Wire System)

The DbWS is a tool that pretend to assist the developers that works into multiple
projects in the daily basis in the process of changing from one project to another.

Switching contexts is one of the most brain power demanding tasks. From a cognitive
point of view a person needs between 20 to 30 minutes to fully concentrate into a new
task. On top of that we have to add the effort of opening all the required apps with 
the desired configuration. Just to setup the environment for start working may take a 
while to the user. The main aim of this project is to reduce this mental fatigue by 
setting up automatically these working environment (context) for the user, allowing 
the user to switch smoothly from one context to another and focus on what really 
creates value for him.

This project is a tool aimed to integrate with the OS and save part of the effort
to the developers by setting up the entire working environment for a defined project.

## How does it work

DbWS is based on the idea of multiple contexts. Each context represent the needed
environment to work in a project. Thus, a user that works in multiple projects in its
daily basis would have to setup multiple contexts for DbWS. Once the contexts are setup
the user can easily switch from one context (project, task, etc...) to another very
easily, just by saying to the DbWS that he wants to change to the other project.

## What is a context?
A "Context" is what a user can 
conceptually do i.e. A user may work in Project X, then working in "Project X" may be 
considered a Context. For the user to work in "Project X" (That specific context) 
the system will have to open a series of applications (i.e. Eclipse IDE, the browser, 
etc ...) each of this applications with a specific configuration (i.e. Eclipse IDE with 
the Workspace _A_ and the Working Set _W_, the browser may need to be logged as an 
specific user, etc ...), all of these together, the applications plus their startup 
configuration is what is known as a Context.

## Changing contexts

When a user is working in multiple projects (i.e. Working at a company and also in his 
free time working in some different personal projects (i.e. Building a personal site, 
or contributing to an open source app)) simultaneously one of the things that creates 
a bigger mental fatigue is to switch between Contexts. Open all the required apps with 
the desired configuration. Just to setup the environment for start working may take a 
while to the user. The main aim of this project is to reduce this mental fatigue by 
setting up automatically these contexts for the user, allowing the user to switch 
smoothly from one context to another and focus on what really creates value for him.

## What does DbWS in reality?
This project is the basis for the DbWS (Develop by Wire System) which pretends to 
automatize all routinary tasks that as a developer I carry out every day such as:

- Select the computer set up on startup. Choose whether you will be working in a:
	- Company project
	- Personal project
	- Other tasks... (I.e. You switch on the computer just to reply some email).

Once the user has decided in which project is he/she going to work, then DbWS will
do the following:

- Based on the chosen context, DbWS will set up your environmnet for the chosen 
task, this may include:
	- Open browsers
	- Start the IDE
	- Show the status of the Docker containers
	- Etc ...



# TODO:
1. Define exactly what is a Context and which attributes will have the context --> JSON or XML ???
2. Define different Contexts based on 1.
3. Make the UI of the app to generate automatically based on the supplied set of contexts ...
4. Be able to open the different apps with the desired configurations.
5. Integrate the concept of Context with the project _iworkin_ --> _iworkin_ can be 
seen as just another application more to execute when the user switch to that context.
	

# Future Lines of Work
- Integrate this project with the iworkin project
- Integrate with Dragonfire
	- https://medium.com/@hkdb/siri-alternative-for-ubuntu-a6bc6825b9ad
	- http://dragon.computer/


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
