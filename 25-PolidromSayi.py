sayi=input("sayı girin:")
l=len(sayi)
polidrom=True
for i in range(l):
    if sayi[i]!=sayi[l-i-1]:
        polidrom=False
        break
if polidrom:
    print("Polidrom sayı")
else:
    print("Polidrom sayı değil")