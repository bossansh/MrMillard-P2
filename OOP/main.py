#############################################################################
# Name: Anshul Prabu #221                                                   #
# Project: OOP Practice													    #
#                                                                           #
# Description: Creates vehicle class, and gives it two attributes. Makes a  #
# bus class and copies its attributes				                        #                   #
#############################################################################


class Vehicle(): #step 1 Creates class
    def __init__(self, mileage, maxspeed): #step 2 creates attributes for vehicle
        self.milesper = mileage
        self.Max = maxspeed
        pass
        
class Bus(Vehicle): #step 3 Creates bus class and gives it Vehicle's attributes
    def __init__(self, Vehicle, Vehiclename):
        super().__init__()
        self.name = Vehiclename
    def update(self):
        print("Vehicle Name: ", self.name, "Speed: ", self.Max, "Mileage: ", self.milesper)

schoolVehicle = Vehicle(12, 180)
schoolBus = Bus(schoolVehicle, "School Lambo")
Bus.update(schoolBus)
