# QUS-10:Write a Python program to convert  days into years,week and days.

D=int(input("Enter days: "))
Y=D//365
W=(D-Y*365)//7
Day= (D-((Y*365)+(W*7)))
print(f"{D} days = {Y} years/s, {W} week/s and {Day} day/s")