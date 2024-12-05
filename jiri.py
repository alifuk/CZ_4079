print("Start")
def print_pred_a_po(fnc):
    print(f"Vykonává se dekorátor pro funkci {fnc.__name__}")
    def jina_funkce(a,b):
        print(f"byla spuštěna jiná funkce i přestože jsi pouštěl funkci {fnc.__name__}. Součet je {a+b}")
        print(fnc("Albert"))
    return jina_funkce

@print_pred_a_po
def druhy_a_treti_znak(retezec):
    return retezec[1:3]

@print_pred_a_po
def treti_a_ctvrty_znak(retezec):
    return retezec[2:4]

druhy_a_treti_znak(5,6)
treti_a_ctvrty_znak(7,8)
