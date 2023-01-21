from Poggyasz import Poggyasz
lista = []
def beolvas():
    fajlom = open("csomag.txt", "r", encoding="utf-8")
    fejlec = fajlom.readline()
    sorok = fajlom.readlines()
    fajlom.close()

    i = 0
    while i < len(sorok):
        sor = sorok[i].strip().split("#")
        lista.append(Poggyasz(sor))
        print(sor)
        i += 1

def poggyaszok_szama():
    print("III/A, B:")
    print(f"\t A pogyászok száma: {len(lista)}")

def poggyaszok_atlag_sulya():
    i = 0
    c = 0
    sulyok = 0
    while i < len(lista):
        if lista[i].a == 51:
            c += 1
            sulyok += lista[i].m
        i += 1
    atlag = sulyok / c
    return int(atlag * 1000)

def legmagasabb():
    legmagasabbak = 0
    max = lista[0].b
    i = 0
    while i < len(lista):
        if max < lista[i].b:
            max = lista[i].b
            legmagasabbak = i
        i += 1
    return lista[legmagasabbak]

