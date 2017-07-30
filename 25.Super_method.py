SUPER METHOD:

EXAMPLE 1:

class A(object):
    def __init__(self,a,b):
        self.a=a
        self.b=b
        pass
    def add(self):
        print("add is:",self.a+self.b)
class B(A):
    def __init__(self,x,y):
        self.x=x
        self.y=y
        super(B,self).__init__(x,y)
    def mul(self):
        print("multiply is:",self.a*self.b)
        
cc=B(2,5)
cc.add()
cc.mul()

EXAMPLE 2:

class bank(object):
    def __init__(self):
        pass
    def status(self):
        print("Status verified")
class user(bank):
    def __init__(self):
        pass
    def help(self):
        print("help me...I wanna know the status")
        super(user,self).status()

cc=user()
cc.help()
