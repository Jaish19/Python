Python 2.7.13 (v2.7.13:a06454b1afa1, Dec 17 2016, 20:42:59) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>>  l1=[1,1,1,2,3,6,5,5]
 
  File "<pyshell#0>", line 2
    l1=[1,1,1,2,3,6,5,5]
    ^
IndentationError: unexpected indent
>>> l1=[1,1,1,2,3,6,5,5]
>>> l1
[1, 1, 1, 2, 3, 6, 5, 5]
>>> set(l1)
set([1, 2, 3, 5, 6])
>>> s1=set()
>>> type(s1)
<type 'set'>
>>> code={1,2,3,4,5}
>>> code.add(9)
>>> code
set([1, 2, 3, 4, 5, 9])
>>> code.add(9)
>>> code
set([1, 2, 3, 4, 5, 9])
>>> s2={11,12,13}
>>> s2.clear()
>>> s2
set([])
>>> s2={11,12,13}
>>> s2.pop()
11
>>> s2
set([12, 13])
>>> s2.pop()
12
>>> s2
set([13])
>>> s2.add(12)
>>> s2.add(13)
>>> s3=set()
>>> type(s3)
<type 'set'>
>>> del s3
>>> s1={1,2,3,4,5}
>>> s2={5,6,7,8,9}
>>> s2.difference(s1)
set([8, 9, 6, 7])
>>> s2
set([8, 9, 5, 6, 7])
>>> s2.difference_update(s1)
>>> s2
set([8, 9, 6, 7])
>>> s2.discard(6)
>>> s2
set([8, 9, 7])
>>> s1
set([1, 2, 3, 4, 5])
>>> s2
set([8, 9, 7])
>>> s1.union(s2)
set([1, 2, 3, 4, 5, 7, 8, 9])
>>> s1
set([1, 2, 3, 4, 5])
>>> len(s1)
5
>>> 
