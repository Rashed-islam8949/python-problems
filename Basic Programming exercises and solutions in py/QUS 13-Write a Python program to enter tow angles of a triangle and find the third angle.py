# QUS-13:Write a Python program to enter tow angles of a triangle and find the third angle.

x=int(input("Enter first angle: "))
y=int(input("Enter second nangle: "))
if (x+y)<180:
    z= 180-(x+y)
    print(f"Third angle = {z}")
else:
    print("Plz Enter valid Angel degrees. In a triangle, the sum of the 1st and 2nd angles must be less than 180 degrees.")