Example 1:

def decorator(name):
    def func():
        return "Hi Mr."
    result = func() + name
    return result

print(decorator("Jaish"))

EXAMLE 2:

def decorator(name):
    return "hi Mr."  + name

greet=decorator
print(greet("Jaish"))

EXAMPLE 3:

def decorator(func):
    print("going to...")
    return func

@decorator
def norm():
    print("Its kinda decorator operation")
    
norm()

EXAMPLE 4:

def decorator(func):
    def wrap(name):
        return func(name)
    return wrap

@decorator
def norm(name):
    print("Its kinda decorator operation Mr.",name)
    
norm("Alex")
