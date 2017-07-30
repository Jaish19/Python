Python 2.7.13 (v2.7.13:a06454b1afa1, Dec 17 2016, 20:42:59) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> tup=(1,2,3,4,5)
>>> tup.append(5)

Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    tup.append(5)
AttributeError: 'tuple' object has no attribute 'append'
>>> len(tup)
5
>>> tup_one=(5,8,7,9,5)
>>> tup+tup_one
(1, 2, 3, 4, 5, 5, 8, 7, 9, 5)
>>> 4 in tup
True
>>> 9 in tup_one
True
>>> max(tup_one)
9
>>> min(tup)
1
>>> tup_one.count(5)
2
>>> tup.index(5)
4
>>> tup_one.index(9)
3
>>> tup_three=tup
>>> tup_three
(1, 2, 3, 4, 5)
>>> del tup
>>> tup

Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    tup
NameError: name 'tup' is not defined
>>> 
