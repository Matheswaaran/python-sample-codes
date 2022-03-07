#!/usr/bin/python

number = 6
decimal = 3.14
drink = "Yes"
food = None
true = True
false = False
unique_numbers = { 1, 2, 3, 4, 5, 6, 6 }
python_dic = { 1: "Hello", 2: "World" }

print (number, "is type of", type(number))
print (decimal, "is type of", type(decimal))
print (drink, "is type of", type(drink))
print (food, "is type of", type(food))
print (true, "is type of", type(true))
print (false, "is type of", type(false))
print (unique_numbers, "is type of", type(unique_numbers))
print (python_dic, "is type of", type(python_dic))

print ("Is", number+decimal*3, "type of float?", isinstance(number+decimal*3,float))
print ("Is", number+2j, "type of complex?", isinstance(number+2j,complex))