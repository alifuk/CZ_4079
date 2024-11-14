import pickle

def soucet(a,b):
    return a+b

vysledek = soucet(input("a:"),input("b:"))

with open('data.pickle', 'wb') as f:
    pickle.dump(vysledek, f)