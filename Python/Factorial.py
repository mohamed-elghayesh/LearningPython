# Calculate the factorial of a number
number = int(input("Please enter a number: "))
factorial = 1

for i in range (1,number+1):
    factorial*=i
print ("Factorial : ", factorial)

# also check math.factorial(num)