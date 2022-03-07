#!/usr/bin/python

class Student:

  def __init__(self, name, marks):
    print("__init__")
    self.marks = marks
    self.name = name
  
  def checkPassOrFail(self):
    if self.marks >= 40:
      return True
    else:
      return False

      
student1 = Student("Harry", 85)

print(student1.name, student1.marks, student1.checkPassOrFail())

student2 = Student("Mat", 10)

print(student1.name, student1.marks, student1.checkPassOrFail())

# ====================================================================

class Complex:

  def __init__(self, real, imag):
    self.real = real
    self.imag = imag

  def add(self, number):
    real = self.real + number.real
    imag = self.imag + number.imag
    result = Complex(real, imag)
    return result


n1 = Complex(5, 8)
n2 = Complex(2, 3)

result = n1.add(n2)
print("{}+{}i".format(result.real, result.imag))

# ====================================================================

class Triangle:
  def __init__(self, a, b, c):
    self.a = a
    self.b = b
    self.c = c

  def getPerimeter(self):
    perimeter = self.a + self.b + self.c
    return perimeter


triangle1 = Triangle(1, 2, 3)

triangle1_perimeter = triangle1.getPerimeter()

print(triangle1_perimeter)