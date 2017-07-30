example 1:

l1=[1,2,3,4,5]
for i in l1:
    print(l1.index(i),'is',i)

example 2:

code=range(10)
print(code)
print(type(code))

example 3:

for i in range(0,50,5):
    print(i)

example 4:

l1=range(10)
for i in l1[::-1]:
#     print('9'*9)---this operation gonna happen below
    print(str(i)*i)

example 5:

for i in range(10):
     print("Value is",i,"Squared value is:",i**2)

example 6:

for i in raw_input("Enter the string:"):
     if i in ['a','j','u']:
          print("Its available in our string")
     else:
          print("Its not...")
