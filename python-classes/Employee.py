#!/usr/bin/python
import json

class Employee(object):
  def __init__(self):
    return

  def create(self, name, age, position):
    self.name     = name
    self.age      = age
    self.position = position

    employees = self.getEmployees()

    employeesLength = len(employees["Employees"])

    # Sometime around here we need to see if there are any employees or if this file is empty.
    # If it's empty, let's start the dictionary

    employees["Employees"].append({"name":self.name,"age":self.age,"position":self.position})

    employeesString = json.dumps(employees)

    #print employees["Employees"]
    with open('employees.json', 'w') as file_:
      file_.write(employeesString)

  def bio(self):
    print "My name is %s, I am %s years old and I am a %s" % (self.name, self.age, self.position)

  def getEmployees(self):
    with open('employees.json') as employees_file:
      return json.load(employees_file)

