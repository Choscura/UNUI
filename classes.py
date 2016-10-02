"""
	IUNU Test project.

	Kendall,

Lets try a little coding test under real world conditions. For the record, your code is yours until we hire you or buy/license it etc.

Ive got a camera mounted on a pair of servos. For purposes of this exercise, those servos each have a pair of external functions, one for setting its rotation, one for reading its rotation. Given the position of the camera as locally defined constant as one element in an array of the positions of all the cameras in the room, and a (X,Y,Z) target coordinate, determine if this camera is the closest on any side of the target, and if so, aim at the target and at a synchronized time, take a picture.

I'm looking for a proper python project setup, including tests, with gitbhub repo and commits that make sense. Asking questions is encouraged. Finding hidden requirements is half the battle of building software. Getting software working, then refactoring is the other. Show me how you think through a problem.

"""
import unittest
from math import sqrt

class camera:
	#Position of camera origin point in space
	camerax=(float)
	cameray=(float)
	cameraz=(float)


	#init function to handle class construction
	def __init__(self, x, y, z):
		self.camerax = x
		self.cameray = y
		self.cameraz = z


	#a function to find the distance between the camera and plant in 3D space
	def DistanceToPlant(self, plantx, planty, plantz):
		#Very simply, think of a cube- we're measuring a straight line from top back left to bottom right front, or whatever. So we calculate the hypotenuse for the bottom, then we use that hypotenuse squared to calculate the hypotenuse of the triangle remaining.
		
		#Horizontal first:
		HorizontalX 			= 	(self.camerax-plantx)
		HorizontalY 			= 	(self.cameray-planty)
		HorizontalHypotenuse	=	float(sqrt((HorizontalX**2)+(HorizontalY**2)))
		
		#Now for the vertical part:
		VerticalLeg 			=	(self.cameraz-plantz)
		VerticalHypotenuse		=	float(sqrt((VerticalLeg**2)+(HorizontalHypotenuse**2)))
		#If it all worked, this should be the distance. 
		return VerticalHypotenuse


	#To black box the actual handling of picture tacking for the moment
	def TakePicture(self):
		print("Click!")

#the main function to actually control program flow and test things as I write
def main():
	Derp = camera(1,2,3)
	print(Derp.DistanceToPlant(4,5,6))
	Derp.TakePicture()

main()