#!/usr/bin/python

def printNumbers():
  """Function displays upto 4 numbers"""
  for i in range(1, 10):
    print ("Condition", i == 5)
    if i == 5:
      break
    print ("item:", i)

printNumbers()
print (printNumbers.__doc__)