import math

"""
# Örnek 6.1
yukseklik = float(input("Yüksekliği girin:"))
taban = float(input("Tabanı girin:"))

alan = yukseklik * taban / 2

print("Alan = ", alan)

# Örnek 6.2

derece = float(input("Dereceyi Girin:"))

radyan = derece * math.pi / 180
gradyan = derece * 200 / 180

print("Radyan =", radyan)
print("Gradyan =", gradyan)

# Örnek 6.3
A = float(input("Birinci Kenarı girin:"))
B = float(input("İkinci Kenarı girin:"))
aci = float(input("Aradaki açı:"))

alan = A * B * math.sin(aci * math.pi / 180) / 2

print(alan)

# Örnek 6.19

sayi1 = int(input("Birinci Sayıyı girin:"))
sayi2 = int(input("İkinci Sayıyı girin:"))

if sayi1 % sayi2 == 0:
    print("Tam bölünüyor")
else:
    print("Tam bölünmüyor")
"""

# Örnek 6.20
sayi = int(input("Bir sayıgirin."))

for i in range(1, sayi + 1, 1):
    if sayi % i == 0:
        print(i)
