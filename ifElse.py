#!/usr/bin/python

# score = int(input("Enter your score: "))

# if score >= 50:
#   print("You haved Passed the exam 🥳")
# else:
#   print("You have Failed the exam 😔")

# if score > 100 or score < 0:
#   print("Please enter an valid score")
# elif score >= 50:
#   print("You haved Passed the exam 🥳")
# else:
#   print("You have Failed the exam 😔")

num = int(input("Enter number to check: "))

if num > 0:
  print("Its a positive number")
elif num < 0:
  print("It's a negative number")
else:
  print("It's zero")