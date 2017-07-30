while loop statement example:

code=5
while code<20:
     print("Values are:",code)
     jai+=1

example 2:
     
found=True
while found:
     print("Its True condition...")
     found=False
     print("Its turned to false...")

Break example:

code=5
while code<10:
     if code==5:
          break
     print("The values are:",code)

print("Operation ends...")

Continue statement:

l1=[3,5]
for i in range(10):
     if i in l1:
          continue

     print("Values are:",i)
