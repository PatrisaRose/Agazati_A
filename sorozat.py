import random
vel_list = []

def dollar_jellel_elvalasztott_random_12_szam_nem_masoltam_Janirol():
    print("II/A, B, C:")
    i = 0
    szoveg = ""
    while i < 12:
        vel = int(random.random()*1011)-10
        vel_list.append(vel)
        if i == 11:
            szoveg += str(vel)
        else:
            szoveg += str(vel) + "@"
        i += 1
    print(f'\t {szoveg}')

def paratlanok_szama():
    i = 0
    c = 0
    while i < len(vel_list):
        if vel_list[i] % 2 != 0:
            c += 1
        i += 1
    return c

def konzol_kiir():
    print(f"A páratlanok száma: {paratlanok_szama()}")

def fajlba_kiir():
    fajlom = open("eredmeny.txt", "w", encoding="utf-8")
    fajlom.write(f"II/F:\n \tA páratlanok száma: {paratlanok_szama()}")
    fajlom.close()