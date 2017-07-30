Python 2.7.13 (v2.7.13:a06454b1afa1, Dec 17 2016, 20:42:59) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 
>>> 5**4
625
>>> 5**7
78125
>>> pow(5,5)
3125
>>> pow(8,3)
512
>>> x=5
>>> x
5
>>> x=-18
>>> abs(x)
18
>>> x
-18
>>> 58+abs(x)
76
>>> 58+x
40
>>> floor(18.55)

Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    floor(18.55)
NameError: name 'floor' is not defined
>>> import math
>>> math.floor(18.55)
18.0
>>> math.floor(-18.222)
-19.0
>>> math.sqrt(81)
9.0
>>> jaish=math.sqrt
>>> jaish(81)
9.0
>>> jaish(64)
8.0
>>> user='jaishgamb'
>>> user[0]
'j'
>>> user[9]

Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    user[9]
IndexError: string index out of range
>>> user[8]
'b'
>>> user[-1]
'b'
>>> user[-2]
'm'
>>> user[-8]
'a'
>>> user[1:5]
'aish'
>>> user[2:8]
'ishgam'
>>> user[0:]
'jaishgamb'
>>> user[2:]
'ishgamb'
>>> user[:]
'jaishgamb'
>>> user[-1:]
'b'
>>> user[-5:-2]
'hga'
>>> user[:-4]
'jaish'
>>> user[::-1]
'bmaghsiaj'
>>> var='nice'
>>> user[1:]+var
'aishgambnice'
>>> user[-1:]+var
'bnice'
>>> user[-2]+var
'mnice'
>>> user[:]+var
'jaishgambnice'
>>> user
'jaishgamb'
>>> print(len(user))
9
>>> 
