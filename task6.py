class Animals:
    total_weight = 0
    all_animals = []

    def __init__(self, weight, age):
        self.weight = weight
        self.age = age
        Animals.all_animals.append(self)
        Animals.add_weight(self.weight)

    @classmethod
    def add_weight(cls, weight):
        cls.total_weight += weight

    @classmethod
    def delete_weight(cls, weight):
        cls.total_weight -= weight

    def set_weight(self, changed_weight):
        Animals.delete_weight(self.weight)
        self.weight = changed_weight
        Animals.changed_weight(self.weight)



    def look(self):
        print(f"Looking at you...")

    def breath(self):
        print(f"Breathing normally when not active.")

class Fish(Animals):

    def swim(self):
        print("Swimming in the sea.")

    def turn(self):
        print("Turning right...")

class Bird(Animals):

    def turn(self):
        print("Turning left...")

    def fly(self):
        print("Flying high, feeling free...")

class Mammal(Animals):

    def run(self):
        print("Running fast when needed.")

class DomesticDog(Mammal):

    def __init__(self, weight, age, breed, coat_color):
        super().__init__(weight, age)
        self.breed = breed
        self.coat_color = coat_color

    def bark(self):
        print(f"Barking at a postman or just for fun.")

    def retrieve(self):
        print(f"Retrieving everything back to the owner.")

class Ptakopysk(Bird, Fish):
    pass

ptakopysk = Ptakopysk(20, 3)
ptakopysk.turn()

dd1 = DomesticDog(30, 7, "german shepherd", "brown")
dd1.bark()
print(dd1.breed)
dd1.look()
brd1 = Bird(0.4, 4)
brd1.turn()
brd1.set_weight(0.6)
print(Animals.total_weight)

for animal in Animals.all_animals:
    print(animal)