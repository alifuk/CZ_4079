
def funkce_Livia():
    print("pokus")

def funkce_Nicole(delka):
    import random
    znaky = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
    heslo = ""
    for _ in range(delka):
        heslo += znaky[random.randint(0, len(znaky) - 1)]

    return heslo

def funkce_Milan():
    print("Gin tonic navzdy")

def funkce_Juraj():
    pass

def funkce_Jiri():
    print("Jirka rika, ze je dneska hezky pocasi.")

def funkce_Albert():
    print("Ahoj AL")
    pass

print("Díky za spolupráci")