MULTIPLE INHERITANCE:

class dad(object):
    def __init__(self):
        pass
    def permission(self):
        print("I'm your dad...permission granted")
class mom(object):
    def __init__(self):
        pass
class child(mom,dad):
    def __init__(self):
        pass
c=child()
c.permission()
print(child.__mro__)
