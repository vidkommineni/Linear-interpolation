# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Names        Vidhya Kommineni
# Section:      562
# Assignment:   Lab 2
# Date:         9/8/22
#
from sympy import *
time1 = 10
time2 = 55
distance1 = 2026
distance2 = 23026
currenttime = 300

slope1 = (distance2 - distance1) / (time2 - time1)
yint = distance1 - (slope1 * time1)

currentdist = slope1 * 25 + yint
print("Part 1: ")
#J plugged in the number into the equation
print("For t = 25 minutes, the position p =", currentdist, "kilometers")

circumference = 2 * pi * 6745

# it is going to keep subtracting the curcumfrence from the distance as long as the distance is greater
currentdist = slope1 * currenttime + yint
while((currentdist) > circumference):
    (currentdist) -= circumference
    
print("Part 2:")
print("For t = 300 minutes, the position p =", currentdist.evalf(), "kilometers")



