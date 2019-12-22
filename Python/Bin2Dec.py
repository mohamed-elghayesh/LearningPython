# method1 - using while loop
binary = int(input("Enter a binary number: "))
decimal1, i, n = 0, 0, 0
while(binary != 0): 
    dec = binary % 10
    decimal1 = decimal1 + dec * pow(2, i) 
    binary = binary//10
    i += 1
print("method1: ",decimal1)

# method2 - using int with base-2
binary2 = input("Enter a binary number: ")
decimal2 = int(binary2,2)
print("method2: ",decimal2)

# ASCII || decimal
character = 'A'
print("Ascii of A: ",ord(character))

print("Letter equals to 87: ",chr(87))

# hexa to decimal
print(int('0xfde',0))