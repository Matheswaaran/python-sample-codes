#!/usr/bin/python

class SalaryNotInRangeError(Exception):
  """Exception raised for errors when salary is not in the specified range."""

  def __init__(self, salary, message="Salaray is not in 5000-15000 range."):
    self.salary = salary
    self.message = message
    super().__init__(self.message)

  def __str__(self):
    return f'{self.salary} -> {self.message}'


salary = int(input("Enter a Salaray: "))

if not 5000 < salary < 15000:
  raise SalaryNotInRangeError(salary)