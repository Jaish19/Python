Example 1:
     
def glob():
     print(a)

a="I'm global"
glob()

Example 2:

def glob():
     global a
     print(a)
     a="I'm Local"
     print(a)

a="I'm global"
glob()
print(a)

Example 3:

def glob():
     a="I'm Local"
     print(a)


glob()
print(a)

Example 4:

def func(x,y):
     global a
     a=12
     b=15
     c=19
     print a,x,y,b

func(7,17)
