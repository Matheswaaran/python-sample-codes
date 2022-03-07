#!/usr/bin/python

# def printGreetings(name):
#   print("Hello", name)

# name = input("Enter your name: ")

# printGreetings(name)

# Adding two numbers

# def addNumbers(num1, num2):
#   result = num1 + num2
#   return result

# number1 = 4.5
# number2 = 5.6

# result = addNumbers(number1, number2)

# print (result);

#  Add marks


def findAverageMarks(marks):
  length = len(marks)
  total = sum(marks)  
  print ("Total of {} marks is {}".format(length, total))
  average = total / length
  return average

def getGradeFromAverageMarks(average):
  if average >= 80:
    grade = "A"
  elif average >= 60:
    grade = "B"
  elif average >= 50:
    grade = "C"
  else:
    grade = "F"
  return grade

marks = [95, 95, 98, 89, 100]

average = findAverageMarks(marks);

grade = getGradeFromAverageMarks(average);

print ("Average Mark is {} and the grade is {}".format(average, grade))