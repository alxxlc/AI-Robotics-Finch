#!/usr/bin/python3

# AI Robotics S18 Semester Project
# Alex Coté - alc552
# Marc Moore - mnm419

from finch import Finch

finch = Finch()

fStates = ["LightSeek", "ObstAvoid", "Rest", "WarmSeek"]
curState = 0

wantedLight = .7 # Temp Value: 0-1.0
wantedTemp = 30 # Degrees in C
wanderSpeedMax = .5
wanderSpeedMin = .2
rushSpeedMax = 1
rushSpeedMin = .5
curSpeedL = 0
curSpeedR = 0

def FinchRun():
	global fStates
	global curState
	finchRunning = True

	while (finchRunning):
		if (fStates[curState] == "LightSeek"):
			# Move at rushing speed
			

			# Check for obstacle
			if (finch.obstacle):
				curState = 1
			elif (finch.light == wantedLight):
				if (finch.temperature == wantedTemp):
					curState = 2
				else:
					curState = 3
		elif (fStates[curState] == "ObstAvoid"):
			# Turn to the right until obstacle is gone

			if (finch.obstacle == False):
				if (finch.light < wantedLight):
					curState = 0
				elif (finch.temperature < wantedTemp):
					curState = 3
				else: curState = 2
		elif (fStates[curState] == "Rest"):
			if (finch.light < wantedLight):
				curState = 0
			elif (finch.temperature < wantedTemp):
				curState = 3
			
			if (curState != 2):
				if (finch.obstacle == True):
					curState = 1
		elif (fStaets[curState] == "WarmSeek"):
			# Wander until warmth has been found
			
			if (finch.obstacle == True):
				curState = 1
			elif (finch.light < wantedLight):
				curState = 0
			elif (finch.temperature >= wantedTemp):
				curState = 2
		else:
			curState = 0

FinchRun()