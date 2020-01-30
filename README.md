In the future this project will be based on Contexts. A "Context" is what a user can coceptually do i.e. A user may work in Project X, then working in "Project X" may be considered a Context.
For the user to work in "Project X" (That specific context) the system will have to open a series of applications (i.e. Eclipse IDE, the browser, etc ...) each of this applications with a specific configuration (i.e. Eclipse IDE with the Workspace A and the Working Set W, the browser may need to be loged as an specific user, etc ...), all of these together, the applicaitons plus their startup configuration is what is known as a Context.

When a user is working in multiple projects (i.e. Working at a company and also in his free time working in some different personal projects (i.e. Building a personal site, or contributing to an open source app)) simultaneously one of the things that creates a bigger mental fatigue is to switch between Contexts. Open all the required apps with the desired configuration. Just to setup the environment for start working may take a while to the user. The main aim of this project is to reduce this mental fatigue by setting up automatically these contexts for the user, allowing the user to switch smoothly from one context to another and focus on what really creates value for him.

TODO:
	0- Define exactly what is a Context and which attributes will have the context --> JSON or XML ???
	1- Define different Contexts based on 0.
	2- Make the UI of the app to generate automatically based on the supplied set of contexts ...
	3- Be able to open the different apps with the desired configurations.
	4- Integrate the concept of Context with the project "iworkin" --> "iworkin" can be seen as just another application more to execute when the user switch to that context.
	
	



This project is the basis for the DbWS (Develop by Wire System) which pretends to automatize all routinary tasks that as a developer I carry out every day such as:

	-Select the computer set up on startup. Choose whether you will be working in a:
		-Company project
		-Personal project
		-Other tasks... (I.e. You switch on the computer just to reply some email).

	-Based on these preferences the DbWS will set up your environmnet for the chosen task, this
	 may include:
		-Open browsers
		-Start the IDE
		-Show the status of the Docker containers
		-Etc ...


Future Lines of Work:
	Integrate this project with the iworkin project
	Integrate with Dragonfire
		https://medium.com/@hkdb/siri-alternative-for-ubuntu-a6bc6825b9ad
		http://dragon.computer/

Context{
	applications: [
		app{
			name: Eclipse
			path: /path/to/eclipse/executable
			configurations: [
				configuration{
					name: "username"
					option: "-u"
					value: "Francisco"
				},
				configuration{
					name: "Workspace"
					option: "-w"
					value: "/home/francisco/eclipse/workspace"
				}
				
			]
			
		}
	]
	
}
