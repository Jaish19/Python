list Comprehension:

example 1:
     
l1=[1,2,3,'a','b','c']

l2=[i for i in l1 if type(i)==str]
print(l2)

example 2:

l1=[i**2 for i in range(10)]
print(l1)

example 3:

l1=[i for i in l1 if i%2==1]
print(l1)

Tuple comprehension:

example 1:

t1=(1,2,3,4)
t2=(i for i in t1)
print(t2)
for i in t2:
     print(i)

Dictionary comprehension:

example 1:

dict={i:i**2 for i in range(10)}
print(dict)

example 2:

l1=[1,1,1,2,2,3,3,3,4,5,4,5,8,8]
dict={i:l1.count(i) for i in l1}
print(dict)
