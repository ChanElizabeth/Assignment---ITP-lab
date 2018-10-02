stack = [0]
while True:
   print("Options:")
   print("Enter 'add' to add two numbers")
   print("Enter 'subtract' to subtract two numbers")
   print("Enter 'multiply' to multiply two numbers")
   print("Enter 'divide' to divide two numbers")
   print("Enter 'quit' to end the program")
   user_input = input(": ")
   if user_input == "quit":
      break
   if stack[0] == 0:
        a = int(input("Enter 1st number: "))
   else:
       a = stack[0]
   b = int(input("Enter 2nd number: "))

   if user_input == "add":
       add = lambda a,b:a+b
       stack.append(add(a,b))
       del stack[0]
   elif user_input == "subtract":
       sub = lambda a,b:a-b
       stack.append(sub(a,b))
       del stack[0]
   elif user_input == "multiply":
       mul = lambda a,b:a*b
       stack.append(mul(a,b))
       del stack[0]
   elif user_input == "divide":
       div = lambda a,b:a/b
       stack.append(div(a,b))
       del stack[0]
   else:
      print("Unknown input")
   print(stack[0])


