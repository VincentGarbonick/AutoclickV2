#add functions for main.py 
import random
import decimal 

from varconfig import *

#function to generate random position for like 
def GenRandLikeX():
	dummy = 0
	dummy = random.randint( (tindrLikeX - tindrLikeDif), (tindrLikeX) )
	return dummy 

def GenRandLikeY():
	dummy = 0
	dummy = random.randint( (tindrLikeY - tindrLikeDif), (tindrLikeY))
	return dummy 

def GenRandMedX():
	dummy = 0
	dummy = random.randint( (tindrMedX - tindrMedDif), (tindrMedX))
	return dummy 

def GenRandMedY():
	dummy = 0
	dummy = random.randint( (tindrMedY - 3), (tindrMedY))
	return dummy 

def GenRandDisX():
	dummy = 0
	dummy = random.randint( (tindrDislikeX - tindrDislikeDif), (tindrDislikeX))
	return dummy 

def GenRandDisY():
	dummy = 0
	dummy = random.randint( (tindrDislikeY - tindrDislikeDif), (tindrDislikeY))
	return dummy 

def DurClockGen():
	dummy = 0 
	dummy = random.randint(4,14)
	dummy = dummy / 10
	return dummy

def TindrInit():
	#turns location on for you 
	pyautogui.moveTo(851,171, duration = dur)
	pyautogui.dragTo(882,610, 0.5, button = 'left')

	time.sleep(dur)

	#enables location
	pyautogui.moveTo(828,228, duration = dur)
	pyautogui.click()

	#exits the location drag down menu and agree to loc.const
	pyautogui.moveTo(986,730,duration = dur)
	pyautogui.click()

	time.sleep(1)

	#resets location to prevent some glitchiness
	pyautogui.moveTo(863, 443, duration = dur)

	#opens folder
	pyautogui.moveTo(1042,753, duration = dur)
	pyautogui.click()


	time.sleep(1)

	#opens Tindr
	pyautogui.moveTo(884,607, duration =dur)
	pyautogui.click()

	time.sleep(20)