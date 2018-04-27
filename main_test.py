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

	buzzTime = .5
	buzzTone = 500

	left_obstacle, right_obstacle = finch.obstacle()
	left_light, right_light = finch.light()

	while (finchRunning):
		if (fStates[curState] == "LightSeek"):
			## Debug code
			# print(finch.temperature())

			########## Setup #############################
			light_mod = (left_light + right_light) / 2
			if (light_mod > wantedLight): light_mod = wantedLight
			light_mod = (light_mod / wantedLight)

			green_light = 0
			red_light = 0

			# set green value
			if (light_mod > .3):
				green_light = 255 * ((light_mod - .3) / .7)
			
			# set red value
			if (light_mod < .6):
				red_light = 255 - (255 * (light_mod / .6))
			
			finch.led(red_light, green_light, 0)

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
				finch.buzzer(buzzTime, buzzTone)
				print(fStates[curState])

		elif (fStates[curState] == "ObstAvoid"):
			### Debugging
			#left_obstacle, right_obstacle = finch.obstacle()
			#print("left:", left_obstacle, "\nright:", right_obstacle)
			#print("2 left:", left_obstacle, "\n 2 right:", right_obstacle)
			
			########### Perform Actions ###################
			# Turn to the right until obstacle is gone
			if (right_obstacle and (not left_obstacle)):
				print("right obstacle")
				finch.wheels(-.3, -.3)
				time.sleep(1.7)
				finch.wheels(-.3, .3)
				time.sleep(1)
				finch.wheels(.5, .5)
				time.sleep(1)
			elif(left_obstacle and (not right_obstacle)):
				print("left obstacle")
				finch.wheels(-.3, -.3)
				time.sleep(1.7)
				finch.wheels(.3, -.3)
				time.sleep(1)
				finch.wheels(.5, .5)
				time.sleep(1)
			elif(left_obstacle and right_obstacle):
				finch.wheels(-.3, -.3)
				time.sleep(2.0)
			
			########### Sense #############################
			left_light, right_light = finch.light()
			left_obstacle, right_obstacle = finch.obstacle()

			########### State Changes #####################
			if (not right_obstacle and (not left_obstacle)):
				if ((right_light < wantedLight) and (left_light < wantedLight)):
					curState = 0
					print(fStates[curState])
				else:
					curState = 2
					finch.buzzer(buzzTime, buzzTone)
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