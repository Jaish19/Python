CALL BY VALUE:

def calbyval(a):
    print("first:",a)
    a=25
    print("changed:",a)

a=1
calbyval(a)
print(a)

CALL BY REFERENCE:

def calbyref(a):
    print("first:",a)
    a[0]=1
    a[1]=55
    print("changed:",a)

a=[2,85]
calbyref(a)
print(a)
