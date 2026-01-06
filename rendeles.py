from Megrendeles import Megrendeles

rendeles_lista = []

def fajlbeolvasas():
    f = open("rendeles.txt", "r", encoding="UTF-8")
    f.readline()
    sorok = f.readlines()
    f.close()

    i = 0
    while i < len(sorok):
        sor = sorok[i].strip().split("-")
        rendeles = Megrendeles(sor[0], sor[1], int(sor[2])) # mindig uj lesz
        rendeles_lista.append(rendeles)
        i += 1
    return rendeles_lista

def tetelek_szama(lista):
    print("III/A, B:\n")
    ossz = 0
    while ossz < len(lista):
        ossz += 1
    print(f"\tA rendelési tételek száma: {ossz}.")

def BG01(lista):
    print("III/C:\n")
    ossz = 0
    i = 0
    while ossz < len(lista):
        if lista[i].cikkszam == "BG01":
            ossz += 1
        i += 1
        
