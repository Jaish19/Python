EXAMPLE 1:

def gen(num):
    i=0
    while i<num:
        yield i
        i+=1
    
y=gen(5)
print(y.next())
print(y.next())
print(y.next())
print(y.next())
print(y.next())

EXAMPLE 2:

def gen():
    yield 'hi'
    yield 'welcome'

y=gen()
print(y.next())
print(y.next())

    
EXAMPLE 3:

def gen(num):
    i=0
    while i<num:
        yield i
        i+=1
    
for i in gen(5):
    print(i)

EXAMPLE 4:

def gen(num):
    print('Start')
    for i in range(num):
        print("before yield:",i)
        yield i
        
for i in gen(5):
    print("After yield:",i)
