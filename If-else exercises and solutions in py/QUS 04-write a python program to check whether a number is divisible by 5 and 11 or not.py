# write a python program to check whether a number is divisible by 5 and 11 or not.

num=int(input("Input number: "))
if num%5==0 and num%11==0:
  print("Number is divisible by 5 and 11")
else:
  print("Not divisible")