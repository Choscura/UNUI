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
     
    #Spatial positioning of origin point for actor
    actorx      =   (float)    
    actory      =   (float)
    actorz      =   (float)
    
    #spacial orientation (for directional headings)
    headingx    =   (float)
    headingy    =   (float)
    headingz    =   (float)

    
    def getposition(self):
        """
        gets the world's assessment of where the origin point of this actor is.
        returns the xyz coordinates as an array of floats""" 
        return [self.actorx, self.actory, self.actorz]

    def getheading(self):
        """
        gets the world's assessment of what point the actor is facing, from the origin point of this actor
        where the actor is. returns the xyz coordinates as an array of floats""" 
        return [self.headingx, self.headingy, self.headingz]

    def setposition(self, *args):
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
        HorizontalX             =   (self.camerax-actorx)
        HorizontalY             =   (self.cameray-actory)
        HorizontalHypotenuse    =   float(sqrt((HorizontalX**2)+(HorizontalY**2)))
        #Now for the vertical part:
        VerticalLeg             =   (self.cameraz-actorz)
        VerticalHypotenuse      =   float(sqrt((VerticalLeg**2)+(HorizontalHypotenuse**2)))
	#If it all worked, this should be the distance. 
        return VerticalHypotenuse
    
    def __tostring__(self):
        """
        Returns the name as a string of utf-8 encoded text
        """
        return self.name
    
    def __init__(self, *args, **kwargs):
        """
        initialization for 'actor' class
        """
        for arg in args:
            print(arg)
        #self.setposition(x, y, z)
        #self.name = name
            
class actorspace:
    """
    an 'actorspace' is a computational abstraction of a real, physical,
    3-dimensional environment. If a greenhouse is the 'book', this is 
    like the table of contents.
    """
    
    SpaceID     =   (str)   # a name for the humans to call the space being tracked, for the purposes of hci
    actorlist   =   []      # a list for the UID's of thte actors to be stored in

    def getactor(self, actor_ID):
        pass

    def __init__(self, *args, **kwargs):
        """
        constructor to initialize the actorspace
        Design intent is to pass metadata about actors in *args
                        and to pass meta about actor spaces in **kwargs

                        This is to separate attributes of plants from attributes of places and customers
        """
        for x in args:
            pass
        for x in kwargs:
            pass
    
    def __tostring__(self):
        """
        actorspace tostring returns the name of the space as a string so that the humans actually doing this know which space is which
        """
        return spacename


#"Cylinder actuator" refers to an actuator- a motor, piston, or whatever else that moves.
class cylinderactuator(actor):
    """
    this is a controller class for items such as motors (including servos and steppers, for the purposes of calculating the
    transformations that their rotations will apply to the other actors in the actorspace.
    """
    
    #an axle direction in order to constrain calculations as accurately as possible to the vector that motor/other axle rotates around
    axle_x  =   (float)
    axle_y  =   (float)
    axle_z  =   (float)

    #a positional description of what direction the shaft on the actuator axle has been rotated to face
    rotator_x = (float)
    rotator_y = (float)
    rotator_z = (float)

    def __init__(self):
        pass


class plant(actor):
    """
    a data member to represent the plant, as a descriptor of the CV calculation attributes in human-comprehendable form.
    read as "this is a dictionary to define the attributes of plants for computers, with descriptions for humans to properly identify
    said plants".  The premise is to describe the range of height, width, depth, spacing between plants, foliage density, and any 
    other relevant attributes necessary to figure out 1) how the humans have to interact with the plant, 2) how the cameras have to 
    interact with the plant, and 3) how the plant will change as time progresses.
    """
    species = (str)
    
    #plant foliage attributes
    foliage_height  =   (float)
    foliage_width   =   (float)
    foliage_depth   =   (float)
    
    def setsize(self, *args):
        pass

    def __init__(self, Species):
        self.species = Species
    
    def __tostring__(self):
        """
        actorspace tostring returns the name of the space as a string, for the humonkeys
        """
        return species  
 

class camera(actor):
    """     
    The camera class represents the physical cameras in the abstracted greenhouse/network space 
    """
    #   data members the camera needs to be able to make meaningful decisions about behavior
    #   Internal Camera Attributes <without external use>
    #   position of origin point (by default camera mounting point, since that is the 
    #   direct point of transform from which the camera's heading and position must necessarily be made.
    xorigin     =   (float)
    yorigin     =   (float)
    zorigin     =   (float)
    
    #       Networking Attributes
    Camera_SSID =   (str)   #   a string SSID assigned to the camera
    

    def __init__(self, *args, **kwargs):
        """
        camera constructors
        """
        self.xorigin = x
        self.yorigin = y
        self.zorigin = z

    def TakePicture(self):
        """
        placeholder for picam handling code 
        """


##################################################################################################################################
#                                           CODE BELOW IS FOR DEVELOPMENT ONLY                                                   #
##################################################################################################################################


def main():
    """
    Main function, for testing
    """
    try:
        #test actor
        derp = actor("derp", "derp2", "derp3", "derp4", "derp5")
        #test actorspace
        #test plant
        #test actuator
        #test camera

    
    except:
        print("Exception handled- something's fucked!")

    
main()

