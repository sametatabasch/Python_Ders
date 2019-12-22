ders = "Algoritma ve Progamlama"
kAdi = "samet"
sifre = "123456"

ad = input("Adınız:").strip().capitalize()
soyad = input("Soyadınız:").strip().upper()
girilenKAdi = input("Kullanıcı Adınız:").strip()

if len(girilenKAdi) <= 3:
    print("Sayın", ad, soyad, "kullanıcı adınız Çok kısa. Lütfen daha uzun bir seçim yapın")
elif kAdi == girilenKAdi:
    girilenSifre = input("Şifreniz:")
    if sifre == girilenSifre:
        print("Hoşgeldiniz Sayın", ad, soyad)
    else:
        print("Sayın", ad, soyad, "yanlış şifre girdiniz.")
else:
    print("Sayın", ad, soyad, "yanlış kullanıcıadı girdiniz.")