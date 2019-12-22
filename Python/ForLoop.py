# "for loop" is used as a counting loop (numbre of iterations is pre-known)
# "for" uses a range, list, or a string (tracing example is needed) 
# pre-test loop (post-test loop "do-while" is not implemented in python) 

# Foreward
for i1 in range(1,7):
    print(i1**2)
print()
# Reversed
for i2 in range(5,0,-1):
    print(i2)
print()
# From List
for i3 in [1,2,4,8,16]:
    print(i3)
print()
# From a string
for i4 in "Hello World!":
    print(i4, end=', ')
print()
# for .. else and [break continue pass]
# break: exit out of a loop on an event
# continue: skip this round and complete the rest of the loop
# pass: can be used as placeholders while thinking about conditions 

for i5 in [1,8,9.1,3,4.5,-1.3,12]:
    if(i5 < 0):
        print("We have a -ve in the list --> ",i5)
        continue
else:
    print("This code will not run because of BREAK, but CONTINUE and PASS will reach it")