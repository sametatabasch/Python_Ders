meyveler =["şeftali","armut","ayva","portakal"]

if "muz" in meyveler:
    print("evet")
else:
    print("hayır")

meyveler[2]="muz"

for meyve in meyveler:
    print(meyve)

if "muz" in meyveler:
    print("evet")

meyveler.clear()

günler = {
  1: "pazartesi",
  2: "salı",
  3: "çarşamba"
}

for x,y in günler.items():
    print(x," =>",y)
