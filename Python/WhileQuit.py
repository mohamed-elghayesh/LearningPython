# the body of the loop will continue until the user press Q or q
loop_on = 'A'
while (loop_on not in ('Q','q')):
    print("executing the loop :) ")
    loop_on = input("Press any key to continue, press Q-q to quit: ")