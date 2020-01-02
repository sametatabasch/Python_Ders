ders = "Algoritma ve Progamlama"
kAdi = "samet"
sifre = "123456"

ad = input("Adınız:").strip().capitalize() # Kullanıcıdan "Adınız:" mesajı ile ismi alınıp gereksiz boşluklar silinecek (strip) ve ilk harfi büyük gersi küçük olacak şekilde ad değişkenine aktarılacak
soyad = input("Soyadınız:").strip().upper() # Kullanıcıdan "Soyadınız:" mesajı ile soyadı alınıp gereksiz boşluklar silinecek (strip) ve tüm harfleri büyük yazarak soyad değişkenine aktaracak
girilenKAdi = input("Kullanıcı Adınız:").strip()

if len(girilenKAdi) <= 3: # len fonksiyonu karakter sayısını verir. girilen kullanıcı aldı 3 karakterden küçük ise
    print("Sayın", ad, soyad, "kullanıcı adınız Çok kısa. Lütfen daha uzun bir seçim yapın")
elif kAdi == girilenKAdi:
    girilenSifre = input("Şifreniz:")
    if sifre == girilenSifre:
        print("Hoşgeldiniz Sayın", ad, soyad)
    else:
        print("Sayın", ad, soyad, "yanlış şifre girdiniz.")
else:
    print("Sayın", ad, soyad, "yanlış kullanıcıadı girdiniz.")