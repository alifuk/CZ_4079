def with_password(func):
    def pass_protect(*args, **kwargs):
        password = "prase"
        if input("vlozte heslo: ") == password:
            return func(*args, **kwargs)
        else:
            return "Špatné heslo"
    return pass_protect

@with_password
def soucetAB(a,b):
    return a + b

@with_password
def soucer_all(*args):
    soucet = 0
    for i in args:
        soucet += i
    return soucet


print(soucetAB(3,5))
print(soucer_all(5,2,4,3,4,8,5))