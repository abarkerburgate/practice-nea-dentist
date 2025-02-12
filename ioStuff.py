# import only system from os
from os import system, name

# import sleep to show output for some time period
from time import sleep

def clearScreen():
  # for windows
  if name == 'nt':
      _ = system('cls')
  # for mac and linux(here, os.name is 'posix')
  else:
      _ = system('clear')
    
def getNumber(prompt, minVal, maxVal):
  while True:
    try:
      val = int(input(prompt))
      if val < minVal:
        raise Exception
      if val > maxVal:
        raise Exception
      return val
    except:
      print("Invalid choice")

def getString(prompt, minLen=0, maxLen=0):
  while True:
    try:
      val = input(prompt)
      if val == "":
        raise Exception
      if len(val) < minLen:
        print("Too short")
        raise Exception
      if len(val) > maxLen:
        print("Too long")
        raise Exception
      return val
    except:
      print("Invalid entry")

def getDate(prompt, minLen=0, maxLen=0):
  while True:
    try:
      val = input(prompt)
      if val == "":
        raise Exception
      if len(val) < minLen:
        print("Too short")
        raise Exception
      if len(val) > maxLen:
        print("Too long")
        raise Exception
      return val
    except:
      print("Invalid entry")

def getYesNo(prompt):
  while True:
    try:
      val = input(prompt)
      val = val.lower()
      if val != "y" and val != "n":
        raise Exception
      return val
    except:
      print("Invalid response")

def getGender(prompt):
  while True:
    try:
      val = input(prompt)
      val = val.lower()
      if val != "m" and val != "f":
        raise Exception
      return val
    except:
      print("Invalid response")

def getPhoneNumber(prompt):
  #use regular expression to check for valid phone number
  while True:
    try:
      val = input(prompt)
      if val == "":
        raise Exception
      if len(val) < 1:
        print("Too short")
        raise Exception
      if len(val) > 11:
        print("Too long")
        raise Exception
      return val
    except:
      print("Invalid entry")

def getEmail(prompt):
  #use regular expression to check for valid email
  while True:
    try:
      val = input(prompt)
      if val == "":
        raise Exception
      if len(val) < 1:
        print("Too short")
        raise Exception
      if len(val) > 11:
        print("Too long")
        raise Exception
      return val
    except:
      print("Invalid entry")
