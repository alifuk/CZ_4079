
class TimeMeasurment:
    pass

with TimeMeasurment() as t: #"Spouštím výpočet v čase 18:59.03"
    cislo = 1
    for i in range(10000000):
        cislo += i
    print(cislo) #49999995000001
#"Dokončeno v čase 18:59.05 - blok trval 3 sekundy
