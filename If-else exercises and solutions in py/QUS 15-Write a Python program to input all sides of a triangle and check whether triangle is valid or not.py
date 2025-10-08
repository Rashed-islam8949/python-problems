# Write a Python program to input all sides of a triangle and check whether triangle is valid or not.

s1=int(input("Input side 1: "))
s2=int(input("Input side 2: "))
s3=int(input("Input side 3: "))
if s1+s2>s3 and s1+s3>s2 and s2+s3>s1:
  print("Triangle is valid")
else:
  print("Triangle is not valid")
