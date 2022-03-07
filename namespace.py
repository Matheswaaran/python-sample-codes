#!/usr/bin/python

a = 5

print('id(2) =', id(2))
print('id(5) =', id(5))
print('id(5) =', id(3))
print('id(a) =', id(a))
a -= 3
print('id(a-3) =', id(a))


# Scope of a variable

def outer_function():
  a = 20

  def inner_function():
    a = 30
    print('a =', a)

  inner_function()
  print('a =', a)


a = 10
outer_function()
print('a =', a)

# Global scope

def outer_function():
  global a
  a = 20

  def inner_function():
    global a
    a = 30
    print('a =', a)

  inner_function()
  print('a =', a)


a = 10
outer_function()
print('a =', a)