Python 2.7.13 (v2.7.13:a06454b1afa1, Dec 17 2016, 20:42:59) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> jaish=[]
>>> jaish=[1,2,3,4,5]
>>> jaish[2]
3
>>> jaish[5]

Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    jaish[5]
IndexError: list index out of range
>>> jaish[4]
5
>>> len(jaish)
5
>>> elem=['jaish','steve','vashini']
>>> jaish+elem
[1, 2, 3, 4, 5, 'jaish', 'steve', 'vashini']
>>> jaish
[1, 2, 3, 4, 5]
>>> jaish*3
[1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
>>> for i in jaish:
	print(i)

	
1
2
3
4
5
>>> jaish.append(5)
>>> jaish.append([9,5,5])
>>> jaish
[1, 2, 3, 4, 5, 5, [9, 5, 5]]
>>> jaish.pop()
[9, 5, 5]
>>> jaish.extend([5,9,8,7,1,1,1,8,5])
>>> jaish
[1, 2, 3, 4, 5, 5, 5, 9, 8, 7, 1, 1, 1, 8, 5]
>>> jaish.pop()
5
>>> jaish.pop()
8
>>> jaish.count(1)
4
>>> jaish.count(5)
3
>>> jaish.remove(2)
>>> jaish.remove(8)
>>> 
