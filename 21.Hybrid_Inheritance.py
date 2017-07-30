HYBRID INHERITANCE:

class grand_father(object):
    def __init__(self):
        pass
    def behaviour(self):
        print("I'm grand father...Its my behaviour")
    def character(self):
        print("I'm your grand father...its my behaviour")
class dad(grand_father):
    def __init__(self):
        pass
    def character(self):
        print("I'm your dad...I have some character")
class son(dad):
    def __init__(self):
        pass
    def character(self):
        print("I'm son...I have my own character")
class daughter(dad):
    def __init__(self):
        print("Since,I'm small...I don't have anything...")
        pass
a=daughter()
a.character()
a.behaviour()
b=son()
    
    
