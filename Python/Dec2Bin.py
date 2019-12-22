# method-1 using loops
n = int(input("Enter a decimal number: "))
holder = ""
if(n > 1):  
    while (n!=0):    
        holder += str(n%2)
        n=n//2
    print(' '.join(reversed(holder)),end=' ')
print()
# method2 - using recursion
m = int(input("Enter a decimal number: "))

def decimalToBinary(m):   
    holder2 = ""
    if(m > 0):              
        holder2 += str(m%2)
        decimalToBinary(m//2)
    print(' '.join(reversed(holder2)),end=' ')
# execute the method
decimalToBinary(m)

# method3 - using bin()
num=int(input("Enter a decimal number: "))
print(bin(num))