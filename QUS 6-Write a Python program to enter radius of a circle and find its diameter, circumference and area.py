# QUS-6:Write a Python program to enter radius of a circle and find its diameter, circumference and area.
r=int(input("Enter radius: "))
dia= 2*r
cir= 2*r*(22/7)
area= int((22/7)*r**2)
print(f"Diameter = {dia} units")
print(f"Circumference = {cir:.2f} units")
print(f"Area = {area} sq. units")