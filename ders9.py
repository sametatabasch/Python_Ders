meyveler =["şeftali","armut","ayva","portakal"]

if "muz" in meyveler:
    print("evet")
else:
    print("hayır")

meyveler[2]="muz"

meyveler.insert(2,"at")

for meyve in meyveler:
    print(meyve,end=" ")

if "muz" in meyveler:
    print("evet")

meyveler.clear()

günler = {
  1: "pazartesi",
  2: "salı",
  3: "çarşamba"
}

print(günler[2])

for anahtar in günler:
    print(anahtar)

for anahtar in günler.values():
    print(anahtar)

for anahtar, deger in günler.items():
    print(anahtar, " =>", deger)
