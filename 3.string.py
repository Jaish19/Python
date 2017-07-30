Python 2.7.13 (v2.7.13:a06454b1afa1, Dec 17 2016, 20:42:59) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> x="jaish gamb"
>>> type(x)
<type 'str'>
>>> x='jaish gamb'
>>> type(x)
<type 'str'>
>>> x='I don't wanna play this game'
SyntaxError: invalid syntax
>>> x="I don't wanna play this game"
>>> x
"I don't wanna play this game"
>>> print(x)
I don't wanna play this game
>>> y='he asking me "wru?"'
>>> y
'he asking me "wru?"'
>>> x='I don\'t wanna play this game'
>>> x
"I don't wanna play this game"
>>> print('c:\desktop\nextvideo')
c:\desktop
extvideo
>>> print(r'c:\desktop\nextvideo')
c:\desktop\nextvideo
>>> first='jai'
>>> second='ganesh'
>>> first+second
'jaiganesh'
>>> first*5
'jaijaijaijaijai'
>>> first*2
'jaijai'
>>> first**2

Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    first**2
TypeError: unsupported operand type(s) for ** or pow(): 'str' and 'int'
>>> num=55
>>> first='jaish'
>>> first+num

Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    first+num
TypeError: cannot concatenate 'str' and 'int' objects
>>> first+str(num)
'jaish55'
>>> num='55'
>>> first+num
'jaish55'
>>> num=55
>>> first+'num'
'jaishnum'
>>> 
