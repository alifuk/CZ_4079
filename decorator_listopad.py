pass
def obalka(func):
    print(f"Dekorátor přijal jako parametr funkci {func.__name__}")
    def podfunkce(a,b):
        print(f"Dostal jsem parametry {a} a {b}, jdu zavolat funkci {func.__name__}")
        return func(a,b)
    return podfunkce
#dekorátor nám nahradí dekorovanou funkci za výstup dekorátoru
@obalka
def secti(a,b):
    return a+b

@obalka
def rozdil(a, b):
    return a - b

@obalka
def nasobeni(a, b):
    return a * b
print(f"Součet čísel 3 a 4 je {secti(3,4)}")
print(f"Rozdíl čísel 3 a 4 je {rozdil(3,4)}")







