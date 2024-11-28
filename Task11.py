#Task 11 - udělat iterátor, kterému řekneme kolik chceme čísel, např. 5.
#Iterátor bude postupně vracet mocniny těchto čísel. Tzn pro číslo 5, iterátor vrátí 1, 4, 9, 16, 25
#Pro č. 3 by iterátor vrátil hodnoty 1,4,9
class Iterator_mocnin:
    def __init__(self, kolik_cisel_chceme):
        self.kolik_cisel_chceme = kolik_cisel_chceme
        self.pozice = 0
    def __iter__(self):
        return self
    def __next__(self):
        if self.pozice >= self.kolik_cisel_chceme:
            raise StopIteration
        self.pozice += 1
        return self.pozice ** 2
mocniny = Iterator_mocnin(5)
for mocnina in mocniny:
    print(mocnina)