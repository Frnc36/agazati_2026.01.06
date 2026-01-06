import random

def veletlen():
    
    velszam_lista = []
    i = 0
    while i < 5:
        szam = random.randint(10,20)
        velszam_lista.append(szam)
        i += 1
    return velszam_lista

def kiiras(velszam):
    print("II/A, B, C:")
    i = 0
    while i < len(velszam):
        if i < len(velszam) - 1:
            print(velszam[i], end="-")
        else:
            print(velszam[i])
        i += 1

def kisebb(lista):
    darab = 0
    aktualis = 0
    i = 0
    while i < len(lista):
        if lista[i] < aktualis:
            darab += 1
        aktualis = lista[i]
        i += 1
    return darab

def konzolba_ir(darab):
    print("\nII/D, E:\n")
    print(f"\tKisebb számok száma: {darab}")

def fajlba_ir(darab):
    with open("vegeredmeny.txt ", "w", encoding="UTF-8") as f:
        f.write(f"II/F:\n\tKisebb számok száma: {darab}")