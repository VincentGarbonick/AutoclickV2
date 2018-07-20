import pyautogui

import random 

import sys 
sys.path.insert(0, 'C:/Users/vincent.garbonick/Desktop/AutoclickV2/config')
import config
from varconfig import * 
from function import *

while count <= passes:

	#variable that decides if loop is going to like or dislike someone 
	swipeThresh = random.randint(1,100)

	if swipeThresh <= 60:
		pyautogui.moveTo(tindrLikeX,tindrLikeY, duration = durClock)
		pyautogui.click()

		likeNum += likeNum
		print(likeNum)

		pyautogui.moveTo(tindrMedX, tindrMedY, duration = durClock)
		pyautogui.click()

	else:
		pyautogui.moveTo(tindrDislikeX, tindrDislikeY, duration = durClock)
		pyautogui.click()

		hateNum += hateNum
		print(hateNum)

	count += count

print("Job's done")
