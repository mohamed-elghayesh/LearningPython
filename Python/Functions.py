# Top-Down problem breakdown

# arithmetic operations
def simple_add():
    x=2
    y=5
    print("First add returns: ", x+y)
    # return x+y

def add(x=10, y=20, z=15):
    print("defaults add returns: ", x+y+z)
    # return x+y+z

# GCD of two numbers, Greatest common divisor
def gcd(a,b):
    while (a!=0):
        a,b = b%a, a
    return b

# Calling the functions
print("executing the gcd(a,b)",gcd(12,20))
print("executing simple_add: ", simple_add())
print("executing add with no parameters: ", add())
print("executing add with one parameter: ", add(2))
print("executing add with two parameters: ", add(2,9))
print("executing add with three parameters: ", add(2,9,28))
