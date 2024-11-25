from abc import ABC, abstractmethod
class Animal(ABC):
    total_weight = 0
    all_animals = []

    @abstractmethod
    def set_weight(self, new_weight):
        pass

class Dog(Animal):
    def __init__(self, weight):
        Animal.total_weight += weight
        self.weight = weight
        Animal.all_animals.append(self)


    def set_weight(self, new_weight):
        diff = new_weight - self.weight
        Animal.total_weight += diff
        self.weight = new_weight

dog1 = Dog(5)
dog2 = Dog(2)
dog2.set_weight(1)
dog2.set_weight(4)

print(Animal.total_weight)
print(dog1.total_weight)

for animal in Animal.all_animals:
    print(animal)
