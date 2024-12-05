print("zacatek")
def vyprintuj_a_pust(func):
    print("dekorátor se mi spouští")
    def nova_funkce(a,b):
        print(f"pouštíme funkci {func.__name__} s parametry {a}, {b}")
        hes = input("heslo")
        if hes == "AA":
            return func(a,b)
        else:
            return "blbé heslo"

    return nova_funkce

@vyprintuj_a_pust
def soucet(a,b):
    return a+b

@vyprintuj_a_pust
def rozdil(a,b):
    return a-b

print(soucet(3,5))

print(soucet(3,5))
print(rozdil(3,5))
