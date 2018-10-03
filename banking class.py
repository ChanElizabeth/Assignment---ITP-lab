#Chan Elizabeth(2201797001)
#ATM program using class

#define the Account class
class Account:
    def __init__(self, balance): #initialize values of the class
        self.balance = float(balance)

    def getBalance(self): #method to get balance of an account
        return self.balance

    def deposit(self, amount): #method to deposit amount to balance
        self.balance += amount
        return self.balance

    def withdraw(self, amount): #method to withdraw amount to balance
        #condition where balance inside account must be greater than the amount to be withdraw
        if self.balance >= amount:
            self.balance -= amount
        return self.balance

#define the Customer class
class Customer:

    def __init__(self, firstName, lastName, Account):
        self.firstName = str(firstName)
        self.lastName = str(lastName)
        self.account = Account

    def getfirstName(self): #method to get first name of customer
        return self.firstName

    def getlastName(self): #method to get last name of customer
        return self.lastName

    def setAccount(self): #method to set account
        return self.account

#define the Bank class
class Bank:
    CustomerL = [] #list of Customer's account
    def __init__(self, bankName):
        self.bankName = bankName

    def addCustomer(self, firstName, lastName): #method to add customer by inserting their first and last name
        self.CustomerL.append(Customer(firstName, lastName, Account(0))) #customer's account created is added to CustomerL

    def getNumOfCustomers(self): #method to get the total number of customers
        return len(self.CustomerL)

    def getCustomer(self, i): #method to get customer from the index of CustomerL
        return self.CustomerL[int(i)]

    def getCustomerid(self, firstName, lastName): #method to get index of the customer from CustomerL
        FullName = firstName + lastName
        for x in range(0, len(self.CustomerL)):
            Chkfullname = self.CustomerL[x].getfirstName() + self.CustomerL[x].getlastName()
            if FullName == Chkfullname:
                id = str(x)
                return id

bankaca = Bank("Bank ACA") #bankaca is the object for the class passing the data as parameters to the class.

def main():
    while True:
       print("Welcome to ATM {}, What do you want to do: ".format(bankaca.bankName))
       print("""    1. Create Customer's account
    2. Get Customer Id
    3. Get Customer Balance
    4. Deposit
    5. Withdraw
    6. Transfer
    Enter 'quit' to end the transaction """)
       userinput = input(": ")
       if userinput == "quit":
          break

       elif userinput == "1":
          FullName = input("Enter the first name and last name" ": ")
          splinput = FullName.split(" ")
          bankaca.addCustomer(splinput[0], splinput[1]) #addCustomer by name to the bankaca
          print("{} {} is registered".format(splinput[0], splinput[1])) #to tell customer's account has been registered

       elif userinput == "2":
          FullName = input("Enter the first name and last name" ": ")
          splinput = FullName.split(" ")
          getid = bankaca.getCustomerid(splinput[0], splinput[1]) #take result from getCustomerid function
          print("'{}' is your id".format(getid)) #tell the customer's id to the customer

       elif userinput == "3":
           id = int(input("Enter your id to check your account's balance: "))
           balance = bankaca.getCustomer(id).account.getBalance() #take result from getBalance function
           print("Your account's balance is ${}".format(balance)) #tell the account's balance to the customer

       elif userinput == "4":
           id = int(input("Enter your id to deposit amount into your account: "))
           amount = float(input("Enter the amount to be deposit into the account: "))
           deposit = bankaca.getCustomer(id).account.deposit(amount) #take result from deposit function
           print("You had deposited ${}. Your account's new balance is ${}".format(amount, deposit))
           #tell the customer the amount deposited and the new balance of the account

       elif userinput == "5":
           id = int(input("Enter your id to withdraw amount from your account: "))
           balance = bankaca.getCustomer(id).account.getBalance()
           amount = float(input("Enter the amount to be withdraw from your account: "))
           if balance >= amount:
            #condition the account's balance must be greater than the amount to be withdraw so the transaction can take place
                withdraw = bankaca.getCustomer(id).account.withdraw(amount) #take result from withdraw function
                print("You had successfully withdraw ${}. Your current balance is ${}".format(amount, withdraw))
                #tell that withdraw has been done succesfully and the current balance after withdraw
           else:
                print("Withdraw Fails : not enough amount to be taken from your account")
                #tell that the transaction withdraw failed

       elif userinput == "6":
           id = int(input("Enter your id to transfer amount: "))
           destId = int(input("Enter the id you want to transfer the amount to: "))
           balance = bankaca.getCustomer(id).account.getBalance()
           amount = float(input("Enter the amount you want to transfer: "))
           if balance >= amount:
                withdraw = bankaca.getCustomer(id).account.withdraw(amount)
                #take result from withdraw function where the sender's balance has been withdraw for the transferred
                bankaca.getCustomer(destId).account.deposit(amount)
                #take result from deposit function where the receiver's balance has been deposited with the amount transferred
                print("Transfer successfully. You had transferred ${} to '{}'. Your current balance is ${}".format(amount, destId, withdraw))
                #tell about the successful transfer transaction
           else:
                print("Transfer Fails : not enough amount to transfer")
                #tell that the transfer transaction failed
       else:
           print("Unknown userinput") #output if the user entered the unknown input
           break #stop the program


main()
