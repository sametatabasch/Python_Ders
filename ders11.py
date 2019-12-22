kullanicilar = {
    "samet": {
        "sifre": "1234",
        "adı": "Samet",
        "soyadı": "ATABAŞ"
    },
    "ahmet": {
        "sifre": "ahmet61",
        "adı": "Ahmet Can",
        "soyadı": "ATABAŞ"
    },
    "vecihi": {
        "sifre": "hürkuş",
        "adı": "Vecihi",
        "soyadı": "hürkuş"
    }
}

gKullaniciAdi= input("Kullanıcı Adınız:").lower()


if gKullaniciAdi in kullanicilar:
    gSifre = input("Şifreniz:")
    if gSifre == kullanicilar[gKullaniciAdi]["sifre"]:
        print("Hoşgeldiniz. Sayın",
              kullanicilar[gKullaniciAdi]["adı"].capitalize(),
              kullanicilar[gKullaniciAdi]["soyadı"].upper()
        )
    else:
        print("Yanlış Şifre")
else:
    print("Böyle bir kullanıcı Yok")