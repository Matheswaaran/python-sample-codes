#!/usr/bin/python

# def getDouble(number):
#   return number * 2

getDouble = lambda number:number * 2

getSum = lambda number1, number2:number1 + number2

double_result = getDouble(10)

print(double_result)

sum_result = getSum(10, 30)

print(sum_result)

names = ["Alan", "Jeffery", "Jerome", "Ron", "AB", "Christopher"]
names.sort()
print(names)
names.sort(key = lambda x:len(x))
print(names)