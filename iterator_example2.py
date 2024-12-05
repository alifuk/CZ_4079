import random
class IteratorNahodnychCisel:
    def __init__(self):
        print("Inicializuji náhodnou kostku")
        self.ukoncit = False

    def __iter__(self):
        return self

    def __next__(self):
        if self.ukoncit:
            raise StopIteration
        nahodne_cislo = random.randint(0,5) + 1
        if nahodne_cislo == 6:
            self.ukoncit = True
        return nahodne_cislo

kostka = IteratorNahodnychCisel()
for hod_kostkou in kostka:
    print(f"Padlo {hod_kostkou}")
print("Ukončeno")
