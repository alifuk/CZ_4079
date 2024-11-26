import time
from datetime import datetime

class TimeMeasurment:
    def __init__(self):
        pass
    def __enter__(self):
        self.start_time = time.time()
        print(f"Spouštím výpočet v čase {datetime.now().strftime('%H:%M:%S')}")
        return None
    def __exit__(self, a, b, c):
        total_time = time.time()-self.start_time
        print(f"Dokončeno v čase {datetime.now().strftime('%H:%M:%S')} - blok trval {total_time:.3f} sekundy")
        pass

with TimeMeasurment() as t: #"Spouštím výpočet v čase 18:59.03"
    cislo = 1
    for i in range(10000000):
        cislo += i
    print(cislo) #49999995000001

with TimeMeasurment() as t:
    print("HA")
#"Dokončeno v čase 18:59.05 - blok trval 3 sekundy
