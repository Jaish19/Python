SORTING METHODS:

EXAMPLE 1:

code=[1,2,5,8,9,4,55,11]
code_tuple=(1,8,9,6,3,4)
code_set={1,1,2,5,5,9,55,44,3}
print(sorted(code))
print(sorted(code_tuple))
print(sorted(code_set))

EXAMPLE 2:

import operator
code=([1,2],[5,4],[9,2],[8,1])
print(sorted(code,key=operator.itemgetter(0),reverse=False))

EXAMPLE 3:

import operator
code={'a':22,'b':11,'c':55}
print(sorted(code.items(),key=operator.itemgetter(1),reverse=True))

EXAMPLE 4:

import operator
code={'a':22,'b':11,'c':55}
print(sorted(code.keys(),key=operator.itemgetter(1),reverse=True))



