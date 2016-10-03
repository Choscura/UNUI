"""
	IUNU Test project.

"""
from math import sqrt

class plant:
    """
    a data member to represent the plant
    """

class actor:
    """
    Things that have behavior.
    """

class camera:
    """     
    The camera class represents the physical cameras in the abstracted greenhouse, 
    for the purposes of calculating and controlling their behavior
    """
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
        """
        Very simply, think of a cube- we're measuring a straight line from 
        top back left to bottom right front, or whatever. So we calculate 
        the hypotenuse for the bottom, then we use that hypotenuse squared
        to calculate the hypotenuse of the triangle remaining.
        """
        #Horizontal first:
        HorizontalX = (self.camerax-plantx)
        HorizontalY = (self.cameray-planty)
        HorizontalHypotenuse=float(sqrt((HorizontalX**2)+(HorizontalY**2)))
        #Now for the vertical part:
        VerticalLeg=(self.cameraz-plantz)
        VerticalHypotenuse=float(sqrt((VerticalLeg**2)+(HorizontalHypotenuse**2)))
	#If it all worked, this should be the distance. 
        return VerticalHypotenuse
    
    def TakePicture(self):
        """
        a black box to take pictures
        """
        print("Click!")

def main():
    """
    Main function, for testing
    """
    Derp = camera(1,2,3)
    print(Derp.DistanceToPlant(4,5,6))
    Derp.TakePicture()

main()

"""
There is already a separate test document. The following code is being 
generated to populate that, which will deal with package tests.
"""

import unittest

