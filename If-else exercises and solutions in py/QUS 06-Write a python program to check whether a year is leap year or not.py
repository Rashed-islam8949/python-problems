# Write a python program to check whether a year is leap year or not.

year=int(input("Input year: "))
if year%4==0 and year%100!=0:
  print(f"{year} is leap year")
elif year%400==0:
  print(f"{year} is leap year")
else:
  print(f"{year} is not leap year")