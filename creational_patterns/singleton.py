class Borg:
    """The Borg Design pattern"""
    _shared_data = {} #Attribute Dictionary
    def __init__(self):
        self.__dict__ = self._shared_data # Overriding inbuilt dict to update attributes of object. Not important here.

class Singleton(Borg):
    """The singleton class. Inheriting from Borg allows to share variables across all instances"""
    def __init__(self, **kwargs):
        Borg.__init__(self) # initiating the Borg class init to set the __dict__ attribute.
        self._shared_data.update(kwargs) # updates the Class variable _shared_data in Borg with new values appended. SO that updated for new object too.

    def __str__(self):
        return str(self._shared_data)

    def update_shared_data(self,**kwargs): # updates shared data post object creation
        self._shared_data.update(kwargs)

#create first Singleton object
obj1 = Singleton(
    TCP = "Transmission Control Protocol"
)
print(obj1)

#Create second Singleton object
obj2 = Singleton(
    UDP = "User Datagram Protocol"
)
print(obj2)

# update shared data post object creation
obj1.update_shared_data(IP = "Internet Protocol")
print(obj2)