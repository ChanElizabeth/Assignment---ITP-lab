import datetime

class Car:
    def __init__(self, plate):
        self.nPlate = plate
        now = datetime.datetime.now().strftime("%H:%M")
        self.timeIn = datetime.datetime.strptime(now, "%H:%M")

    def calculatePrice(self, out):
        timeOut = datetime.datetime.strptime(out, "%H:%M")
        timeParked = timeOut - self.timeIn
        timeParkedSplit = str(timeParked).split(":")
        hour = int(timeParkedSplit[0])
        min = int(timeParkedSplit[1])
        if min > 0:
            hour += 1

        return hour * 1000

class Cars:
    ListOfCars = []
    def __init__(self,nplate):
        self.nplate = nplate

    def addCars(self, nplate):
        self.ListOfCars.append(Car(nplate))

    def deleteCar(self, plate):
        for i in range(0, len(self.ListOfCars)):
            if self.ListOfCars[i].nPlate == plate:
                del self.ListOfCars[i]

    def getIndex(self, plate):
        for i in range(0, len(self.ListOfCars)):
            if self.ListOfCars[i].nPlate == plate:
                return i

cars = Cars("PlateNum")

def parkingLot():
    for i in range(0, len(cars.getListCars())):
        print("[{}]".format(cars.getListCars()[i].nPlate), end=", ")
    if len(cars.getListCars()) == 0:
        print("")
    else:
        print("are in the parking lot")
        
def main():
    while True:
       parkinglot()
       print("Welcome to Parking Lot, What do you want to do: ")
       print("""    1. Go in the parking lot
    2. Go out the parking lot
    Enter 'quit' to cancel """)
       userinput = input(": ")
       if userinput == "quit":
            break

       elif userinput == "1":
            PlateNum = input("Enter your car's plate number: ")
            cars.addCars(PlateNum)
            print("{} has parked".format(PlateNum))

       elif userinput == "2":
            PlateNum = input("Enter your car's plate number: ")
            if cars.getIndex(PlateNum) == None:
                print("The car isn't found in the parking lot")
                break
            else:
                i = cars.getIndex(PlateNum)
            TimeOut = input("What time do you go out: ")
            totalprice = cars.ListOfCars[i].calculatePrice(TimeOut)
            print("You must pay {}".format(totalprice))

main()
