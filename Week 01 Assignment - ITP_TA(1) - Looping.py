num = 5 #the total number of lines
x = 1 #the first line to be run
while x <= num: #do the process in limited loop
    print("*"*x) #print the asterisks according to the value of x
    x += 1 #to continue to next line

print()

num = 5
x = 1
while x <= num:
    print(" "*(num-x), "*"*x) #print num-x spaces then x *
    #the number of spaces decrease down the line and number of * increase down the line
    x += 1

print()

num = 5
x = 0
while x <= num:
    print("*"*(num-x) + " "*x) #print num-x * then x spaces
    #the number of * decrease down the line and number of spaces increase down the line
    x += 1

print()

num = 5
x = 0
while x <= num:
    print(" "*x + "*"*(num-x)) #print x spaces then num-x *
    #the number of spaces increase down the line and number of * decrease down the line
    x += 1

print()

num = 5
x = 1
while x <= num:
    print(" "*(num-x) + "*"*(x+(x-1))) #print num-x spaces then (x+(x-1)) *
    #the number of spaces decrease down the line and number of * increase down the line
    x += 1

print()

num = 5
x = 1
while x <= num:
    print(" "*(num-x) + "*"*(2*x-1)) #print num-x spaces then ((2*x)-1) *
    #the number of spaces decrease down the line and number of * increase down the line
    x += 1
x = 1
while x <= num:
    print(" "*x + "*"*((num-x)*2-1)) #print x spaces then ((num-x)*2-1) *
    #the number of * decrease down the line and number of spaces increase down the line
    x += 1
