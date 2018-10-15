#Chan Elizabeth (2201797001)
#Program for hotel management system

#define the Rooms class
class Rooms:
    def __init__(self, d, s): #initialize values of the class
        self.doublefee = int(d)
        self.singlefee = int(s)

    def Roomfee(self,rtype): #method to define the room fee
        rtype.lower()
        if rtype == "double":
            return self.doublefee
        elif rtype == "single":
            return self.singlefee

#define the Fee class
class Fee:
    FeeLists = [] #list to store the fees
    def addFee(self, d, s):  #method to store the room's fee to the list
        self.FeeLists.append(Rooms(d, s))

    def getfee(self, i): #method to get the room's fee from the list
        for i in range(len(self.FeeLists)):
            return self.FeeLists[i]


def roomfee(fee, rtype): #method to print the fee of the room type
    print("Category of room:")
    print("1. Single Bed (RP.{})".format(fee.Roomfee("single")))
    print("2. Double Bed (RP.{})".format(fee.Roomfee("double")))
    print("")
    Rfee = fee.Roomfee(rtype)
    return Rfee

#main function to manage the hotel system where people can check in and check out.
# Also to check the availability of rooms and the reserved rooms based on the room types
def main():
    single = []
    double = []
    singleroom = 10
    doubleroom = 10

    while True:
       #roomNumber()
       print("Welcome to vHotel, What do you want to do: ")
       print("""    1. Check in
    2. Check out
    3. Check reserved rooms
    Enter 'quit' to cancel """)
       userinput = input(": ")
       if userinput == "quit":
            break

       elif userinput == "1":
            print("Available room: single = {} double = {} ".format(singleroom, doubleroom))
            print("Room occupied: single = {} double = {} ".format(len(single), len(double)))
            roomType = input("Choose room type: ")
            if roomType == "single":
                roomfee(hotelOP.getfee(0), roomType)
                if len(single) < 10:
                 timestayed = int(input("how long you stayed: "))
                 print("Fee: Rp{}".format(roomfee(hotelOP.getfee(0), roomType) * timestayed))
                 RoomNum = int(input("Enter the room number: "))
                 single.append(RoomNum)
                 singleroom -= 1
                elif len(single) >= 10 :
                 print("No more single room")

                 proceed = input("Do you want to proceed (Y/N)?")
                 if proceed == "N":
                    print("Available room: single = {} double = {} ".format(singleroom, doubleroom))
                    print("Room occupied: single = {} double = {} ".format(len(single), len(double)))
                    break

            elif roomType == "double":
                roomfee(hotelOP.getfee(1), roomType)
                if len(double) < 10:
                 timestayed = int(input("how long you stayed: "))
                 print("Fee: Rp{}".format(roomfee(hotelOP.getfee(1), roomType) * timestayed))
                 RoomNum = int(input("Enter the room number: "))
                 double.append(RoomNum)
                 doubleroom -= 1
                elif len(double) >= 10 :
                 print("no more double room")
                 proceed = input("Do you want to proceed (Y/N)?")
                 if proceed == "N":
                    print("Available room: single = {} double = {} ".format(singleroom, doubleroom))
                    print("Room occupied: single = {} double = {} ".format(len(single), len(double)))
                    break

       elif userinput == "2":
            print("Available room: single = {} double = {} ".format(singleroom, doubleroom))
            print("Room occupied: single = {} double = {} ".format(len(single), len(double)))
            roomType = input("Choose room type: ")
            if roomType == "single":
                 RoomNum = int(input("Enter the room number: "))
                 if RoomNum in list(single):
                    single.remove(RoomNum)
                    singleroom += 1
                 else:
                     print("Room isn't registered")
                 proceed = input("Do you want to proceed (Y/N)?")
                 if proceed == "N":
                    print("Available room: single = {} double = {} ".format(singleroom, doubleroom))
                    print("Room occupied: single = {} double = {} ".format(len(single), len(double)))
                    break

            elif roomType == "double":
                  RoomNum = int(input("Enter the room number: "))
                  if RoomNum in list(double):
                    double.remove(RoomNum)
                    doubleroom += 1
                  else:
                    print("Room isn't registered")
                  proceed = input("Do you want to proceed (Y/N)?")
                  if proceed == "N":
                    print("Available room: single = {} double = {} ".format(singleroom, doubleroom))
                    print("Room occupied: single = {} double = {} ".format(len(single), len(double)))
                    break

       elif userinput == "3":
           print("--------------------------------")
           print("Single RoomsNo:  Double RoomsNo:")
           print("--------------------------------")
           print("{}                {}   ".format(single, double)) #display to total numbers of room registered
           print("--------------------------------")

hotelOP = Fee()
hotelOP.addFee(1000000, 500000)
main()

