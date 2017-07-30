Example 1:
     
name='jaish'
if name==raw_input("Enter the name:"):
    print("Its you...")
else:
    print("Sorry...")

example 2:

value=50
if value>90:
    print("Its greater than 90")
# elif value<50:
#     print("its less than 50")
elif value == 40:
    print("Its 40...")
else:
    print("Not in a condition...")

example 3:

value=5
if type(value)==str:
    print("Its string")
else:
    print("It's not a string...")

example 4:

value=98

if value>90 and value < 100:
    print("Between 90 to 100")
elif value==50 or value == 40:
    print("Its either 40 or 50")
else:
    print("Not in a condition...")

