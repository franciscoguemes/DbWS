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
option2="Work in AEGIS project"
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
UNISCON_GITLAB=https://gitlab.uniscon-rnd.de/users/sign_in
LEO=https://dict.leo.org/spanisch-deutsch
WORDREFERENCE=http://www.wordreference.com/es/en/translation.asp


function work_in_uniscon_as_product_owner {
	echo "Starting Uniscon environment..."

	#Start Chrome...
	chromium --window-position=$THIRD_MONITOR_LEFT_UPPER_CORNER_XPS --profile-directory="$CHROMIUM_PROFILE_UNISCON" --new-window \
		$EVERNOTE \
		$UNISCON_OUTLOOK \
		$IDGARD \
		$AHA \
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
	#slack

	#Start Zoho Cliq
	cliq
}



#
# This funciton comes from the old days when I was a developer and the entire environment was initialized magically...
#
function work_in_uniscon_as_developer {
	echo "Starting Uniscon environment..."

	#Start eclipse...
	$ECLIPSE_PATH/eclipse -data $ECLIPSE_UNISCON_WORKSPACE &

	#Start docker container idgard_6275...
	#gnome-terminal -- sudo docker start -ai idgard_6275
	
	CONTAINER_NAME=BAC-15
	#Open terminals in differnt possitions in XPS13
	gnome-terminal --geometry $LEFT_UPPER_CORNER_XPS13 --working-directory=~ -- /bin/bash -c "set-title Docker Images; sudo docker images; /bin/bash" & 	
	#gnome-terminal --geometry $RIGHT_UPPER_CORNER_XPS13 --working-directory=~ -- /bin/bash -c "set-title $CONTAINER_NAME; sudo docker start -ai $CONTAINER_NAME; /bin/bash " &
	#gnome-terminal --geometry $RIGHT_UPPER_CORNER_XPS13 --working-directory=~ -- /bin/bash &
	gnome-terminal --geometry $RIGHT_UPPER_CORNER_XPS13 --working-directory=~ -- /bin/bash -c "set-title Containers; exec /bin/bash"
	gnome-terminal --geometry $LEFT_DOWN_CORNER_XPS13 --working-directory=~ -- /bin/bash -c "set-title Docker Containers; sudo docker ps -a; /bin/bash " & 
	gnome-terminal --geometry $RIGHT_DOWN_CORNER_XPS13 --working-directory=~ -- /bin/bash &

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
	#slack

	#Start Zoho Cliq
	cliq
}

function startOption1 {
	# I used to be a developer...
	#work_in_uniscon_as_developer

	work_in_uniscon_as_product_owner
}

function open_bookmarks {
	# echo "$1"
	# echo  `pwd`
	url_list=$($CHROME_BOOKMARKS_APP_DIR/chrome_bookmarks.py --config=$CHROME_BOOKMARKS_APP_CONFIG_FILE "$1")
	# Remove characters not needed from Python list
	url_list=$(echo "$url_list" | tr -d [],\')
	# echo $url_list

	for i in "${url_list[@]}"
	do
    	#echo "$i"
		chromium --window-position=$THIRD_MONITOR_LEFT_UPPER_CORNER_XPS --profile-directory=$CHROMIUM_PROFILE_FRANCISCO --new-window \
		$i  \ &	
	done
}

function startOption2 {
	echo "Starting AEGIS environment..."

	#Start eclipse...
	$ECLIPSE_PATH/eclipse -data $ECLIPSE_PERSONAL_WORKSPACE &

	#Start Chrome... 
	# chromium --window-position=$THIRD_MONITOR_LEFT_UPPER_CORNER_XPS --profile-directory=$CHROMIUM_PROFILE_FRANCISCO --new-window \
	# 	$GMAIL \
	# 	$EVERNOTE \
	# 	$LEO \
	# 	$WORDREFERENCE &


	# Bookmarks/Personal/Login Screen
	# /home/francisco/git/Francisco/github/chrome_bookmarks/chrome_bookmarks.py --config=/home/francisco/conf/chrome_bookmarks/chrome_bookmarks.conf /Personal/"Login screen"
	open_bookmarks /Personal/"Login screen"

	#Wait 5 seconds...
	sleep 5
}

function startOption3 {
	echo "Initializing Other..."
	# echo  `pwd`
	# git/Francisco/github/chrome_bookmarks/chrome_bookmarks.py --config=/home/francisco/conf/chrome_bookmarks/chrome_bookmarks.conf /Personal/"Start new Spring Boot project"

	#open_bookmarks /Personal/"Login screen"

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




