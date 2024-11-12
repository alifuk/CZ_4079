haah




# CZ_4079

Přihlášení na github pomocí jména a hesla nebo pomocí SSH

## Jak vytvořit ssh klíč


příkazem `ssh-keygen.exe`
- to mi vygeneruje v domovskásložka/.ssh soubory `id_rsa` a `id_rsa.pub`
- obsah `id_rsa.pub` vložíme na github-Settings-SSH a GPT keys

## Git nastavení user a hesla
`git config --global user.name "FIRST_NAME LAST_NAME"`
`git config --global user.email "example@email.com"`


## Úkol 1 - Kalkulačka

- Vytvořit github repo
- Naklonovat si to na PC
- napsat něco do readme.md, vytvořit commit a pushnout to
- dát do .gitignore `.idea`
- poslat do chatu URL na to repo
- udělat kalkulačku - zeptá se nás na první číslo, znaménko a druhé číslo (načítat lze pomocí `input()`)
- zacommitovat a pushnout

## Úkol 2 - Exception
- ošetřit vstup
- ošetřit dělení nulou
- vyvolejte vyjímku, pokud uživatel zadal nějaké jiné znaménko než je povolené

## Úkol 2 - Extra
- nekonečná kalkulačka - dokud nenapíšeme "konec", tak se nás kalkulačka stále ptá na další operace

## Task 1 - Calculator

- Create a GitHub repository.
- Clone it to your PC.
- Write something in readme.md, create a commit, and push it.
- Add `.idea` to `.gitignore`.
- Send the URL of the repository in the chat.
- Create a calculator:
- It should prompt the user for the first number, an operator, and the second number (using input()).
- Commit and push the changes.
- 
## Task 2 - Exception Handling

- Validate user input.
- Handle division by zero.
- Raise an exception if the user enters an operator that is not allowed.
- 
## Task 2 - Extra

- Infinite calculator - the calculator should keep asking for operations until the user types "end".

## Task 4 - Dědičnost tříd
![task4](task4.png)

Podle tohoto obrázku napsat třídy v Pythonu. Výsledek přidejte do nového souboru ve vašem repozitáři a zacommitujte.

Write classes in Python according to this diagram. Add the result to a new file in your repository and commit it."

## Task 5 - vícenásobné dědění
- Dvě třídy aby měli stejnou metodu.
- Jiná třída dědí od obou tříd.
- Instance jiné třídy zavolá onu metodu - z jaké třídy bude metoda vykonána?

ENG:
- Two classes should have the same method.
- Another class inherits from both classes.
- An instance of this other class calls that method - from which class will the method be executed?

## Task 6 - celková váha zvířát
- vycházíme z diagramu na obrázku výše
- při vytvoření zvířete, se přičte jeho váha k celkové váze (property `total_weight` u třídy Animals)
- zvířata mají metodu `set_weight`
- když na konci programu napíšu `print(Animals.total_weight)`, tak se mi vypíše celková váha všech zvířat