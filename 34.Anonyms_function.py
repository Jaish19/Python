ANONYMS FUNCTION:

EXAMPLE 1:

def square(num):
    return num**2
def add(num):
    return num+5

l1=[1,2,3,4,5]
print("The square of list is:",map(square,l1))

print("The Addition of list is:",map(add,l1))

EXAMPLE 2:

print(map(lambda x,y:x+y,[1,2,3],[4,5,6]))

print(filter(lambda x:x%2==0,[1,2,3,4,5]))

print(filter(lambda x:x<0,[-1,-2,1,2,5,8]))

print(reduce(lambda x,y:x*y,[1,2,3,4,5]))
