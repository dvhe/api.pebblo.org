"""
# Basic class
class Person:
  # Instead of constructor
  def __init__(self, name, sexuality):
    self.name = name
    self.sexuality = sexuality

  # All methods require `self` parameter
  def proclaim(self):
    print(f"{self.name} is {self.sexuality}.")

Kyle = Person("Kyle", "the big gay")
Kyle.proclaim()

# > "Kyle is the big gay."
"""
import time
import string
class OTP:
    def __init__(self, code, expired, backup, time):
        self.code = code
        self.time = time.time()
        self.backup = backup
        self.expired = False

    
    def generate(self):
      self.code = string.ascii_lowercase
      print(self.code)
      for i in range(5):
        self.backup = []
        self.backup.append(string.ascii_letters in range(5))
        print(self.backup)
      now = time.time()
      if self.time - now > 30:
        self.expired = True 
        print('Time has expired for code')

    def generate(self):



