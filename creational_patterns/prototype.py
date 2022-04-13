import copy

class Prototype:
    def __init__(self):
        self._objects = {}

    def register_object(self, name, obj):
        """Register an object"""
        self._objects[name] = obj
    def unregister_object(self,name):
        """Unregister an object"""
        self._objects.pop(name)
    def clone(self, name, **attr):
        """Clone a registered object and update it's attributes"""
        obj = copy.deepcopy(self._objects.get(name))
        obj.__dict__.update(attr)
        return obj

class Car:
    def __init__(self):
        self.name = "i20"
        self.color = "Blue"
        self.options = "Ex"

c = Car() # This is the prototypical object to be called
prototype = Prototype()

prototype.register_object("hyundai", c) #returns back the object

c1 = prototype.clone("hyundai")

print(c1)