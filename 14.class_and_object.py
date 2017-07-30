CLASS AND OBJECTS:
     
class master(object):
    func=5
    def students(self):
        print("Hi sir....good morning...")
        print("Total students presents:",self.func)
    def staff_members(self):
        print("Welcome sir...")
        return self.func
        
source=master()
source.students()
print(source.staff_members())
