#száma-cikkszám-mennyiség

class Rendeles:
    def __init__(self, szama, cikkszam, mennyiseg):
        self.szama = szama
        self.cikkszam = cikkszam
        self.mennyiseg = mennyiseg

    def __str__(self):
        txt = f"{self.szama}, {self.cikkszam}, {self.mennyiseg}"
        return txt
        