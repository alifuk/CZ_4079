import threading
import time
celkovy_soucet = 1
def secti(num):
    global celkovy_soucet
    print("Začínám vykonávat sčítání")
    for i in range(num):
        print(i)
        celkovy_soucet += i

def vynasob(num):
    global celkovy_soucet
    print("Začínám vykonávat násobení")
    for i in range(num):
        print(i)
        celkovy_soucet *= i+1

print("Spustí se pouze toto")
if __name__ == "__main__": #K čemu to je?
    print("toto se už nespustí")

    thread_secti  = threading.Thread(target=secti, args=(30000,))
    thread_vynasob = threading.Thread(target=vynasob, args=(300,))

    thread_secti.start()
    thread_vynasob.start()

    thread_secti.join()
    thread_vynasob.join()

    print(f"Vysledek scitani cisel od 1 do 1 000 000 je {celkovy_soucet}.")
