CONSTRUCTOR:

class calculator():
    def __init__(self,a,b):
        print("I'm a constructor dude")
        self.one=a
        self.two=b
        pass
    def add(self):
        print("I'm a addition operator:",self.one+self.two)
        
a=calculator(5,8)
a.add()


CONSTRUCTOR EXAMPLE 2:

class master():
     def __init__(self):
          print("I'm a Constructor")
          pass
     def student(self):
          print("I'm a Student")

a=master()
a.student()
