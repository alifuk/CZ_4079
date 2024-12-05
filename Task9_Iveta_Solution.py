'''
Task 9 author - Iveta Szabóová
'''
import json
import pickle
import csv

class NakupnyZoznam:
    def __init__(self):
        self.zoznam = []

    def pridat_polozku(self):
        polozka = input("Zadajte názov položky: ")
        self.zoznam.append(polozka)
        print(f"Položka '{polozka}' bola pridaná do zoznamu.")

    def vypisat_polozky(self):
        if self.zoznam:
            print("Váš nákupný zoznam:")
            for i, polozka in enumerate(self.zoznam, start=1):
                print(f"{i}. {polozka}")
        else:
            print("Zoznam je prázdny.")

    def zmazat_polozku(self):
        self.vypisat_polozky()
        try:
            cislo = int(input("Zadajte číslo položky na zmazanie: "))
            if 1 <= cislo <= len(self.zoznam):
                zmazana = self.zoznam.pop(cislo - 1)
                print(f"Položka '{zmazana}' bola zmazaná.")
            else:
                print("Nesprávne číslo.")
        except ValueError:
            print("Zadajte platné číslo.")

    def upravit_polozku(self):
        self.vypisat_polozky()
        try:
            cislo = int(input("Zadajte číslo položky na úpravu: "))
            if 1 <= cislo <= len(self.zoznam):
                nova_polozka = input("Zadajte nový názov položky: ")
                self.zoznam[cislo - 1] = nova_polozka
                print(f"Položka č. {cislo} bola upravená na '{nova_polozka}'.")
            else:
                print("Nesprávne číslo.")
        except ValueError:
            print("Zadajte platné číslo.")

    def ulozit_do_csv(self):
        nazov_suboru = input("Zadajte názov súboru na uloženie (napr. zoznam.csv): ")
        try:
            with open(nazov_suboru, "w", newline="", encoding="utf-8") as subor:
                writer = csv.writer(subor)
                for polozka in self.zoznam:
                    writer.writerow([polozka])
            print(f"Zoznam bol uložený do súboru '{nazov_suboru}'.")
        except Exception as e:
            print(f"Chyba pri ukladaní do CSV: {e}")

    def nacitat_z_csv(self):
        nazov_suboru = input("Zadajte názov súboru na načítanie (napr. zoznam.csv): ")
        try:
            with open(nazov_suboru, "r", encoding="utf-8") as subor:
                reader = csv.reader(subor)
                self.zoznam = [riadok[0] for riadok in reader]
            print(f"Zoznam bol načítaný zo súboru '{nazov_suboru}'.")
            self.vypisat_polozky()
        except Exception as e:
            print(f"Chyba pri načítaní z CSV: {e}")

    def ulozit_do_pickle(self):
        nazov_suboru = input("Zadajte názov súboru na uloženie (napr. zoznam.pkl): ")
        try:
            with open(nazov_suboru, "wb") as subor:
                pickle.dump(self.zoznam, subor)
            print(f"Zoznam bol uložený do súboru '{nazov_suboru}'.")
        except Exception as e:
            print(f"Chyba pri ukladaní do pickle: {e}")

    def nacitat_z_pickle(self):
        nazov_suboru = input("Zadajte názov súboru na načítanie (napr. zoznam.pkl): ")
        try:
            with open(nazov_suboru, "rb") as subor:
                self.zoznam = pickle.load(subor)
            print(f"Zoznam bol načítaný zo súboru '{nazov_suboru}'.")
            self.vypisat_polozky()
        except Exception as e:
            print(f"Chyba pri načítaní z pickle: {e}")

    def ulozit_do_json(self):
        nazov_suboru = input("Zadajte názov súboru na uloženie (napr. zoznam.json): ")
        try:
            with open(nazov_suboru, "w", encoding="utf-8") as subor:
                json.dump(self.zoznam, subor, ensure_ascii=False, indent=4)
            print(f"Zoznam bol uložený do súboru '{nazov_suboru}'.")
        except Exception as e:
            print(f"Chyba pri ukladaní do JSON: {e}")

    def nacitat_z_json(self):
        nazov_suboru = input("Zadajte názov súboru na načítanie (napr. zoznam.json): ")
        try:
            with open(nazov_suboru, "r", encoding="utf-8") as subor:
                self.zoznam = json.load(subor)
            print(f"Zoznam bol načítaný zo súboru '{nazov_suboru}'.")
            self.vypisat_polozky()
        except Exception as e:
            print(f"Chyba pri načítaní z JSON: {e}")

class Operacie:
    def __init__(self):
        self.nakupny_zoznam = NakupnyZoznam()

    def spustit(self):
        while True:
            print("\nNÁKUPNÝ ZOZNAM")
            print("1. Pridať položku")
            print("2. Vypísať všetky položky")
            print("3. Zmazať položku")
            print("4. Upraviť položku")
            print("5. Uložiť zoznam do CSV")
            print("6. Načítať zoznam z CSV")
            print("7. Uložiť zoznam do pickle")
            print("8. Načítať zoznam z pickle")
            print("9. Uložiť zoznam do JSON")
            print("10. Načítať zoznam z JSON")
            print("11. Ukončiť")

            volba = input("Zvoľte možnosť: ")

            if volba == "1":
                self.nakupny_zoznam.pridat_polozku()
            elif volba == "2":
                self.nakupny_zoznam.vypisat_polozky()
            elif volba == "3":
                self.nakupny_zoznam.zmazat_polozku()
            elif volba == "4":
                self.nakupny_zoznam.upravit_polozku()
            elif volba == "5":
                self.nakupny_zoznam.ulozit_do_csv()
            elif volba == "6":
                self.nakupny_zoznam.nacitat_z_csv()
            elif volba == "7":
                self.nakupny_zoznam.ulozit_do_pickle()
            elif volba == "8":
                self.nakupny_zoznam.nacitat_z_pickle()
            elif volba == "9":
                self.nakupny_zoznam.ulozit_do_json()
            elif volba == "10":
                self.nakupny_zoznam.nacitat_z_json()
            elif volba == "11":
                print("Koniec programu.")
                break
            else:
                print("Nesprávna voľba, skúste znova.")



operacie3 = Operacie()
operacie3.spustit()

operacie2 = Operacie()
operacie4 = Operacie()
operacie5 = Operacie() #Konstruktor - protože to konstruuje objekt/instanci =  __init__
