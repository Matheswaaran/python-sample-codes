#!/usr/bin/python

# languages = ["English", "Tamil", "Hindi", "Sanskrit"]

# for language in languages:
#   print(language)

# for count in range(1, 6):
#   print(count)

number = int(input("Enter a number: "))

for count in range(1, 11):
  product = count * number;
  print("{} * {} = {}".format(number, count, product))