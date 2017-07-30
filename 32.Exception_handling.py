EXCEPTION HANDLING:

EXAMPLE 1:

def exceptionHandling(num):
    try:
        if num>0:
            print(abs(num/0))
    except ZeroDivisionError as code:
        print(code.message)
        
    finally:
        print("Inside main")
        
exceptionHandling(5)

EXAMPLE 2:

try:
    code=int(raw_input("Enter the integer value:"))
    if code==type(str):
        raise ValueError
    else:
        print("Hey...thanks for entering the valid input")
except ValueError as e:
    print(e.message)
finally:
    print("Inside finally...")

EXAMPLE 3:

class Error(Exception):
    def __init__(self,num):
        self.num=num
        pass

def func(x,y):
    try:
        if x==y:
            print("Both values are same")
        else:
            raise Error("err...")
    except Error:
        print("Values are not equal....")
        
func(5,8)

EXAMPLE 4:

class Error(Exception):
    def __init__(self,num):
        self.num=num
        pass

def func(x,y):
    try:
        if x<0:
            raise Error("err...")
        else:
            print("Its positive value....")
        
    except Error:
        print("Its negative values...")
        
func(5,8)
