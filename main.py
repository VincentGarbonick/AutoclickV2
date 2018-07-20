import pyautogui

import random 

#variables concerning the swipe loop, passes is number of passes 
passes = 10
count = 0
likeNum = 0
hateNum = 0

#variables concerning screen size, can be adjusted for different screens (like and dislike come from center of button)
tindrLikeX = 1350
tindrLikeY = 754

tindrMedX = 1350
tinerMedY = 734

tindrDislikeX = 1300
tindrDislikeY = 754

#variables concerning duration of clicks and swipes
clickClock = 0.5
durClock = 0.8

#add random swipe time 

while count <= passes:

	swipeThresh = random.randint(1,100)

	if swipeThresh <= 60:
		pyautogui.moveTo(tindrLikeX,tindrLikeY, duration = durClock)
		pyautogui.click()

		likeNum += likeNum
		print(likeNum)

		pyautogui.moveTo(tindrMedX, tinerMedY, duration = durClock)
		pyautogui.click()

	else:
		pyautogui.moveTo(tindrDislikeX, tindrDislikeY, duration = durClock)
		pyautogui.click()

		hateNum += hateNum
		print(hateNum)

	count += count

print("Job's done")