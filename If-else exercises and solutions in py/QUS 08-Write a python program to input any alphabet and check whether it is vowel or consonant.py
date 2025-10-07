# Write a python program to input any alphabet and check whether it is vowel or consonant.

char = input("Enter a character: ")

if char.lower() in 'aeiou':
  print(f"{char} is a vowel")
else:
  print(f"{char} is a consonant")

# OR 

ch= input("Enter a character: ")
if(ch=='A'or ch=='a' or ch=='E'or ch =='e' or ch=='I'or ch=='i' or ch=='O'or ch=='o' or ch=='U'or ch=='u'):
    print(ch, "is a Vowel")
else:
    print(ch, "is a Consonant")

# OR

ch=input("Enter an alphabet:")
if len(ch) == 1 and ch.isalpha():
  if ch in 'aeiouAEIOU':
    print(f"{ch} is vowel")
  else:
    print(f"{ch} is consonant")
else:
  print("Invalid input. Please enter a single alphabet.")