#!/usr/bin/python
from Employee import Employee

def main():

  name      = raw_input("What's your name? ")
  age       = raw_input("What's your age? ")
  position  = raw_input("What is your position? ")

  e = Employee()
  e.create(name,age,position)

if __name__ == "__main__":
  main()