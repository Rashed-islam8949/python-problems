# Write a python program to input month number and print number of days in that month.

month_num=int(input("Input month number (1-12) : "))
if month_num==1:
  print("31 days")
elif month_num==2:
  print("28/29 days")
elif month_num==3:
  print("31 days")
elif month_num==4:
  print("30 days")
elif month_num==5:
  print("31 days")
elif month_num==6:
  print("30 days")
elif month_num==7:
  print("31 days")
elif month_num==8:
  print("31 days")
elif month_num==9:
  print("30 days")
elif month_num==10:
  print("31 days")
elif month_num==11:
  print("30 days")
elif month_num==12:
  print("31 days")
else:
  print("Invalid month number")