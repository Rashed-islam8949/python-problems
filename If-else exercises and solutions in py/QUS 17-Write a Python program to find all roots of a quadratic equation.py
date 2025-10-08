# Write a Python program to find all roots of a quadratic equation.

import cmath

a = float(input("Input a: "))
b = float(input("Input b: "))
c = float(input("Input c: "))

delta = (b**2) - (4*a*c)

if delta >= 0:
  x1 = (-b - delta**0.5) / (2*a)
  x2 = (-b + delta**0.5) / (2*a)
  print(f"Root1: {x1:.2f}")
  print(f"Root2: {x2:.2f}")
else:
  x1 = (-b - cmath.sqrt(delta)) / (2*a)
  x2 = (-b + cmath.sqrt(delta)) / (2*a)
  print(f"Root1: {x1:.2f}")
  print(f"Root2: {x2:.2f}")