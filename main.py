#!/usr/bin/python3

# AI Robotics S18 Semester Project
# Alex Cote - alc552
# Marc Moore - mnm419
import time
from finch import Finch

finch = Finch()

fStates = ["LightSeek", "ObstAvoid", "Rest", "WarmSeek"]
curState = 0

wantedLight = 1.0 # Temp Value: 0-1.0
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
		print(fStates[curState])
		if (fStates[curState] == "LightSeek"):
			while(fStates[curState] == "LightSeek"):
				left_obstacle, right_obstacle = finch.obstacle()
				if left_obstacle:
					print("left obstacle")
				if right_obstacle:
					print("right obstacle")
				finch.led(0, 0, 0)
				# Move at rushing speed
				prev_left_light, prev_right_light = finch.light()
				prev_light_cumulative = prev_left_light + prev_right_light
				#print(prev_light_cumulative, "  previous light")
				finch.wheels(0.5, 0.5)
				time.sleep(.5)
				finch.wheels(0, 0)
				cur_left_light, cur_right_light = finch.light()
				cur_light_cumulative = cur_left_light + cur_right_light
				#print(cur_light_cumulative, "  current light")
				if(cur_light_cumulative > prev_light_cumulative):
					finch.wheels(0.5, 0.5)
					print("light level has increased")
					time.sleep(0.5)
					finch.wheels(0,0)
					if(cur_right_light > prev_right_light):
						print("light source detected to the right")
						finch.wheels(.5, -.5)
						time.sleep(2)
						finch.wheels(0.5, 0.5)
						time.sleep(2)
						finch.wheels(0,0)
					elif(cur_left_light > prev_left_light):
						print("light source detected to the left")
						finch.wheels(-.5, .5)
						time.sleep(2)
						finch.wheels(0.5, 0.5)
						time.sleep(1)
						finch.wheels(0, 0)
				else:
					finch.wheels(.5, .5)
					time.sleep(.5)
					finch.wheels(0, 0)

				# Check for obstacle
				cur_left_light, cur_right_light = finch.light()
				if (right_obstacle or left_obstacle):
					curState = 1
				elif (cur_left_light >= wantedLight or cur_right_light >= wantedLight):
					#if (finch.temperature() >= wantedTemp):
					curState = 2
					#else:
						#curState = 3
		elif (fStates[curState] == "ObstAvoid"):
			while(fStates[curState] == "ObstAvoid"):
				# Turn to the right until obstacle is gone
				left_obstacle, right_obstacle = finch.obstacle()
				if(right_obstacle and not left_obstacle):
					finch.wheels(-.5, -.5)
					time.sleep(5.0)
					finch.wheels(-.5, .5)
					time.sleep(5.0)
				elif(left_obstacle and not right_obstacle):
					finch.wheels(-5, -.5)
					time.sleep(5.0)
					finch.wheels(.5, -.5)
					time.sleep(5.0)
				elif(left_obstacle and right_obstacle):
					finch.wheels(-.5, -.5)
					time.sleep(5.0)

				cur_left_light, cur_right_light = finch.light()
				#left_obstacle, right_obstacle = finch.obstacle()
				if left_obstacle:
					print("left obstacle")
				if right_obstacle:
					print("right obstacle")
				if ((not right_obstacle) and (not left_obstacle)):
					print("no obstacle")
					if (cur_right_light < wantedLight and cur_left_light < wantedLight):
						curState = 0
					#elif (finch.temperature() < wantedTemp):
						#curState = 3
					else:
						curState = 2
		elif (fStates[curState] == "Rest"):
			while(fStates[curState] == "Rest"):
				finch.wheels(0.0, 0.0)
				finch.led(0, 255, 0)

				if (finch.light < wantedLight):
					curState = 0
				#elif (finch.temperature < wantedTemp):
					#curState = 3

				if (curState != 2):
					left_obstacle, right_obstacle = finch.obstacle()
					if ( right_obstacle or left_obstacle):
						curState = 1
					'''
		elif (fStates[curState] == "WarmSeek"):
			# Wander until warmth has been found
			
			cur_left_light, cur_right_light = finch.light()
			left_obstacle, right_obstacle = finch.obstacle()
			if (left_obstacle or right_obstacle):
				curState = 1
			elif (cur_right_light < wantedLight and cur_left_light < wantedLight):
				curState = 0
			elif (finch.temperature() >= wantedTemp):
				curState = 2 '''
		else:
			curState = 0


FinchRun()