MODULES AND PACKAGES:

ADD.PY PYTHON FILE:

class addition(object):
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def add(self):
        print("The addition value is:",self.a+self.b)

SUB.PY PYTHON FILE:

class subtract(object):
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def sub(self):
        print("The subtraction value is:",self.a-self.b)

MUL.PY PYTHON FILE:

class multiplication(object):
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def mul(self):
        return "The multiplication value is:",self.a*self.b

BASE.PY PYTHON FILE:

from add import addition
from sub import subtract
from mul import multiplication

obj=addition(5,4)
obj_two=subtract(8,2)
obj_three=multiplication(2,9)
obj.add()
obj_two.sub()
print(obj_three.mul())

(NOTE: CREATE __INIT__.PY PYTHON FILE TO CONVERT IT INTO PACKAGES)
