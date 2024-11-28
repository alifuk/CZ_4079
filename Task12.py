#Task12 - Vytvoříte generátor, který bude postupně vracet
# Albert - máme koncovku "bert".
# před tu koncovku budou dávány předpony "Al", "Ro", "Hu", "Nor", "Gil"

def GeneratorMien(predpona, koncovka):
    for predpon in predpona:
        yield predpon + koncovka

predpona = ["Ive", "Ane", "Evi", "Ani", "Ri"]
koncovka = "ta"

for meno in GeneratorMien(predpona, koncovka):
    print(f"Tvoje meno je {meno}.")







