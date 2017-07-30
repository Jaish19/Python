MULTILEVEL INHERITANCE:

class dad(object):
    def __init__(self):
        pass
    def behaviour(self):
        print("Its your dad behaviour")
    def character(self):
        print("Its your dad character")
class son_one(dad):
    def __init__(self):
        pass
    def behaviour(self):
        print("I'm a son_one,I have my own behaviour")
class son_two(son_one):
    def __init__(self):
        pass
    
c=son_two()
c.behaviour()
c.character()
    


        
