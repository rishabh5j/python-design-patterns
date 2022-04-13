from abc import ABC,abstractmethod
class Animal(ABC):
    """Abstract product Animal. Acts as base to concrete objects Dog and cat.
    """
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def speaks(self):
        pass

class Food(ABC):
    """Abstract product Food. Acts as base to concrete objects Bone and Milk.
    """
    @abstractmethod
    def food(self):
        pass

class Dog(Animal):
    """Concrete product. Derived from Abstract product Animal.
    """
    def __init__(self):
        self.__str__ = "Dog"
    def speaks(self):
        return "Woof!"

class Cat(Animal):
    """Concrete product. Derived from Abstract product Animal.
    """
    def __init__(self):
        self.__str__ = "Cat"
    def speaks(self):
        return "Meow!"

class Bone(Food):
    """Concrete product. Derived from Abstract product Food.
    """
    def food(self):
        return "Bone"

class Milk(Food):
    """Concrete product. Derived from Abstract product Food.
    """
    def food(self):
        return "Milk"

class AnimalFactory(ABC):
    """Abstract Factory class.
    The Abstract Factory interface declares a set of methods that return
    different abstract products. These products are called a family and are
    related by a high-level theme or concept. Products of one family are usually
    able to collaborate among themselves. A family of products may have several
    variants, but the products of one variant are incompatible with products of
    another.
    """
    @abstractmethod
    def get_animal(self) -> Animal:
        pass

    @abstractmethod
    def get_food(self) -> Food:
        pass

class DogFactory(AnimalFactory):
    """Dog Concrete Factory class. Derived from Abstract Factory AnimalFactory.
    """
    def get_animal(self) -> Animal:
        """Returns back Concrete product(which is derived from Abstract product).
        """
        return Dog()
    def get_food(self) -> Food:
        return Bone().food()

class CatFactory(AnimalFactory):
    """Cat Concrete Factory class. Derived from Abstract Factory AnimalFactory.
    """
    def get_animal(self) -> Animal:
        """Returns back Concrete product(which is derived from Abstract product).
        """
        return Cat()
    def get_food(self) -> Food:
        return Milk().food()

dogObj = DogFactory()
print(dogObj.get_animal())
print(dogObj.get_food())