POLYMORPHISM: METHOD OVER-RIDING

EXAMPLE 1:
     
class set_one(object):
    def __init__(self):
        pass
    def mtd_one(self):
        print("set_one--mtd one")
    def mtd_two(self):
        print("set_one--mtd two")
class set_two(set_one):
    def __init__(self):
        pass
    def mtd_one(self):
        print("set_two--mtd one")
    def mtd_two(self):
        print("set_two--mtd two")
a=set_two()
a.mtd_one()

EXAMPLE 2:

class calculator(object):
    def __init__(self,a,b):
        self.a=a
        self.b=b
        pass
    def add(self):
        print("Calculator add is:",self.a+self.b)
    
class maths(calculator):
    def __init__(self,a,b):
        self.a=a
        self.b=b
        pass
    def add(self):
        print("Maths add is:",self.a+self.b)
        
a=maths(5,5)
a.add()

        
