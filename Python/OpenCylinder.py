print("Enter Cylinder Height:")
H=int(input())
print("Enter Cylinder Radius:")
R=int(input())
print("Enter Cost per square cm:")
CPS=float(input())

Z=2*H/R
Total=3.14*R*R*(1+Z)*CPS
print(Total)