"""
    UNUI
    IUNU environment abstraction toolkit.  See README.md for documentation.
"""
from math import sqrt

class actor:
    """
    An actor in UNUI space is a noun that has <or can possibly have> 
    behavior. A light is an actor, a camera is an actor, a plant is an actor.
    """
    #Spatial positioning
    actorx = (float)
    actory = (float)
    actorz = (float)
    
    #spacial orientation
    transformx = (float)
    transformy = (float)
    tronsformz = (float)
    
    #constructor method
    def __init__(self, x, y, z):
        """
        initialization for 'actor' class
        """
        self.actorx = x
        self.actory = y
        self.actorz = z

    def getposition(self):
        """
        gets the world's assessment of where the origin point of this actor is.
        returns the xyz coordinates as an array of floats""" 
        return [self.x, self.y, self.z]

    def setposition(self, x, y, z):
        """
        Sets the position of the actor to equal the function parameters
        """
        self.actorx = x
        self.actory = y
        self.actorz = z
    
    def getdistance(self, measured_x, measured_y, measured_z):
        """
        Very simply, think of a cube- we're measuring a straight line from 
        top back left to bottom right front, or whatever. So we calculate 
        the hypotenuse for the bottom, then we use that hypotenuse squared
        to calculate the hypotenuse of the triangle remaining.
        """
        #Horizontal first:
        HorizontalX = (self.camerax-actorx)
        HorizontalY = (self.cameray-actory)
        HorizontalHypotenuse=float(sqrt((HorizontalX**2)+(HorizontalY**2)))
        #Now for the vertical part:
        VerticalLeg=(self.cameraz-actorz)
        VerticalHypotenuse=float(sqrt((VerticalLeg**2)+(HorizontalHypotenuse**2)))
	#If it all worked, this should be the distance. 
        return VerticalHypotenuse

class plant(actor):
    """
    a data member to represent the plant
    """
    
class camera(actor):
    """     
    The camera class represents the physical cameras in the abstracted greenhouse, 
    """

    def __init__(self, x, y, z):
        """
        camera constructors
        """
        self.camerax = x
        self.cameray = y
        self.cameraz = z

    def TakePicture(self):
        """
        placeholder for picam handling code 
        """

def main():
    """
    Main function, for testing
    """
    
main()

