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

				finch.led(0, 0, 0)
				# Move at rushing speed
				prev_left_light, prev_right_light = finch.light()
				prev_light_cumulative = prev_left_light + prev_right_light
				light_difference = prev_right_light - prev_left_light
				light_difference *= 4
				left_coefficient = light_difference + .5
				right_coefficient = .5 - light_difference
				finch.wheels(left_coefficient, right_coefficient)
				#print(prev_left_light, " left light", prev_right_light, " right light")

				'''
				cur_left_light, cur_right_light = finch.light()
				cur_light_cumulative = cur_left_light + cur_right_light
				print(cur_left_light, " ", cur_right_light,  " current light left, right")
				if(cur_light_cumulative > prev_light_cumulative):
					#finch.wheels(0.3, 0.3)
					print("light level has increased")
					#time.sleep(0.5)
					#finch.wheels(0,0)
					if(cur_right_light > prev_right_ light):
						print("light source detected to the right")
						finch.wheels(.4, -.4)
						time.sleep(1.5)
						finch.wheels(0.4, 0.4)
						time.sleep(1.0)
						finch.wheels(0,0)
						time.sleep(2)
					if(cur_left_light > prev_left_light):
						print("light source detected to the left")
						finch.wheels(-.4, .4)
						time.sleep(1.5)
						finch.wheels(0.4, 0.4)
						time.sleep(1.0)
						finch.wheels(0, 0)
						time.sleep(2)
				else:
					print("moving forward looking for light")
					finch.wheels(.3, .3)
					time.sleep(.5)
					finch.wheels(0, 0)
					time.sleep(2)
				'''

				# Check for obstacle
				left_obstacle, right_obstacle = finch.obstacle()
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
					print("right obstacle")
					finch.wheels(-.2, -.2)
					time.sleep(2.0)
					finch.wheels(-.2, .2)
					time.sleep(2.0)
				elif(left_obstacle and not right_obstacle):
					print("left obstacle")
					finch.wheels(-2, -.2)
					time.sleep(2.0)
					finch.wheels(.2, -.2)
					time.sleep(2.0)
				elif(left_obstacle and right_obstacle):
					finch.wheels(-.3, -.3)
					time.sleep(2.0)


				cur_left_light, cur_right_light = finch.light()
				left_obstacle, right_obstacle = finch.obstacle()
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