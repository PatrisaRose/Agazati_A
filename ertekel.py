def ertekel():
    print("I/A, B:")
    etel_neve = input("\t Étel neve: ")
    rendelo = input("\t Étel rendelőjének neve: ")
    ertekeles = int(input("\t Értékelés (1-5): "))

    print("I/C:")
    if ertekeles < 0:
        print("\t Az értékelés nem lehet negatív!")
    elif ertekeles == 0:
        print("\t")
    elif ertekeles > 5:
        print("\t 5 pont feletti értékelés nem elfogadható!")
    else:
        print("\t Köszönjük az értékelést!")

