import requests, re
link = "https://ct24.ceskatelevize.cz"
hlavni_stranka = requests.get(link) #stáhne obsah stránky
vyraz = r"/clanek[A-z0-9/-]*"
odkazy = re.findall(vyraz, hlavni_stranka.text)
for odkaz in odkazy:
    print(link + odkaz)
    stranka = requests.get(link + odkaz) #stažení konkrétního článku
    vsechen_text = re.findall(r"<p[^>]*>[^<]*</p>", stranka.text) #Najdu na stránce pouze odstavce
    #Odstave jsou v <p>Podle ní by měla vláda nastavit dotace tak, aby se cena potravin snížila</p>
    for paragraf in vsechen_text:
        zkratky = re.findall(r"[ (][A-Z]{4}[) \.]", paragraf)
        for zkratka in zkratky:
            print(zkratka)
#Task 13 - nainstalovat knihovnu pomocí pip install requests
# přepsat si tento kód. Zeptat se jestli něco není jasné
#vyzkoušet - nalezení všech zkratek o třech znacích
#vyzkoušet - nalezení všech zkratek o čtyrech znacích
#vyzkoušet - nalezení všech slov, které začínají velkým písmenem
#extra - modifikovat tak, aby na https://auto.bazos.cz/ jsme prošli všechny odkazy a našli tam, kolik mají auta
#najeto km


