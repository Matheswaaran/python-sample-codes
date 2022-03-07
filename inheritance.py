#!/usr/bin/python

class Animal:
  def eat(self):
    print("I can eat")
  def walk(self):
    print("I can walk")

class Dog(Animal):
  def bark(self):
    print("I can bark")

class Cat(Animal):
  def grumpy(self):
    print("I am grumpy")
    
  def eat(self):
    print("I can also eat")

dog1 = Dog()
cat1 = Cat()

dog1.bark()
dog1.eat()
dog1.walk()

cat1.eat()
cat1.grumpy()
dog1.walk()