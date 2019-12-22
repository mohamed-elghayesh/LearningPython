# pre-test event-loop (sentinel-loop) that stops executing when an event is reached
# number of iterations is not pre-known

# example1 - print numbers 0-4
i1=0
while (i1 <= 4):
    print(i1)
    i1+=1
print()

# example2 - print numbers 1-128 using while-loop
i2=1
while (i2 < 200):
    print(i2)
    i2=i2*2
print()
