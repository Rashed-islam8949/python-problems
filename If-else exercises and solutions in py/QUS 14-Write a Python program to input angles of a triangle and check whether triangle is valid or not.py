# Write a Python program to input angles of a triangle and check whether triangle is valid or not.

a1=int(input("Input angle 1: "))
a2=int(input("Input angle 2: "))
a3=int(input("Input angle 3: "))
sum=a1+a2+a3
if sum==180:
  print("Triangle is valid")
else:
  print("Triangle is not valid")