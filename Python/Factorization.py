# This calculates the factors of a number
num = int(input("Enter an Integer:"))
for i in range(1,num//2+1):
    if (num%i==0):
        print(i)