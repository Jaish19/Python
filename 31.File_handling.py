EXAMPLE 1:
     
with open('stuart.txt','r') as file:
    data=file.read()
filechange=data.replace('discussing','talking')
print(filechange.count('talking'))

with open('stuart.txt','w') as file:
    file.write(filechange)

EXAMPLE 2:

with open('stuart.txt','r') as file:
    print("file name is:",file.name)
    print("file mode is:",file.mode)
    print("file status:",file.closed)

EXAMPLE 3:

with open('stuart.txt','w') as file:
    file.write('hi everyone...\n')
    lines=['welcome back to new tutorial']
    file.writelines(lines)
    
    
    
