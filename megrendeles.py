#száma-cikkszám-mennyiség

class Megrendeles:
    def __init__(self, szama, cikkszam, mennyiseg:int):
        self.szama = szama
        self.cikkszam = cikkszam
        self.mennyiseg = int(mennyiseg)

    def __str__(self):
        txt = f"{self.szama}, {self.cikkszam}, {self.mennyiseg}"
        return txt
        