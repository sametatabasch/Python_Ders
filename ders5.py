'''
vize ve final notunu alıp %40 ve %60 ını toplayıp dönem sonu bulan
'''

print("Ortalama Hesaplama programına hoşgeldiniz")
print("-" * 45)

vize = int(input("Vize Notunuz:"))
final = int(input("Final Notunuz:"))
donemSonu = vize * 40 / 100 + final * 0.6
if donemSonu>=50:
    print("Geçer")
else:
    print("Kalır")

print("Dönem sonu Notunuz =", int(donemSonu))
harfNotu = ""

if donemSonu >= 0 and donemSonu < 40:
    harfNotu = "FF"
elif donemSonu < 45:
    harfNotu = "DD"
elif donemSonu < 50:
    harfNotu = "DC"
elif donemSonu < 60:
    harfNotu = "CC"
elif donemSonu < 70:
    harfNotu = "CB"
elif donemSonu < 80:
    harfNotu = "BB"
elif donemSonu < 85:
    harfNotu = "BA"
elif donemSonu <= 100:
    harfNotu = "AA"
else:
    harfNotu = "Hata"

print("Harf Notunuz =", harfNotu)
