# https://docs.python.org/2/tutorial/classes.html

############################################################################

# Encapsulation (global, local)

x = 0 # define x outside of method
def outer(): # define method
    x = 1 # set x local to outer(), it will remain 0 globally
    def inner(): # define method
        x = 2 # set x local to inner(), it will remain 0 globally and 1 within outer()
        print("inner ", x) # prints 2
    inner() # call inner() method to print 2
    print("outer ", x) # prints 1
    
outer() # calls outer() which calls inner() to prin 1 and 2 respectively
print("global ", x) # prints 0 due to global setting

# BUT if you specifically declare x to be global within one of the internal
# methods (encapsulated methods) then you can tell it to set the value
# globally as well as locally

x = 0
def outer():
    global x
    x = 1
    print("local: ", x)
outer()
print("global: ", x)

############################################################################

# Strings are immutable

a = "Foo" # creates an immutable string "Foo" and stores it in variable a
b = a # assigns "Foo" to b, they share the same data location
a = a + a # alters the mutable variable a to have the value "FooFoo"
          # BUT this does not alter the string "Foo", that remains where it is
          # instead it creates a new variable at a new data location
print a # prints "FooFoo"
print b # "prints "Foo" because b is still assigned to the original, immutable string location

############################################################################

# Namespaces/Modules

# Namespaces in Python map names to objects, they are essentially packages of functions
# contained within a specific area. For example, functions such as abs() are contained
# within the built-in names namespace. 

# In Python it is possible to have multiple functions with the same name providing
# that they are defined in different namespaces, you differentiate between the two
# by writing the namespace/module name first and then accessing via dot notation.

# In the namespace 'modname' you can have the function 'funcname', you would access
# this function via modname.funcname. Here, modname is the namespace/module and
# funcname is an attribute reference/attribute of the module.

# Scope refers to a region of the code in which a namespace is accessible. If you
# are outside the scope of a namespace then you cannot call upon its attributes
# or functionality, however you can within its scope. Building code which encapsulates
# namespaces is useful for ensuring that functionality can only be called upon
# when required.

# If you define a name globally then the scope extends to the module's global names
# enabling you to use references and assignments which are kept external to the local
# scope. However, if you do not do this then the variable/name remains local and even
# if you create an item with an identical name to one external to the current scope
# then you will only create a new variable and will not be able to assign or reference
# the external variable which shares its name.

############################################################################

# Classes
# 1) Basic Class Definition and Access
class TestClass:              # define class
    """My test class"""       # write class docs
    i = 123                   # class variable/attribute
    
    def f(self):              # define class method (methods are simply functions within a class)
        return 'hello world'  # function behaviour

print TestClass.i             # access class attribute
print TestClass().f()         # return output of f() method
print TestClass.__doc__       # show class docs

x = TestClass()               # create instance of class in a variable
x.i                           # access class behaviour via variable
print x.f()                   # return output of class method

# In the class above, the method 'f' takes an argument 'self', however, you
# can call the method without an argument (e.g. x.f()). This is because when
# you call a class method, the object 'x' is passed in as an argument itself,
# therefore x.f() is essentially TestClass.f(x).        
         
# 2) Class Initialisation
class InitClass:                       # define class
    def __init__(self, num1, num2):    # define initialisation method, when a class is called,
        self.one = num1                # it is initiated with the values num1 and num2
        self.two = num2                # these are initialisation values

x = InitClass(1, 4)                    # initialise the class with 2 vars (1 and 4)
print x.one                            # access the initialisation vars
print x.two                            # the purpose of this is to create class objects with starting values

# A instantiated class is an instance object because it is literally an
# instance of an object (the class definition). Instance objects let you
# access attribute references of which there are data attributes and methods.
# Data attributes are instance variables (e.g. x = 4 within a class) and
# methods are literally functions within a class.

# 3) Class and Instance Variables
# Class and instance variables are different. Class instances are accessible
# to all instances of a class (i.e. all class objects), whereas instance
# variables belong to a specific instance of a class only.

class Dog:                      # define class 'Dog'
    breed = 'labrador'          # define class variable 'breed'
    
    def __init__(self, name):   # initialisation method takes a name input
        self.name = name        # sets input name as method.name
        
dogOne = Dog('Pebbles')         # creates class instance/object with name 'Pebbles'
dogTwo = Dog('Fenton')          # creates class instance/object with name 'Fenton'

print dogOne.breed              # class variable is constant for all class objects
print dogTwo.breed              # class variable is constant for all class objects
print dogOne.name               # instance variable is specific to this class object
print dogTwo.name               # instance variable is specific to this class object


# If you are creating a variable which you intend to be mutable, then you should
# create this as an instance variable rather than a class variable because
# creating a mutable class variable means that all instances of that class
# would be changing the same shared variable, creating confusion.

class Dog:                          # define class 'Dog'
    breed = 'labrador'              # define class variable 'breed'
    #tricks = []                    # this would create a class variable, which is not good
        
    def __init__(self, name):       # initialisation method takes a name input
        self.name = name            # sets input name as method.name
        self.tricks = []

    def add_trick(self, trick):     # instead, define a method which takes a new trick
        self.tricks.append(trick)   # and append that to an instance variable list instead

dogOne = Dog('Norbet')
dogOne.add_trick('Fetch')
dogTwo = Dog('Lassie')
dogTwo.add_trick('Beg')
print dogOne.tricks
print dogTwo.tricks

# 4) Inheritance
# You can create classes (derived class) which inherit attributes/variables and
# methods from other classes (base class). These can be chained together so that
# if each base class inherits from another base class, the derived class has access
# to all variables and methods present in all linked classes. Derived classes can
# also override inherited classes if required - i.e. methods are 'virtual'.

class DerivedClass(BaseClass):          # basic inheritance syntax
    test = ""
class DerivedClass2(modname.BaseClass):  # same as above but base class is defined in another module
    BaseClass.method(self, arguments)   # access inherited methods

isinstance(obj, int)     # returns True if the object's class is int or a class derived/inherited from from int
issubclass(bool, int)    # returns True if the bool object is a subclass of int (in this case this is True)
issubclass(unicode, str) # same as above but this would return False because unicode is not a subclass of string

# You can also have multiple inheritance, here you specify multiple classes for
# your derived class to inherit from. In this case, the derived class inherits
# from the first names base class (and recursively filters through all of that
# base classes base classes) before moving onto the next and so on. You can also
# use super() to specify exactly how multiple inherited classes are filtered through.

class DerivedClass3(Base1, Base2, Base3):
    test = ""

# 5) Private variables and class-local references
# There is no way in Python to completely make a variable/method private to
# a particular class or encapsulation. However, there is some limited support
# to make vars ~private. By putting an underscore before a variable or method
# the compiler will read this _ as the classname prefixing the variable/method
# you are specifying, therefore you can avoid overriding inherited methods when
# using the same method name in different classes.

class Mapping:                             # define base class
    def __init__(self, iterable):          # initiate with an iterable variable
        self.items_list = []               # create class instance list
        self.__update(iterable)            # run iterable through method, making it ~private
        
    def update(self, iterable):            # define method
        for item in iterable:              # iterate through iterable
            self.items_list.append(item)   # populate class list with iterable
            
    __update = update
    
class MappingSubClass(Mapping):
    def update(self, keys, values):
        for item in zip(keys, values):
            self.items_list.append(item)















          
  
          
          
          
          
          
          
