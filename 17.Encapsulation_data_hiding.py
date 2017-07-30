ENCAPSULATION: DATA HIDING

class data_hiding():
    def __init__(self):
        self.a=1 # public
        self._a=2 # protected
        self.__a=3 # private
    def public_method(self):
        print("Hey..I'm public method",self.__a)
    def _protected_method(self):
        print("Hey..I'm protected",self._a)
    def __private_method(self):
        print("Oh dude...I'm private method")
        
obj=data_hiding()
obj.public_method()
obj._protected_method()
obj._data_hiding__private_method()
        
        
