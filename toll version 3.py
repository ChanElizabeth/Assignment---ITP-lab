#Chan Elizabeth (2201797001)
#Program for toll gate

#define the Vehicle class
class Vehicle:
    def __init__(self, vtype): #initialize values of the class
        self.vehicle = vtype

#define the Tollgate class
class Tollgate:
    def __init__(self, location, c, b, t): #initialize values of the class
        self.cartotal = 0
        self.bustotal = 0
        self.trucktotal = 0
        self.location = location
        self.carfee = int(c)
        self.busfee = int(b)
        self.truckfee = int(t)

    def vehiclefee(self,vtype): #method to define the vehicle fee
        vtype.lower()
        if vtype == "car":
            return self.carfee
        elif vtype == "bus":
            return self.busfee
        elif vtype == "truck":
            return self.truckfee


    def addvehicle(self,vtype): #method to total the numbers of vehicle
        vtype.lower()
        if vtype == "car":
            self.cartotal += 1
        elif vtype == "bus":
            self.bustotal += 1
        elif vtype == "truck":
            self.trucktotal += 1

    def getloc(self): #method to get the toll location
        return self.location

    def getcarfee(self): #method to get the car fee
        return self.carfee

    def getbusfee(self): #method to get the bus fee
        return self.busfee

    def gettruckfee(self): #method to get the truck fee
        return self.truckfee

    def getcartotal(self): #method to get the total the numbers of car
        return self.cartotal

    def getbustotal(self): #method to get the total the numbers of bus
        return self.bustotal

    def gettrucktotal(self): #method to get the total the numbers of truck
        return self.trucktotal

#define the TollOperator class
class TollOperator:
    GateLists = [] #list to store the data for the toll gate
    def addGate(self, location, c, b, t): #method to store the location and the vehicle's fee to the list
        self.GateLists.append(Tollgate(location, c, b, t))

    def getgate(self, i): #method to get the toll location along with the vehicle's fee from the list
        return self.GateLists[i]

def title(): #method to print the title of the toll
       print("="* 50)
       print(" "* 15 + "Toll Payment Systems")
       print(" "* 15 + "PT Jasa Marge, Tbk.")
       print("="* 50)


def tolllocation(gate, vtype): #method to print the fee of the vehicle according to the toll location choosen
    print("Location of Toll gate: {}".format(gate.getloc()))
    print("Category of vehicle:")
    print("1. Car (RP.{})".format(gate.vehiclefee("car")))
    print("2. Bus (RP.{})".format(gate.vehiclefee("bus")))
    print("3. Truck (RP.{})".format(gate.vehiclefee("truck")))
    print("")
    print("Fee: {}".format(gate.vehiclefee(vtype)))
    print("")

def revenue(gate): #method to total the revenue of the vehicle according to the toll location
    print("Location of Toll gate:{}".format(gate.getloc()))
    print("-------------")
    print("Car Bus Truck")
    print("-------------")
    print("{}   {}   {}".format(gate.getcartotal(), gate.getbustotal(), gate.gettrucktotal()))
    print("-------------")
    rev = gate.getcarfee()*gate.getcartotal() + gate.getbusfee()*gate.getbustotal() + gate.gettruckfee()*gate.gettrucktotal()
    print("Total revenue: RP {}".format(rev))

def getrevenue(gate): #method to get the revenue of the vehicle
    rev = gate.getcarfee()*gate.getcartotal() + gate.getbusfee()*gate.getbustotal() + gate.gettruckfee()*gate.gettrucktotal()
    return rev

#main function to check the vehicles that enter the toll and total the numbers of vehicle enter the toll according to the toll location
def main():
    while True:
       title()
       userinput = input("Choose vehicle type: ").lower() #enter the vehicle type
       locinput = input("Choose location: ") #enter the location of the toll
       if locinput == "Meruya":
           tolllocation(tollOP.getgate(0), userinput)
           tollOP.getgate(0).addvehicle( userinput)
       elif locinput == "Pondok Aren":
           tolllocation(tollOP.getgate(1), userinput)
           tollOP.getgate(1).addvehicle( userinput)
       isLooping = True
       while isLooping:
        otherV = input("Is there any other vehicle (Y/N)?")
        if otherV == "Y":
            userinput = input("Enter vehicle type: ").lower()
            if locinput == "Meruya":
                tolllocation(tollOP.getgate(0), userinput)
                tollOP.getgate(0).addvehicle(userinput)
            elif locinput == "Pondok Aren":
                tolllocation(tollOP.getgate(1), userinput)
                tollOP.getgate(1).addvehicle(userinput)
        elif otherV == "N":
         while True:
            otherG = input("Is there any other Toll gate location (Y/N)?")
            if otherG == "N":
                revenue(tollOP.getgate(0))
                revenue(tollOP.getgate(1))
                print("GRAND TOTAL REVENUE: {}".format(getrevenue(tollOP.getgate(0))+getrevenue(tollOP.getgate(1))))
                #print the total revenue of all the location
                quit()
            else:
                isLooping = False
                break
        print("")

tollOP = TollOperator() #tollOP is the object for the class
tollOP.addGate("Meruya", 6000, 8000, 10000) #the location along with vehicle fees are pass as parameters to the class.
tollOP.addGate("Pondok Aren", 18000, 20000, 25000) #the location along with vehicle fees are pass as parameters to the class.

main()



