from math import sqrt

# Rocket class
class Rocket(object):
    """Rocket simulates a rocket ship for a game"""
    
    # Constructor method, defines starting parameters for class object
    def __init__(self): # this is built automatically when you create a class object
        # Initiate Rocket with (x,y) coordinates
        self.x = 0 # self lets you access a variable from anywhere
        self.y = 0 # else in the class
        # the self keyword is like a key to all other objects in the class,
        # by putting this first it gives the object access to all other
        # class attributes.
        
    # Increment y-position of Rocket
    def move_up(self): # putting self here gives this method access to the
        self.y += 1    # object which is calling the method, here it lets
                       # us access the y attribute#s value.
        
# Create rocket object (instance of class)
rocket1 = Rocket() # instantiate class as rocket1 object
rocket1.move_up() # call class object method
print rocket1 # shows this object is a Rocket object from the __main__ file
print "Rocket altitude: ", rocket1.y

# Create a fleet of rockets   
my_rockets = [Rocket() for x in xrange(0,5)]
for rocket in my_rockets:
    print(rocket)
    
# changing the values of each one does not affect any other
my_rockets[0].move_up() 
print [rocket.y for rocket in my_rockets]

# the above class initiates the x and y values for a class object to
# (0,0), however we can provide the option to define the starting (x,y)
# coords when the object is created as follows

class RocketCustom(object):
    """Create a rocket with custom values"""
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        
    # move rocket (x,y) with default (0,1)    
    def move_rocket(self, x_increment=0, y_increment=1):
        self.x += x_increment
        self.y += y_increment
        
    def distance_from(self, other_rocket):
        distance = sqrt((self.x - other_rocket.x)**2 + (self.y - other_rocket.y)**2)
        return distance
        
        
# create fleet of custom rockets
my_custom_rockets = [RocketCustom() for x in xrange(0,5)]
my_custom_rockets[0].move_rocket(10,-10)
my_custom_rockets[3].move_rocket(5,25)
for index, rocket in enumerate(my_custom_rockets):
    print "Rocket %d is at %d, %d" % (index, rocket.x, rocket.y)
    
# check distance
rocket1 = RocketCustom(5,5)
rocket2 = RocketCustom(15,15)
print "The rockets are %d units apart." % rocket1.distance_from(rocket2)
    
