def with_password(func):
    def novy_soucet(a, b):
        password = "zirafa"
        if input("vlozte heslo: ") == password:
            return func(a, b)
        else:
            return "Špatné heslo"
    return novy_soucet

@with_password
def soucet(a,b):
    return a + b

print(soucet(3,5))
