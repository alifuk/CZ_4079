from abc import ABC, abstractmethod

class Animals:
    total_weight = 0
    animal_list = []
    def __init__(self, species: str, weight: int, age: int):
        self.species = species
        self.weight = weight
        self.age = age
        Animals.total_weight += self.weight
        Animals.animal_list.append(self)

    @abstractmethod
    def set_weight(self):
        Animals.total_weight -= self.weight
        self.weight = int(input("zadejte aktualni vahu zvirete zaokrouhlenou na jednotky kg:"))
        Animals.total_weight += self.weight


    def look(self):
        print(f"to je ale hezke {self.species}")

    def breath(self):
        print(f"zhluboka se nadechni pane {self.species}")

class Mammal(Animals):
    def run(self):
        print(f"utikej {self.species}")


class Bird(Animals):
    def fly(self):
        print(f"koukej odletet {self.species}")

class Fish(Animals):
    def swim(self):
        print(f"odplav {self.species}")
    def print_info(self):
        print(f"tato ryba plave")

class Domestic_dog(Mammal):
    def __init__(self,species, weight, age, breed: str, coat_color: str):
        super().__init__(species, weight, age)
        self.breed = breed
        self.coat_color = coat_color
    def print_info(self):
        print(f"teento pejsek ma rasu {self.breed}")


class Pso_Ryba(Fish, Domestic_dog):
    def __str__(self):
        return f"to je divne zvire. Jmenuje se {self.species}, vazi {self.weight}, je mu {self.age} let a je rasy {self.breed}. A navic je {self.coat_color}"

# podivnost = Pso_Ryba("divnej",56, 22, "kokr", "ruzovy")

jelen = Mammal("kudu", 215, 14)
pirana = Fish("pirana", 2, 3)
vrabec = Bird("vrabec", 155, 2)
velryba = Mammal("keporkak", 1252, 58)
# podivnost.print_info()
# print(podivnost)
#
# print(Animals.total_weight)
# # velryba.set_weight()
# print(Animals.total_weight)
#
# print(Animals.animal_list)

for animal in Animals.animal_list:
    print(f"zvire {animal.species} vazi {animal.weight}Kg.")

