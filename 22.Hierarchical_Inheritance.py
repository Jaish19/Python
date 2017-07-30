HIERARCHICAL INHERITANCE:

class dad(object):
    def __init__(self):
        pass
    def character(self):
        print("Its dad character")
    def behaviour(self):
        print("its dad behaviour")
class child_one(dad):
    def __init__(self):
        pass
    def character(self):
        print("Since I'm a child one...I've my own character")
class child_two(dad):
    def __init__(self):
        print("I have nothing with me")
        pass
a=child_two()
a.character()
a.behaviour()
b=child_one()
b.behaviour()
    
