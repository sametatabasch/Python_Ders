kullaniciAdlari = {
    1: "samet",
    2: "ahmet",
    3: "veli"
}
sifreler = {
    1: "1234",
    2: "asdf",
    3: "qwert"
}

gKullaniciAdi = input("Kullanıcı Adınız:").lower()
gSifre = input("Sifre:")

if gKullaniciAdi in kullaniciAdlari.values() and gSifre in sifreler.values():
    print("Giriş Yapıldı")
else:
    print("Giriş yapılamadı")
