# QUS-7:Write a Python program to enter length in centimeter and convert it into meter and kilometer.

C=int(input("Enter length in centimeter = "))
M= C//100
KM= C/100000
print(f"Length in meter = {M} m")
print(f"Length in kilometer = {KM} km")