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
    
    uniqueID = (int)        # a unique identifier to facilitate selection
    name = (str)            # a name to help humans interact with actor data
     
    #Spatial positioning
    actorx = (float)
    actory = (float)
    actorz = (float)
    
    #spacial orientation
    transformx = (float)
    transformy = (float)
    tronsformz = (float)

    
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
    
    def __tostring__(self):
        return self.name
    
    def __init__(self, x, y, z, name):
        """
        initialization for 'actor' class
        """
        self.setposition(x, y, z)
        self.name = name
            
class actorspace:
    """
    an 'actorspace' is a computational abstraction of a real, physical, 3-dimensional environment.
    If a greenhouse is the 'book', this is like the table of contents.
    """
    
    spacename = (str)       # a name for the humans to call the space being tracked, for the purposes of hci
    actorlist = []          # a list for the UID's of thte actors to be stored in

    def __init__(self, spacename):
    """
    constructor to initialize the actorspace
    """
        self.spacename = spacename
    
    def __tostring__(self):
    """
    actorspace tostring returns the name of the space as a string so that the humans actually doing this know which space is which
    """
        return spacename


class cylinderactuator(actor):
    """
    this is a controller class for items such as motors (including servos and steppers, for the purposes of calculating the
    transformations that their rotations will apply to the other actors in the actorspace.
    """
    
    #an axle direction in order to constrain calculations as accurately as possible to the vector that motor/other axle rotates around
    axle_x = (float)
    axle_y = (float)
    axle_z = (float)

    #a positional description of what direction the shaft on the actuator axle has been rotated to face
    rotator_x = (float)
    rotator_y = (float)
    rotator_z = (float)

    def __init__(self):
        pass


class plant(actor):
    """
    a data member to represent the plant
    """
    species = (str)
    
    def __tostring__(self):
    """
    actorspace tostring returns the name of the space as a string, for the humonkeys
    """
        return species
   
 
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

##################################################################################################################################
                                                CODE BELOW IS FOR DEVELOPMENT ONLY
##################################################################################################################################

def main():
    """
    Main function, for testing
    """
 
main()
    
