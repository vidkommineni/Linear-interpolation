# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Vidhya Kommineni
#               Ayushi Sharma
#               James Poe
#               Conner Kurtin 
# Section:      562
# Assignment:   Lab 3 Team
# Date:         9/15/22



import math



t1 = float(input("Enter time 1:"))
x1 = float(input("Enter the x position of the object at time 1:"))
y1 = float(input("Enter the y position of the object at time 1:"))
z1 = float(input("Enter the z position of the object at time 1:"))

t2 = float(input("Enter time 2:"))
x2 = float(input("Enter the x position of the object at time 2:"))
y2 = float(input("Enter the y position of the object at time 2:"))
z2 = float(input("Enter the z position of the object at time 2:"))

# 'first' is the initial time
first = t1
x = ((x2-x1)/(t2-t1))*(first-t1) +x1
y=((y2-y1)/(t2-t1))*(first-t1)+y1
z=((z2-z1)/(t2-t1))*(first-t1)+z1
print(f"At time {first:.2f} seconds the object is at ({x:.3f}, {y:.3f}, {z:.3f})")
print("")

tt1 = (t2-t1)/4
#calculating the position at time tt2 by adding an increment to tt1
tt2 = tt1 + t1
x = ((x2-x1)/(t2-t1))*(tt2-t1) +x1
y=((y2-y1)/(t2-t1))*(tt2-t1)+y1
z=((z2-z1)/(t2-t1))*(tt2-t1)+z1
print(f"At time {tt2:.2f} seconds the object is at ({x:.3f}, {y:.3f}, {z:.3f})")
print("")

tt3 = tt2 + tt1
x = ((x2-x1)/(t2-t1))*(tt3-t1) +x1
y=((y2-y1)/(t2-t1))*(tt3-t1)+y1
z=((z2-z1)/(t2-t1))*(tt3-t1)+z1
print(f"At time {tt3:.2f} seconds the object is at ({x:.3f}, {y:.3f}, {z:.3f})")
print("")

tt4 = tt3 + tt1 
x = ((x2-x1)/(t2-t1))*(tt4-t1) +x1
y=((y2-y1)/(t2-t1))*(tt4-t1)+y1
z=((z2-z1)/(t2-t1))*(tt4-t1)+z1
print(f"At time {tt4:.2f} seconds the object is at ({x:.3f}, {y:.3f}, {z:.3f})")
print("")

tt5 = tt4 + tt1
x = ((x2-x1)/(t2-t1))*(tt5-t1) +x1
y=((y2-y1)/(t2-t1))*(tt5-t1)+y1
z=((z2-z1)/(t2-t1))*(tt5-t1)+z1
print(f"At time {tt5:.2f} seconds the object is at ({x:.3f}, {y:.3f}, {z:.3f})")
print("")

    



