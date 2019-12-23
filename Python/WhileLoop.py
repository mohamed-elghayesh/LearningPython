# pre-test event-loop (sentinel-loop) that stops executing when an event is reached
# number of iterations is not pre-known

# example1 - print numbers 0-4
i1=0  # initialize loop control
while (i1 <= 4):  # test loop condition
    print(i1)     # execute the loop body
    i1+=1  # update loop control
print()

# example2 - print numbers 1-128 using while-loop
i2=1
while (i2 < 200):
    print(i2)
    i2=i2*2
print()
