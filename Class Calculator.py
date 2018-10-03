#Chan Elizabeth (2201797001)
#Calculator program using Class

#define the Calculator class
class Calculator:
    def __init__(self, A, B): #initialize values of the class
        self.A = A
        self.B = B

    def addition(self): #method to do addition
        add = self.A + self.B
        return add

    def subtraction(self): #method to do substraction
        sub = self.A - self.B
        return sub

    def multiplication(self): #method to do multiplication
        mul = self.A * self.B
        return mul

    def division(self): #method to do division
        div = self.A / self.B
        return div

#main fuction
def main():
 numlist = [0] #list to store result of the calculation
 while True:
   print("Options:")
   print("Enter 'add' to add two numbers")
   print("Enter 'subtract' to subtract two numbers")
   print("Enter 'multiply' to multiply two numbers")
   print("Enter 'divide' to divide two numbers")
   print("Enter 'quit' to end the program")
   user_input = input(": ")
   if user_input == "quit":
      break #stop the program if user inputted "quit"

   if numlist[0] == 0:
        a = int(input("Enter 1st number: "))
   else:
    a = numlist[0]
   b = int(input("Enter 2nd number: "))

   cal = Calculator(a, b) #cal is the object for the class passing the two numbers as parameters to the class.

   #Using cal, the respective method is called according to the choice taken from the user
   #and the respective result will be added to the stack
   if user_input == "add":
      numlist.append(cal.addition())
      del numlist[0] #delete the contain index 0 to replace it with the result of the calculation

   elif user_input == "subtract":
      numlist.append(cal.subtraction())
      del numlist[0]

   elif user_input == "multiply":
      numlist.append(cal.multiplication())
      del numlist[0]

   elif user_input == "divide":
       numlist.append(cal.division())
       del numlist[0]

   else:
      print("Unknown input") #output if the user entered the unknown options
   print(numlist[0]) #print the result of the calculation store in the list

main()
