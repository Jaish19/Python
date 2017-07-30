SINGLE INHERITANCE:

class dad(object):
    def __init__(self):
        pass
    def behaviour(self):
        print("I'm your dad...Its my behaviour")

class child(dad):
    def __init__(self):
        pass
#     def behaviour(self):
#         print("heeee...I'm a kid....")
    
a=child()
a.behaviour()
