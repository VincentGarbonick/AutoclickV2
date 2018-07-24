import pyautogui

import random 

import decimal

import sys 
sys.path.insert(0, 'C:/Users/vincent/AutoclickV2/AutoclickV2/config')
import config
from varconfig import * 
from function import *

#turns on location and opens Tindr
TindrInit()

while count <= passes:

	#variable that decides if loop is going to like or dislike someone 
	swipeThresh = random.randint(1,100)

	if swipeThresh <= 48:
		pyautogui.moveTo(GenRandLikeX(),GenRandLikeY(), duration = durClock)
		pyautogui.click()
		durClock = DurClockGen()

		likeNum = likeNum + 1 
		print("Likes: {}".format(likeNum))

		pyautogui.moveTo(GenRandMedX(), GenRandMedY(), duration = durClock)
		pyautogui.click()
		durClock = DurClockGen()


	else:
		pyautogui.moveTo(GenRandDisX(), GenRandDisY(), duration = durClock)
		pyautogui.click()
		durClock = DurClockGen()


		hateNum = hateNum + 1  
		print("Dislikes: {}".format(hateNum))

	count = count + 1  

print("Job's done ;)")
print("Total Likes: {}".format(likeNum))
print("Total Dislikes: {}".format(hateNum))