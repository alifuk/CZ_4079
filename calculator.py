def calc():
    try:
        prvni_cislo = int(input("vloz prvni cislo: "))
    except(ValueError):
        print("vlozil jsi chybnou hodnotu, bude pouzito '1'")
        prvni_cislo = 1


    znamenko = input("vloz znak pozadovane matematicke operace (+, -, *, /): ")
    if znamenko not in ["+", "-", "*", "/"]:
        raise ValueError("zvolil jsi chybne matematickou operaci a program bude ukoncen")

    try:
        druhe_cislo = int(input("vloz druhe coslo: "))
    except(ValueError):
        print("vlozil jsi chybnou hodnotu, bude pouzito '1'")
        druhe_cislo = 1

    if znamenko == "+":
        print(f"soucet cisel {prvni_cislo} a {druhe_cislo} je {prvni_cislo + druhe_cislo}")
    elif znamenko == "-":
        print(f"rozdil cisel {prvni_cislo} a {druhe_cislo} je {prvni_cislo - druhe_cislo}")
    elif znamenko == "*":
        print(f"soucin cisel {prvni_cislo} a {druhe_cislo} je {prvni_cislo * druhe_cislo}")
    elif znamenko == "/":
        try:
            print(f"podil cisel {prvni_cislo} a {druhe_cislo} je {prvni_cislo / druhe_cislo}")
        except (ZeroDivisionError):
            print("chces delit nulou a to nejde")
    else:
        print(f"zvolil jsi chybnou operaci, program bude ukoncen")


try:
    calc()
except:
    print("Nastala nějaká vyjímka")
print("Ale program jede dál")