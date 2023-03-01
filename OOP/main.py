##############################################################################
# Name: Anshul Prabu #221                                                   #
# Project: OOP Practice													    #
#                                                                           #
# Description: Creates vehicle class, and gives it two attributes. Makes a  #
# bus class and copies its attributes. Prints out attributes.				#                        #                   #
#############################################################################


class Vehicle(): #step 1 Creates class
    def __init__(self, color, Vehiclename, mileage, maxspeed): #step 2 creates attributes for vehicle
        self.milesper = mileage 
        self.Max = maxspeed
        self.name = Vehiclename
        self.Color = color
    def update(self): #prints variables when update runs
        print("Color: ", self.Color, "Vehicle Name: ", self.name, "Speed: ", self.Max, "Mileage: ", self.milesper)
    def seating_capacity(self, capacity): 
        print("The seating capacity of a ", self.name, "is ", capacity, "passengers")#prints capacity
        #on call
    def fare(self, capacity): 
        return capacity * 100
        
class Bus(Vehicle): #step 3 Creates bus class and gives it Vehicle's attributes
    pass
class Car(Vehicle): #Creates car class and gives vehicle's attributes
    pass
capacity = 50
schoolBus = Bus("white", "School Lambo", 12, 180) #step 4 allows user to inputparameters
Audi = Car("white", "School Lambo", 18, 240) #makes the car parameters
Vehicle.update(schoolBus) #runs update and prints them
Vehicle.update(Audi) #step 6 runs update and prints car stats
Vehicle.seating_capacity(schoolBus, 50) #step 5
