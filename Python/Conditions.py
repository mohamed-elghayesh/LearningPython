x = int(input("Input X : "))
y = int(input("Input Y : "))
z = int(input("Input Z : "))

# comparing any 2 numbers
if (x>y):
    print("X is GT Y")
elif (x==y):
    print("X equals Y")
else:
    print("Y is GT X")

# comparing 3 different numbers
if (x>y) and (x>z):
    print("X is GT Y and Z")
elif (y>z):
    print("Y is GT X and Z")
else:
    print("Z is GT X and Y")