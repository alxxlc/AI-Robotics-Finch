#!/usr/bin/python3

# AI Robotics Spr18 Semester Project
# Alex Cote - alc552
# Marc Moore - mnm419

import time
from finch import Finch

finch = Finch()

# State values
fStates = ["LightSeek", "ObstAvoid", "Rest", "WarmSeek"]
curState = 0

#### CONSTANTS ####
# Sensor values
wantedLight = .27

# Move speeds
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

	left_light = 0
	right_light = 0
	left_obstacle = False
	right_obstacle = False

	while (finchRunning):
		if (fStates[curState] == "LightSeek"):
			## Debug code
			# print(finch.temperature())

			########## Setup #############################
			finch.led(0, 0, 0)

			########### Perform Actions ###################
			light_difference = right_light - left_light
			left_coefficient = .7 + (light_difference * 6)
			right_coefficient = .7 - (light_difference * 6)

			finch.wheels(left_coefficient, right_coefficient)

			########### Sense #############################
			left_obstacle, right_obstacle = finch.obstacle()
			left_light, right_light = finch.light()

			########### State Changes #####################
			if (right_obstacle or left_obstacle):
				curState = 1
				print(fStates[curState])
			elif (left_light >= wantedLight or right_light >= wantedLight):
				curState = 2
				print(fStates[curState])

		elif (fStates[curState] == "ObstAvoid"):
			########### Perform Actions ###################
			# Turn to the right until obstacle is gone
			if(right_obstacle and (not left_obstacle)):
				print("right obstacle")
				finch.wheels(-.3, -.3)
				time.sleep(1.7)
				finch.wheels(-.3, .3)
				time.sleep(1.7)
				#finch.wheels(.5, .5)
				#time.sleep(1.5)
			elif(left_obstacle and (not right_obstacle)):
				print("left obstacle")
				finch.wheels(-.3, -.3)
				time.sleep(1.7)
				finch.wheels(.3, -.3)
				time.sleep(1.7)
				#finch.wheels(.5, .5)
				#time.sleep(1.5)
			elif(left_obstacle and right_obstacle):
				finch.wheels(-.3, -.3)
				time.sleep(2.0)
			
			########### Sense #############################
			left_light, right_light = finch.light()
			left_obstacle, right_obstacle = finch.obstacle()

			########### State Changes #####################
			if ((not right_obstacle) and (not left_obstacle)):
				if ((right_light < wantedLight) and (left_light < wantedLight)):
					curState = 0
					print(fStates[curState])
				else:
					curState = 2
					print(fStates[curState])
			
		elif (fStates[curState] == "Rest"):
			########### Perform Actions ###################
			finch.wheels(0.0, 0.0)
			finch.led(0, 255, 0)

			########### Sense #############################
			left_light, right_light = finch.light()

			########### State Changes #####################
			if ((right_light < wantedLight) and (left_light < wantedLight)):
				curState = 0
				print(fStates[curState])

			if (curState != 2):
				left_obstacle, right_obstacle = finch.obstacle()
				if (right_obstacle or left_obstacle):
					curState = 1
					print(fStates[curState])
		else:
			# uh oh
			# go back
			curState = 0
			print(fStates[curState])


FinchRun()
finch.close()



##################################################################################################
# #!/usr/bin/python3

# # AI Robotics S18 Semester Project
# # Alex Coté - alc552
# # Marc Moore - mnm419

# from finch import Finch

# finch = Finch()

# fStates = ["LightSeek", "ObstAvoid", "Rest", "WarmSeek"]
# curState = 0

# wantedLight = .7 # Temp Value: 0-1.0
# wantedTemp = 30 # Degrees in C
# wanderSpeedMax = .5
# wanderSpeedMin = .2
# rushSpeedMax = 1
# rushSpeedMin = .5
# curSpeedL = 0
# curSpeedR = 0

# def FinchRun():
# 	global fStates
# 	global curState
# 	finchRunning = True

# 	while (finchRunning):
# 		if (fStates[curState] == "LightSeek"):
# 			# Move at rushing speed


# 			# Check for obstacle
# 			if (finch.obstacle):
# 				curState = 1
# 			elif (finch.light == wantedLight):
# 				if (finch.temperature == wantedTemp):
# 					curState = 2
# 				else:
# 					curState = 3
# 		elif (fStates[curState] == "ObstAvoid"):
# 			# Turn to the right until obstacle is gone

# 			if (finch.obstacle == False):
# 				if (finch.light < wantedLight):
# 					curState = 0
# 				elif (finch.temperature < wantedTemp):
# 					curState = 3
# 				else: curState = 2
# 		elif (fStates[curState] == "Rest"):
# 			if (finch.light < wantedLight):
# 				curState = 0
# 			elif (finch.temperature < wantedTemp):
# 				curState = 3
			
# 			if (curState != 2):
# 				if (finch.obstacle == True):
# 					curState = 1
# 		# elif (fStates[curState] == "WarmSeek"):
# 		# 	# Wander until warmth has been found
			
# 		# 	if (finch.obstacle == True):
# 		# 		curState = 1
# 		# 	elif (finch.light < wantedLight):
# 		# 		curState = 0
# 		# 	elif (finch.temperature >= wantedTemp):
# 		# 		curState = 2
# 		else:
# 			curState = 0

# FinchRun()