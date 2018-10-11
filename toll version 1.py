#Chan Elizabeth (2201797001)
#Program for toll gate

#define the Vehicle class
class Vehicle:
    def __init__(self, vtype): #initialize values of the class
        self.vehicle = vtype

#define the Tollgate class
class Tollgate:
    def __init__(self, c, b, t): #initialize values of the class
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

    def getcarfee(self): #method to get the car fee
        return self.carfee

    def getbusfee(self): #method to get the bus fee
        return self.busfee

    def gettruckfee(self): #method to ge the truck fee
        return self.truckfee

#define the TollOperator class
class TollOperator:
    FeeLists = [] #list to store the fees
    def addFee(self, c, b, t):  #method to store the vehicle's fee to the list
        self.FeeLists.append(Tollgate(c, b, t))

    def getfee(self, i): #method to get the vehicle's fee from the list
        for i in range(len(self.FeeLists)):
            return self.FeeLists[i]

def title(): #method to print the title of the toll
       print("="* 50)
       print(" "* 15 + "Toll Payment Systems")
       print(" "* 15 + "PT Jasa Marge, Tbk.")
       print("="* 50)


def tollfee(fee, vtype): #method to print the fee of the vehicle
    print("Category of vehicle:")
    print("1. Car (RP.{})".format(fee.vehiclefee("car")))
    print("2. Bus (RP.{})".format(fee.vehiclefee("bus")))
    print("3. Truck (RP.{})".format(fee.vehiclefee("truck")))
    print("")
    print("Fee: {}".format(fee.vehiclefee(vtype))) #fee of the vehicle entered
    print("")

#main function to check the vehicles that enter the toll
def main():
    while True:
       title()
       userinput = input("Choose vehicle type: ").lower() #enter the vehicle type
       if userinput == "car":
           tollfee(tollOP.getfee(0), userinput)
       elif userinput == "bus":
           tollfee(tollOP.getfee(1), userinput)
       elif userinput == "truck":
           tollfee(tollOP.getfee(2), userinput)
       isLooping = True
       while isLooping:
        otherV = input("Is there any other vehicle (Y/N)?")
        if otherV == "Y":
            userinput = input("Enter vehicle type: ").lower()
            if userinput == "car":
                tollfee(tollOP.getfee(0), userinput)
            elif userinput == "bus":
                tollfee(tollOP.getfee(1), userinput)
            elif userinput == "truck":
                tollfee(tollOP.getfee(2), userinput)
        else:
            quit()
        print("")

tollOP = TollOperator() #tollOP is the object for the class
tollOP.addFee(6000, 8000, 10000) #the vehicle fees are pass as parameters to the class.

main()
