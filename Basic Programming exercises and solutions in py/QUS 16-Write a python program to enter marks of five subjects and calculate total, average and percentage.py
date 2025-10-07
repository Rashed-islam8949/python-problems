# QUS-16:Write a python program to enter marks of five subjects and calculate total, average and percentage.

marks= list(map(int, input("Enter marks of five subjects:").split()))
total= sum(marks)
average = total/5
percentage = (total/500)*100
print(f"Total = {total} ")
print(f"Average = {average:.0f}")
print(f"Percentage = {percentage:.2f}")
