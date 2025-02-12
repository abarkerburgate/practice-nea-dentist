from os import *
from ioStuff import *
from patient import * 

class Menu:
  def __init__(self):
    self.breadcrumb = ""
    self.pageName = ""
    self.minMenuVal = 0
    self.maxMenuVal = 0
    self.menuOptions = []

  def displayPage(self):
    clearScreen()
    print(self.pageName)
    print("---------------------------")
    for option in self.menuOptions:
      print(option)
    print("")

  #======================================

  def displayDashboard(self):
    self.pageName = "Dashboard"
    self.breadcrumb = ">"
    self.minMenuVal = 1
    self.maxMenuVal = 5
    self.menuOptions.clear()
    self.menuOptions.append("1. Appointments")
    self.menuOptions.append("2. Patients")
    self.menuOptions.append("3. Messages")
    self.menuOptions.append("4. Reports")
    self.menuOptions.append("5. Staff availabilty")
    self.displayPage()
    choice = getNumber(self.breadcrumb, self.minMenuVal, self.maxMenuVal)
    if choice == 1:
      self.appointments()
    elif choice == 2:
      self.patients()
      
  #======================================

  def appointments(self):
    self.pageName = "Display Appointments"
    self.breadcrumb = "Dashboard>"
    self.minMenuVal = 1
    self.maxMenuVal = 4
    self.menuOptions.clear()    
    self.menuOptions.append("1. New appointment")
    self.menuOptions.append("2. Display appointments (day view)")
    self.menuOptions.append("3. Display appointments (week view)")
    self.menuOptions.append("4. Back")  
    self.displayPage()
    choice = getNumber(self.breadcrumb, self.minMenuVal, self.maxMenuVal)
    if choice == 1:
      self.newAppointment()
    elif choice == 2:
      self.displayDayViewAppointments()
    elif choice == 3:
      self.displayWeekViewAppointments()
    elif choice == 4:
      self.displayDashboard()

  def newAppointment(self):
    self.pageName = "New Appointment"
    self.breadcrumb = "Dashboard / New Appointment>"
    self.minMenuVal = 1
    self.maxMenuVal = 2
    
  #======================================

  
  def patients(self):
    self.pageName = "Patients"
    self.breadcrumb = "Dashboard>"
    self.minMenuVal = 1
    self.maxMenuVal = 4
    self.menuOptions.clear()    
    self.menuOptions.append("1. New patient")
    self.menuOptions.append("2. Remove patient")
    self.menuOptions.append("3. Display patients")
    self.menuOptions.append("4. Back")  
    self.displayPage()
    choice = getNumber(self.breadcrumb, self.minMenuVal, self.maxMenuVal)
    if choice == 1:
      tmpNewPatient = Patient()
      self.newPatient(tmpNewPatient)
    elif choice == 2:
      self.removePatient
    elif choice == 3:
      self.displayPatients() 
    elif choice == 4:
      self.displayDashboard()

  
  def newPatient(self, tmpNewPatient):
            
    self.firstName = tmpNewPatient.getFirstName()
    self.lastName = tmpNewPatient.getLastName()
    self.dob = tmpNewPatient.getDob()
    self.address = tmpNewPatient.getAddress()
    self.phone = tmpNewPatient.getPhone()
    self.email = tmpNewPatient.getEmail()
    self.gender = tmpNewPatient.getGender()
    
    self.pageName = "New Patient"
    self.breadcrumb = "Dashboard / New Patient>"
    self.minMenuVal = 1
    self.maxMenuVal = 9

    self.menuOptions.clear()
    self.menuOptions.append("1. First name: " + self.firstName)
    self.menuOptions.append("2. Last name: " + self.lastName)
    self.menuOptions.append("3. Date of birth: " + self.dob)
    self.menuOptions.append("4. Gender: " + self.gender)
    self.menuOptions.append("5. Address: " + self.address)
    self.menuOptions.append("6. Phone number: " + self.phone)
    self.menuOptions.append("7. Email: " + self.email)
    self.menuOptions.append("8. Submit new patient to database")
    self.menuOptions.append("9. Back")
    self.displayPage()
    choice = getNumber(self.breadcrumb, self.minMenuVal, self.maxMenuVal)
    if choice == 1:
      choice = getString("First name: ", minLen=1, maxLen=20)
      self.firstName = choice
      tmpNewPatient.firstName = choice
      self.newPatient(tmpNewPatient)
      
    elif choice == 2:
      choice = getString("Last name: ", minLen=1, maxLen=20)
      self.lastName = choice
      tmpNewPatient.lastName = choice
      self.newPatient(tmpNewPatient)
  
    elif choice == 3:
      choice = getDate("Date of birth (dd/mm/yyyy): ", minLen=1, maxLen=10)
      self.dob = choice
      tmpNewPatient.dob= choice
      self.newPatient(tmpNewPatient)

    elif choice == 4:
      choice = getGender("Gender: (m/f)")
      self.gender = choice
      tmpNewPatient.gender= choice
      self.newPatient(tmpNewPatient)

    elif choice == 5:
      choice = getString("Address", 1, 50)
      self.address = choice
      tmpNewPatient.address = choice
      self.newPatient(tmpNewPatient)

    elif choice == 6:
      choice = getPhoneNumber("Phone number:")
      self.phone = choice
      tmpNewPatient.phone = choice
      self.newPatient(tmpNewPatient)

    elif choice == 7:
      choice = getEmail("eMail:")
      self.email = choice
      tmpNewPatient.email= choice
      self.newPatient(tmpNewPatient)

    elif choice == 9:
      self.displayDashboard()
#======================================

