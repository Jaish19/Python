POLYMORPHISM: METHOD OVERLOADING

EXAMPLE 1:

class method_overloading(object):
    def __init__(self):
        pass
    def source(self):
        print("I'm the first source")
    def source(self):
        print("I'm the third source")
a=method_overloading()
a.source()


EXAMPLE 2:

class calculator(object):
    def __init__(self):
        pass
    def add(self,a,b):
        print("Addition of two is:",a+b)
    def add(self,a,b,c):
        print("Addition of three is:",a+b+c)

a=calculator()
a.add(5,5,5)
