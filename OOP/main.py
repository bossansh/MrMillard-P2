##############################################################################
# Name: Anshul Prabu #221                                                   #
# Project: OOP Practice													    #
#                                                                           #
# Description: Creates vehicle class, and gives it two attributes. Makes a  #
# bus class and copies its attributes. Prints out attributes.				#                                          
#############################################################################


class Vehicle(): #step 1 Creates class
    def __init__(self, color, Vehiclename, mileage, maxspeed): #step 2 creates attributes for vehicle
        self.milesper = mileage 
        self.Max = maxspeed
        self.name = Vehiclename
        self.Color = color
    def update(self): #prints variables when update runs
        print("Color: ", self.Color, "Vehicle Name: ", self.name, "Speed: ", self.Max, "Mileage: ", self.milesper)
        print("Maintencance fee of", self.name, "is $",Vehicle.fare(self, capacity)) #step 7 runs the fare code when vehicle updates
    def seating_capacity(self, capacity): 
        print("The seating capacity of a ", self.name, "is ", capacity, "passengers")#prints capacity
        #on call
    def fare(self, capacity): 
        if type(self) == Bus: #checks if the vehicle is a bus
            return capacity * 100 + 0.1 * capacity *100 #if so adjusts the fare calculation
        else:
            return capacity * 100 #if not, does regular fare.
    def classfinder(self): #finds type of the parameter
        print("The", self.name, "is a ",type(self))
        
class Bus(Vehicle): #step 3 Creates bus class and gives it Vehicle's attributes
    pass 

class Car(Vehicle): #Creates car class and gives vehicle's attributes
    pass
capacity = 50
schoolBus = Bus("white", "School Lambo", 12, 180) #step 4 allows user to inputparameters
Audi = Car("white", "Audi Q5", 18, 240) #makes the car parameters
Vehicle.update(schoolBus) #runs update and prints them
Vehicle.update(Audi) #step 6 runs update and prints car stats
Vehicle.seating_capacity(schoolBus, 50) #step 5
Vehicle.classfinder(schoolBus) #step 8 displays class, Bus for schoolbus, car for audi
Vehicle.classfinder(Audi) 

#Step 9. School Bus is an instance of a vehicle class, as it is part of one of its subclasses
#, the bus class. It has all the attributes of the vehicle class.
