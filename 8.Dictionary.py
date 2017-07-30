Python 2.7.13 (v2.7.13:a06454b1afa1, Dec 17 2016, 20:42:59) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> d1={'a':100,'b':200}
>>> d1['c']=300
>>> d1
{'a': 100, 'c': 300, 'b': 200}
>>> d1.update({'d':400})
>>> d1
{'a': 100, 'c': 300, 'b': 200, 'd': 400}
>>> d1.keys()
['a', 'c', 'b', 'd']
>>> d1.values()
[100, 300, 200, 400]
>>> var=d1.values()
>>> var
[100, 300, 200, 400]
>>> type(var)
<type 'list'>
>>> d2={}
>>> del d2
>>> d2

Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    d2
NameError: name 'd2' is not defined
>>> d2={'a':1,'b':20}
>>> d2.clear()
>>> d2
{}
>>> d3=d1.copy()
>>> d3
{'a': 100, 'c': 300, 'b': 200, 'd': 400}
>>> d4=d3
>>> d4
{'a': 100, 'c': 300, 'b': 200, 'd': 400}
>>> d3.pop('c')
300
>>> d3
{'a': 100, 'b': 200, 'd': 400}
>>> for i in d1:
	print(i)

	
a
c
b
d
>>> for i in d1.items():
	print(i)

	
('a', 100)
('c', 300)
('b', 200)
('d', 400)
>>> for keys,values in d1.items():
	print(keys,values/2)

	
('a', 50)
('c', 150)
('b', 100)
('d', 200)
>>> 
