#!/usr/bin/python3
import shlex
import subprocess

# full_command = ['chromium', '--window-position=3900,0', '--profile-directory=Default', '--new-window', 'https://github.com/franciscoguemes/online-tools https://franciscoguemes.com/ https://www.google.com/search?q=spring+web+app&oq=spring+web+app&aqs=chrome..69i57j69i65.5880j0j1&client=ubuntu&sourceid=chrome&ie=UTF-8 https://spring.io/guides/gs/spring-boot/#initial https://spring.io/guides/gs/serving-web-content/ https://start.spring.io/ https://dzone.com/articles/gradle-vs-maven https://github.com/spring-projects/spring-petclinic/blob/master/pom.xml https://help.github.com/en/github/importing-your-projects-to-github/adding-an-existing-project-to-github-using-the-command-line https://stackoverflow.com/questions/31639059/how-to-add-license-to-an-existing-github-project http://localhost:8080/ https://github.com/spring-projects/spring-petclinic https://stackoverflow.com/questions/46265775/spring-boot-project-shows-the-login-page https://www.google.com/search?q=login+screen+spring+boot&oq=login+screen+spring+boot&aqs=chrome..69i57.4031j0j1&client=ubuntu&sourceid=chrome&ie=UTF-8 https://www.baeldung.com/spring-security-login https://spring.io/guides/gs/securing-web/ https://stackoverflow.com/questions/51221777/failed-to-configure-a-datasource-url-attribute-is-not-specified-and-no-embedd http://localhost:8080/ https://spring.io/guides/tutorials/react-and-spring-data-rest/']
full_command = ['chromium', '--window-position=3900,0', '--profile-directory=Default', '--new-window', 'https://github.com/franciscoguemes/online-tools', 'https://franciscoguemes.com/']

if isinstance(full_command,list):
    print("is list")

aplication = subprocess.Popen(full_command, stdout=subprocess.PIPE)