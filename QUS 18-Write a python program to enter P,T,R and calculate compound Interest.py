# QUS-18:Write a python program to enter P,T,R and calculate compound Interest.

P=int(input("Enter principle:"))
T=int(input("Enter time:"))
R=float(input("Enter rate:"))
CI=P*(1+R/100)**T
print(f"Simple Interest = {CI}")