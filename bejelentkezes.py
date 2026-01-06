def bekeres():
    print("I/A, B:\n")
    cim1 = str(input("\tEmail cim: "))
    cim2 = str(input("\tEmail cim még egyszer: "))
    jelszo = str(input("\tJelszó: "))
    
    print("I/C:\n")
    if cim1 == cim2:
        print(f"\tSikeres bejelentkezés {cim2}!")
    elif jelszo == "":
        print("\tSikertelen bejelentkezés (üres jelszó).")
    else:
       print("\tSikertelen bejelentkezés (email címek nem egyeznek).") 
    
