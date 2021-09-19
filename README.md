
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
considered a Context. For the user to work in "Project X" (That is an specific context) 
the system will have to open a series of applications (i.e. Eclipse IDE, the browser, 
etc ...) each of this applications with a specific configuration (i.e. Eclipse IDE with 
the Workspace _A_ and the Working Set _W_, the browser may need to be logged as an 
specific user, etc ...), all of these together, the applications plus their startup 
configuration is what is known as a Context.

## Changing contexts

When a user is working in multiple projects (i.e. Working at a company and also in his 
free time being involved in some different personal projects (i.e. A personal site, 
or contributing to an open source app)) simultaneously one of the things that creates 
a bigger mental fatigue is to switch between Contexts. Open all the required apps with 
the desired configuration. Just to setup the environment for start working may take a 
while to the user. The main aim of this project is to reduce this mental fatigue by 
setting up automatically these contexts for the user, allowing the user to switch 
smoothly from one context to another and focus on what really creates value for him.

## What does DbWS in reality?
This project is the basis for the DbWS (Develop by Wire System) which pretends to 
automatize all routine tasks that I personally carry out every day as a developer.
Some of these tasks are:

- Select the computer set up on startup. Choose whether you will be working in a:
	- Company project
	- Personal project
	- Other tasks... (I.e. You switch on the computer just to reply some email).

Once the user has decided in which project is he/she going to work, then DbWS will
do the following:

- Based on the chosen context, DbWS will set up your environment for the chosen 
task, this may include:
	- Open browsers
	- Start the IDE
	- Show the status of the Docker containers
	- Etc ...

## Installation
Clone this repository to your computer or simply download the project from GitHub to your local computer. After that
run the script install.sh that is inside the project. This script will do all the job for you from installing needed
packages in your OS to creating a Python virtual environment. Feel free to have a look at the script before execute it!

## Configuration
In order to configure DbWS you will need to create a configuration file so please have a look 
to the file [CONFIG_FILE.md](https://github.com/franciscoguemes/DbWS/blob/master/CONFIG_FILE.md).

Once you have created your configuration file, your next step will be to define the different 
contexts you will be using. For this purpose, please have a look to the file 
[CONTEXTS_FILE.md](https://github.com/franciscoguemes/DbWS/blob/master/CONTEXTS_FILE.md).

Finally, you will need to create a logging file to supply the logging configuration. See the 
section [LOGGING_FILE.md](https://github.com/franciscoguemes/DbWS/blob/master/LOGGING_FILE.md)
for this purpose.

## Usage
Execute in a terminal the command _DbWS_ as in the example below.
```console
/path/to/DbWS/directory/DbWS.py --config=/path/to/my/config_file --logging=/path/to/my/logging_file
```

As you see this is quite laborious and prone to error, hence I recommend you to take the script DbWS.sh
supplied in the project and adapt it consequently to your environment. Below you can see as an example
the content of the file DbWS.sh.

```bash
DbWS_DIRECTORY=/home/francisco/git/Francisco/github/DbWS
CONFIG_DIRECTORY=/home/francisco/.config/DbWS

$DbWS_DIRECTORY/DbWS.py --config=$CONFIG_DIRECTORY/DbWS.conf --logging=$CONFIG_DIRECTORY/logging.conf
```

In order to ease even more the execution of the script DbWS.sh you can place the file in some directory 
included in your [$PATH](https://opensource.com/article/17/6/set-path-linux) variable. By doing that you 
will be able to execute the DbWS with just typing the command anywhere in a terminal.

If you want DbWS to be executed automatically every time you log into Ubuntu follow
[this instructions](https://askubuntu.com/a/48327). 

In case of using any other Linux distribution or Unix based OS, you will need to follow 
specific instructions for your OS since DbWS is a GUI app instead a 
command line tool, therefore it may happen that you will not see the 
window right after login despite the app is being executed.

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[APACHE](http://www.apache.org/licenses/LICENSE-2.0)


----

This README file was made following the recommendations of [makereadme.com](https://www.makeareadme.com/)