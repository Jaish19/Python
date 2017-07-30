ENCAPSULATION: DATA ABSTRACTION

class data_base():
    def __init__(self,first,last,email):
        self.firstName=first
        self.lastName=last
        self.email=email
        self.friends=[]
    def add_person(self,friend):
        self.friends.append(friend)
        friend.friends.append(self)
        
p1=data_base('A','B','aaa@gmail.com')
p2=data_base('C','D','bbb@gmail.com')
p1.add_person(p2)
print(p1.firstName)
print(list(p1.friends))
