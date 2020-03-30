#!/bin/bash

#############################################################################################
#
# Description:
# 	The script shows a dialog that enquires the user on the purpose of the started session. 
# 	Whether the user wants to:
#		1-) Setup the working environment for Uniscon
#		2-) Setup the working environment for personal projects
#		3-) Other (No setup of any working environment)
#
# Referenced by:
#	referencing file: ~/.config/autostar/environmentChoice.desktop
#
# See:
# 	Zenit manual (version 3.24): https://help.gnome.org/users/zenity/3.24/
# 	Zenit window with 3 buttons: https://stackoverflow.com/questions/37997249/zenity-dialog-window-with-two-buttons-but-no-text-entry
#	Switch in bash: http://tldp.org/LDP/Bash-Beginners-Guide/html/sect_07_03.html
#	Variables in a case of a switch: https://unix.stackexchange.com/questions/234264/how-can-i-use-a-variable-as-a-case-condition
#	Funcitons in bash: http://tldp.org/HOWTO/Bash-Prog-Intro-HOWTO-8.html
#	Start Chrome with a different user: https://superuser.com/questions/377186/how-do-i-start-chrome-using-a-specified-user-profile
# 	Chromium directory in ubunt: https://askubuntu.com/questions/1075103/chromium-config-folder-is-missing-in-ubuntu-18-04
#	
#	
#
#############################################################################################


option1="Work at Uniscon"
option2="Work in personal projects"
option3="Other projects"

ans=$(zenity --info --title 'Welcome Francisco!' \
      --text "¿What do you want to do today?" \
      --ok-label "$option1" \
      --extra-button "$option2" \
      --extra-button "$option3" \
 	)
  rc=$?

#answer="${rc}-${ans}"
#echo $answer
echo "${rc}-${ans}"


ECLIPSE_PATH=/home/francisco/eclipse/java-photon/eclipse
UNISCON_ECLIPSE_WORKSPACE=/home/francisco/workspaces/uniscon
PERSONAL_ECLIPSE_WORKSPACE=/home/francisco/workspaces/personal-projects
BAELDUNG_ECLIPSE_WORKSPACE=/home/francisco/workspaces/baeldung

LEFT_UPPER_CORNER_XPS13=110x24+86+110
RIGHT_UPPER_CORNER_XPS13=80x24+1180+110
LEFT_DOWN_CORNER_XPS13=80x24+86+610
RIGHT_DOWN_CORNER_XPS13=80x24+1180+610

THIRD_MONITOR_LEFT_UPPER_CORNER_XPS=3900,0

CHROMIUM_PROFILE_FRANCISCO=Default
CHROMIUM_PROFILE_UNISCON=Profile\ 1

GMAIL=https://mail.google.com/mail/u/0/#inbox
EVERNOTE=https://www.evernote.com/Login.action
UNISCON_OUTLOOK=https://outlook.office.com/owa/?realm=uniscon.net
IDGARD=https://my.idgard.de/#/login
UNISCON_CONFLUENCE=https://confluence.uniscon-rnd.de/display/BAC/Backoffice
UNISCON_JIRA=https://jira.uniscon-rnd.de/browse/PM-33
UNISCON_GITLAB=https://gitlab.uniscon-rnd.de/users/sign_in
LEO=https://dict.leo.org/spanisch-deutsch
WORDREFERENCE=http://www.wordreference.com/es/en/translation.asp

function startOption1 {
	echo "Starting Uniscon environment..."

	#Start eclipse...
	$ECLIPSE_PATH/eclipse -data $UNISCON_ECLIPSE_WORKSPACE &

	#Start docker container idgard_6275...
	#gnome-terminal -- sudo docker start -ai idgard_6275
	
	CONTAINER_NAME=BAC-15
	#Open terminals in differnt possitions in XPS13
	gnome-terminal --geometry $LEFT_UPPER_CORNER_XPS13 --working-directory=~ -- /bin/bash -c "set-title Docker Images; sudo docker images; /bin/bash" & 	
	#gnome-terminal --geometry $RIGHT_UPPER_CORNER_XPS13 --working-directory=~ -- /bin/bash -c "set-title $CONTAINER_NAME; sudo docker start -ai $CONTAINER_NAME; /bin/bash " &
	gnome-terminal --geometry $RIGHT_UPPER_CORNER_XPS13 --working-directory=~ -- /bin/bash -c "set-title Docker Container" &
	gnome-terminal --geometry $LEFT_DOWN_CORNER_XPS13 --working-directory=~ -- /bin/bash -c "set-title Docker Containers; sudo docker ps -a; /bin/bash " & 
	gnome-terminal --geometry $RIGHT_DOWN_CORNER_XPS13 &

	#Start Chrome...
	chromium --window-position=$THIRD_MONITOR_LEFT_UPPER_CORNER_XPS --profile-directory="$CHROMIUM_PROFILE_UNISCON" --new-window \
		$EVERNOTE \
		$UNISCON_OUTLOOK \
		$IDGARD \
		$UNISCON_CONFLUENCE \
		$UNISCON_JIRA \
		$UNISCON_GITLAB \
		$LEO \
		$WORDREFERENCE &

	#Wait 5 seconds...
	sleep 5

	chromium --window-position=$THIRD_MONITOR_LEFT_UPPER_CORNER_XPS --profile-directory=$CHROMIUM_PROFILE_FRANCISCO --new-window \
		$GMAIL \ &	

	#Wait 5 seconds...
	sleep 5

	#Start slack...
	slack

}

function startOption2 {
	echo "Starting Personal environment..."

	#Start eclipse...
	$ECLIPSE_PATH/eclipse -data $PERSONAL_ECLIPSE_WORKSPACE &

	#Start Chrome...
	chromium --window-position=$THIRD_MONITOR_LEFT_UPPER_CORNER_XPS --profile-directory=$CHROMIUM_PROFILE_FRANCISCO --new-window \
		$GMAIL \
		$EVERNOTE \
		$LEO \
		$WORDREFERENCE &

	#Doing whatever...
}

function startOption3 {
	echo "Initializing Other..."
}

case "$rc" in
	0)
		startOption1
		;;
	1)
		case "$ans" in
			"")
				echo "You chose to leave..."
				exit 0
				;;
			($option2)
				startOption2
				;;
			($option3)
				startOption3
				;;
			*)
				echo "The script should never reach this point. This should be an option between \"$option2\" and \"$option3\""
				exit 1
		esac
		;;
	*)
		echo "The script should never reach this point!!!"
		exit 1
esac




