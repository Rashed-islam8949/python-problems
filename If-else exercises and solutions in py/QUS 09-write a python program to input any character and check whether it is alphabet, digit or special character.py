# write a python program to input any character and check whether it is alphabet, digit or special character.

cha=input("Input character: ")
if cha.isalpha():
  print(f"{cha} is alphabet")
elif cha.isdigit():
  print(f"{cha} is digit")
else:
  print(f"{cha} is special character")