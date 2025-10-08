# Write a Python program to check whether the triangle is equilateral, isosceles or scalene triangle.

s1=int(input("Input side 1: "))
s2=int(input("Input side 2: "))
s3=int(input("Input side 3: "))
if s1+s2>s3 and s1+s3>s2 and s2+s3>s1:
  if s1==s2==s3:
    print("Equilateral triangle")
  elif s1==s2 or s1==s3 or s2==s3:
    print("Isosceles triangle")
  else:
    print("Scalene triangle")
else:
  print("Triangle is not valid")