#!/usr/bin/python

number = float(input("Enter Number: "))
print(number, "type:", type(number))

print(number, "type", type(number), sep=",", end="!\n")

print("The value is {} and type is {}".format(number, type(number)))
print("The value is {0} and type is {1}".format(number, type(number)))
print("The type is {1} and value is {0}".format(number, type(number)))
print("The value is {value} and type is {type}".format(value=number, type=type(number)))