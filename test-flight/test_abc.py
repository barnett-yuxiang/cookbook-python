from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def __init__(self, name: str):
        pass

    @abstractmethod
    def make_sound(self):
        pass

class Cat(Animal):
    def __init__(self, name: str):
        self.name = name

    def make_sound(self):
        return "Meow"

cat = Cat("Whiskers")
print(f"{cat.name} says {cat.make_sound()}")
