"""
__init__ (The Constructor):
Purpose: __init__ is a special method (a function inside a class) that is automatically called when you create a new object (instance) of a class. It's often referred to as the "constructor."
Role: Its primary role is to initialize the object's attributes (data or properties). Think of it as setting up the initial state of the object.

self:

self refers to the current object instance.
self is used to access and modify the object's attributes within its methods.

"""
class BankApp:
    def __init__(self, depositorid):
        self.depositorid = depositorid
    def get_Balance(self, depositorname):
        print("Amount in " + str(self.depositorid) + f" and {depositorname} is 500")

x = BankApp(100)
x.get_Balance("vinod")

