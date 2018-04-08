#!/usr/bin/python3

# AI Robotics S18 Semester Project
# Alex Coté - alc552
# Marc Moore - mnm419

fStates = ["LightSeek", "ObstAvoid", "Rest", "WarmSeek"]
curState = 0

def FinchRun():
	global fStates
	global curState
	finchRunning = True

	while (finchRunning):
		if (fStates[curState] == "LightSeek"):
			pass
		elif (fStates[curState] == "ObstAvoid"):
			pass
		elif (fStates[curState] == "Rest"):
			pass
		elif (fStaets[curState] == "WarmSeek"):
			pass
		else:
			curState = 0

FinchRun()