########################################################
# Rodrigo Leite - drigols                              #
# Last update: 07/11/2021                              #
########################################################

class Person:
  
  def __init__(self, name):
    self.name = name
    
  def say_name(self):
    print('Hello, my name is:', self.name)
    
if __name__ == "__main__":
  p = Person('Rodrigo')
  p.say_name()
