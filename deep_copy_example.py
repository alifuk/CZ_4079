from copy import deepcopy
class Garage:
    def __init__(self):
        self.spaces = []
    def add_car(self, car_name):
        self.spaces.append(car_name)
brno_garage = Garage()
brno_garage.add_car("Volvo")
brno_garage.add_car("Maserati")
print(f"V garáži brno je: {brno_garage.spaces}")
#praha_garage = deepcopy(brno_garage)
praha_garage = brno_garage
print(f"V praha_garage je: {praha_garage.spaces}")
praha_garage.add_car("Trabant")
print("Do prahy jsme přidali trabanta")
print(f"V garáži brno je: {brno_garage.spaces} id: {id(brno_garage)}")
print(f"V praha_garage je: {praha_garage.spaces} id: {id(praha_garage)}")
