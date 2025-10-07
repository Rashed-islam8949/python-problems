# Write a python program to check whether a character is uppercase or lowercase alphabet.

cha=input("Input character: ")
if cha.isupper():
  print(f"{cha} is uppercase")
elif cha.islower():
  print(f"{cha} is lowercase")
else:
  print(f"{cha} is not alphabet")