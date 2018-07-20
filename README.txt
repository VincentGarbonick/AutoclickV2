This is a program that is intended to automate the tindr-like process in order
to make it easier for the user to constantly be looking for matches. 

In order to use this program, perform the following steps.

1.) Download and install python. Install the pyautogui module using pip.

2.) Download and install TeamViewer on your mobile device and computer.

3.) Run teamviewer and maximize the phone in your main screen. 

4.) Navigate to ~/PATH/TO/AutoClickV2/config/config.py and open the configuration file. In a seperate terminal, run "py" and import the pyautogui feature.
Use the pyautogui.position() feature to find the spot where the like, dislike,
and area where the "keep swiping" spot appears after matches are. Find the 
centermost position of them and enter it into the config information for 
the program.

Do this for any extra information as it is added into the program.

5.) Navigate to the ~/PATH/TO/AutoClickV2/main and add the ~PATH/TO/AutoclickV2/
config under the "import sys" at the top of the main file so the program
knows where to find the config information.

6.) Run the program as needed and tweak config information as needed. 
