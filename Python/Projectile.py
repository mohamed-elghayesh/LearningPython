import math

g=32.17
print("Input Theta in radians:")
theta=float(input())
print("Input the velocity:")
velocity=float(input())
print("Input the distance:")
distance=float(input())

time=distance/(velocity*math.cos(theta))
height=velocity*math.sin(theta)*time-(g*time*time/2)

print("Time = ",time)
print("Height = ",height)
