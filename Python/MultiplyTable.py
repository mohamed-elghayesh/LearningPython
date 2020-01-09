import dis

# prints the multiplication table from 1 to 12
def multiply (x,y):
    for i in range(1,x+1):
        for j in range(1,y+1):
            print(i," x ", j , " = ", i*j)

multiply(10,10)
dis.dis(multiply)