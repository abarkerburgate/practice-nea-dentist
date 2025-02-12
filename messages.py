class Messages():
  def __init__(self, newMessage="", patientId=0):
    self.newMessage = newMessage
    self.patientID = patientId
    self.MessageId = 0

  def getNewMessage(self):
    return self.newMessage
    