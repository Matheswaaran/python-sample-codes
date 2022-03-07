#!/usr/bin/python

try:
  numerator = int(input('Numerator: '))
  denominator = int(input('Denominator: '))

  result = numerator / denominator
  print(result)

except ZeroDivisionError:
  print("Denominator cannot be 0. Please try again")
except ValueError:
  print("Value cannot be 0. Please try again")
finally:
  print("Finally Block")

print("\n================================\n")
