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
	dummy = random.randint( (tindrMedY - tindrMedDif), (tindrMedY))
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
