args and kwargs:

EXAMPLE 1:

def sum(*args):
    s=0
    for i in args:
        s+=i
    print("The value of sum is:",s)

sum(1,22,3)

EXAMPLE 2:

def sum(a,b,c):
    print("Parameter values are:",a,b,c)
    
c=[1,2,3]
sum(*c)

EXAMPLE 3:

def my_mtd(**kwargs):
    for i in kwargs.items():
        print(i)

my_mtd(name='Jaish',sport='Cricket',roll=19)


EXAMPLE 4:

def my_mtd(arg1,arg2,arg3):
    print("arg one",arg1)
    print("arg two",arg2)
    print("arg three",arg3)

save={'arg2':2,'arg3':3}
my_mtd(1,**save)

EXAMPLE 5:

def my_mtd(arg1,arg2,arg3):
    print("arg one",arg1)
    print("arg two",arg2)
    print("arg three",arg3)

save=('two',3)
my_mtd(1,*save)
