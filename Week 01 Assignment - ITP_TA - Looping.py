num = 5
x = 1
while x <= num:
    print("*"*x)
    x += 1

print()

num = 5
x = 1
while x <= num:
    print(" "*(num-x), "*"*x)
    x += 1

print()

num = 5
x = 0
while x <= num:
    print("*"*(num-x) + " "*x)
    x += 1

print()

num = 5
x = 0
while x <= num:
    print(" "*x + "*"*(num-x))
    x += 1

print()

num = 5
x = 1
while x <= num:
    print(" "*(num-x) + "*"*(x+(x-1)))
    x += 1

print()

num = 5
x = 1
while x <= num:
    print(" "*(num-x) + "*"*(2*x-1))
    x += 1
x = 1
while x <= num:
    print(" "*x + "*"*((num-x)*2-1))
    x += 1
