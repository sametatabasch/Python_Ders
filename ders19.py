def asalMi(s):
    asal = True

    for i in range(2, s, 1):
        if s % i == 0:
            asal = False
            break
    return asal


girilenSayilar = []
for i in range(5):
    g = int(input("Sayı Girin:"))
    girilenSayilar.append(g)

print(girilenSayilar)

for sayi in girilenSayilar:
    if asalMi(sayi):
        print(sayi,"Asal bir sayı")
    else:
        print(sayi, "Asal bir sayı değil")
