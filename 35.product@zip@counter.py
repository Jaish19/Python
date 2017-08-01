PRODUCT @ COUNTER @ ZIP:

EXAMPLE 1:

from itertools import product
l1=[1,2,3,4,5]
l2=[7,8,9,0,3]
a=product(l1,l2)
for i in a:
    print(i)


EXAMPLE 2:

from itertools import product
a={'a':1,'b':2}
b={'c':3,'d':4}
print(list(product(a.keys(),b.keys())))

EXAMPLE 3:

from itertools import product
l1=[1,2,3,4,5]
l2=[7,8,9,0,3]
print(list(product(l1,l2)))
print(tuple(product(l2,l2))
print(dict(product(l1,l2)))

EXAMPLE 4:

from collections import Counter
a='hi friends welcome back welcome back'
b='FKDJSIFDKSDKSDKSD'
c=[1,4,7,8,5,5,5,5,8,8,8,7,1,2,3,4]
print(Counter(a.split()))
print(Counter(b))
print(Counter(c))


