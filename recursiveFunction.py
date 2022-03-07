#!/usr/bin/python

def getFactorialOfNumber(number):
  """This is a recursive function to find the factorial value of a number"""

  if number == 1:
    return 1
  else:
    return (number * getFactorialOfNumber(number - 1))

num = int(input('Enter a number: '))

result = getFactorialOfNumber(num)

print("The factorial of", num, "is", result)