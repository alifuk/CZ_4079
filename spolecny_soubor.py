
def funkce_Livie():
    pass

def funkce_Nicole(delka):
    import random
    znaky = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
    heslo = ""
    for _ in range(delka):
        heslo += znaky[random.randint(0, len(znaky) - 1)]

    return heslo

def funkce_Milan():
    pass

def funkce_Juraj():
    pass

def funkce_Jiri():
    pass

def funkce_Albert():
    pass