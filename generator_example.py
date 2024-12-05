#Ukázka generátoru
def generuj_mocniny(kolik_cisel_vygenerovat):
    for i in range(kolik_cisel_vygenerovat):
        yield (i+1) ** 2

for mocnina in generuj_mocniny(6):
    print(mocnina)














