# Task 9 - úkolovník
# Cílem úkolu je vytvořit poznámkový blok V poznámkovém bloku můžeme přidávat,
# odebírat nebo měnit řádky. Když spustíme program tak máme následující možnosti:
#
# Přidat poznámku (nakonec)
# Vypsat všechny poznámky
# Smazat poznámku (budeme vyzváni, jaký řádek smazat)
# Upravit poznámku (budeve vyzváni, jaký řádek a jak upravit)
# Uložit poznámky do souboru .csv (budeme vyzváni do jakého souboru)
# (Volitelně uložení i přes pickle)
# Načíst poznámky ze souboru .csv (budeme vyzváni z jakého souboru)



import csv

notes = []


def pridat_task(notes):
    notes.append(input("Vloz task: "))

def vypisat_task(notes):
    print(notes)


def delete_task(notes):
    print(notes)
    zmazanie = int(input("Zadaj cislo riadku na zmazanie: ")) - 1
    del notes[zmazanie]



def upravit_task(notes):
    print(notes)
    poradie = int(input("Zadaj poradie riadku: ")) - 1
    if 0 <= poradie <= len(notes):
        novy_task = input("Zadaj novy task: ")
        notes[poradie] = novy_task

#ulozit do CSV
def ulozit_task_do_csv(notes):
    file = input("Zadaj nazov suboru na uloženie: ")
    file_csv = file + ".csv"
    with open(file_csv, "a", encoding="utf-8") as new_file:
        writer = csv.writer(new_file)
        for line in notes:
            writer.writerow(line)

#nacitat zo CSV
def nacitat_task_z_csv(notes):
    file = input("Zadaj názov súboru na načítanie: ")
    file_csv = file + ".csv"
    with open(file_csv, "r", encoding="utf-8") as save_file:
        reader = csv.reader(save_file)
        for line in reader:
            notes.append(line)
        print(notes)




while True:

    print("\nWelcome to task-master")
    print("1. Pridat task")
    print("2. Vypísať všetky tasky")
    print("3. Delete task")
    print("4. Upraviť task")
    print("5. Ulozit task do súboru")
    print("6. Načítať task zo súboru")
    print("7. Exit")

    choice = input("Vyber moznosť: ")
    if choice == "1":
        pridat_task(notes)
    elif choice == "2":
        vypisat_task(notes)
    elif choice == "3":
        delete_task(notes)
    elif choice == "4":
        upravit_task(notes)
    elif choice == "5":
        ulozit_task_do_csv(notes)
    elif choice == "6":
        nacitat_task_z_csv(notes)
    elif choice == "7":
        print("Ukoncujem program")
        break
    else:
        print("Zlý výber. Prosím vyber medzi 1-5")