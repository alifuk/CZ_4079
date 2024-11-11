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


