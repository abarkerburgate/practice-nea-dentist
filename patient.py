class Patient():
  def __init__(self, firstName="", lastName="", dob="", gender="", address="", phone="", email=""):
    self.firstName = firstName
    self.lastName = lastName
    self.dob = dob
    self.gender = gender
    self.address = address
    self.phone = phone
    self.email = email
    self.appointments = []
    self.messages = []
    self.patientId = 0

  def getFirstName(self):
    return self.firstName
    
  def getLastName(self):
    return self.lastName
    
  def getDob(self):
    return self.dob
    
  def getGender(self):
    return self.gender
    
  def getAddress(self):
    return self.address
    
  def getPhone(self):
    return self.phone
    
  def getEmail(self):
    return self.email
  