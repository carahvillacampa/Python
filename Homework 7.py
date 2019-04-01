#Erica Filgueras Homework 7 CSC 243

#you didn't need to repeat __str__ for everything

class Vehicle:

    def __init__(self, mode, maxPassengers, odometer):
        'initializes variables mode, maxPassengers and odometer'
        self.maxPassengers= maxPassengers
        self.odometer= odometer
        self.mode= mode
    def odometerAdd(self, num):
        self.odometer += num  
    def __str__(self):
        return 'Mode of transport is: {}\nCan carry up to:{}\nOdometer: {}'.format(self.mode,
                self.maxPassengers,self.odometer)
    def __eq__(self, other):
        '__dict__ returns all attributes of the object;this compares all attributes of both objects'
        return self.maxPassengers == other.maxPassengers and self.odometer == other.odometer and self.mode==other.mode

    
class Car(Vehicle):
    'Problem 2'
    def __init__(self, mode,maxPassengers,odometer, make,model,color):
        super().__init__(mode,maxPassengers, odometer)
        self.make= make
        self.model=model
        self.color= color
    def __str__(self):
        return 'Mode of transport is: {}\nCan carry up to: {}\nOdometer:{}\nMake: {}\nModel: {}\nColor: {}'.format(self.mode,
                self.maxPassengers,self.odometer, self.make,self.model,self.color)
    def __eq__(self, other):
        return self.make==other.make and self.model== other.model and self.color==other.color 
class Boat(Vehicle):
    'Problem 3'
    def __init__(self, mode,maxPassengers,odometer, length, horsepower):
        super().__init__(mode, maxPassengers,odometer)
        self.length= length
        self.horsepower= horsepower
    def __str__(self):
        return 'Mode of transport is: {}\nCan carry up to: {}\nOdometer: {}\nLength:{}\nHorsepower:{}'.format(self.mode,
                self.maxPassengers,self.odometer, self.length, self.horsepower)
    def __eq__(self,other):
        return self.length==other.length and self.horsepower==other.horsepower



'''
Super basically delegates the method calls to the parent class without
explicitly naming them. It allows your current class to access the inherited
variables that has been overwritten.For example, the method Car uses the super
function to refer to the arguments inside it's initmethod (mode, maxPassengers,
odometer) to the Parent class Vehicle. It shortens your code because it
eliminates the need to declare certain characteristics that's already demanded
in the Parent Class.

'''




