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
import datetime
# from datetime import timezone, timedelta, date

def timestamp(time):
    dmh = time[-1]
    period = time.replace(dmh, '')
    try:
        if dmh == 'd' or dmh == 'm' or dmh == 'h':
            days = 0
            minutes = 0
            hours = 0
            if dmh == 'd':
                days = int(period)
            elif dmh == 'h':
                hours = int(period)
            return datetime.datetime.now() + datetime.timedelta(days, 0, 0, 0, minutes, hours, 0)
        else:
            return 'error'
    except:
        return 'error'

epoch = datetime.datetime.utcfromtimestamp(0)

def test(dt):
    return (dt - datetime.datetime.now()).total_seconds() * 1000.0

# date = timestamp('7d') - datetime.datetime.now()
print(test(timestamp('7h')))