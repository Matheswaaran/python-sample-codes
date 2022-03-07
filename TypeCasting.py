#!/usr/bin/python

num_int = 123
num_flo = 1.23
num_str = "456"

print("datatype of num_int:",type(num_int))
print("datatype of num_flo:",type(num_flo))
print("datatype of num_str:",type(num_str))

num_new = num_int + num_flo

print("Value of num_new:",num_new)
print("datatype of num_new:",type(num_new))

# num_new_2 = num_int + num_str # This produces TypeError, as string and int cannot be added or concatinated.

num_new_2 = num_int + int(num_str)

print("Value of num_new_2:",num_new_2)
print("datatype of num_new_2:",type(num_new_2))