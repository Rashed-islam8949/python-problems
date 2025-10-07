# Write a python progam to find maximum between three numbers.

num1=int(input("Input num1: "))
num2=int(input("Input num2: "))
num3=int(input("Input num3: "))
if num1>num2 and num1>num3:
  print(f"Maximum = {num1}")
elif num2>num3:
  print(f"Maximum = {num2}")
else:
  print(f"Maximum = {num3}")