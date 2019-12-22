# print numbers from 1-100
for i in range(1,101,1):
    print(i,end=' ')

print("\n=================================================================================================================")

# print even/odd numbers from 1-100
for i in range(1,101,2):
    print(i,end=' ')

print("\n=================================================================================================================")

# print numbers divisible by 11 from 1-100
for i in range(0,101,11):
    print(i,end=' ')

print("\n=================================================================================================================")

# print the weights of a binary number byte eg: 1 2 4 8 16 ... 128
for i in range(0,8,1):
    print(2**i,end=' ')