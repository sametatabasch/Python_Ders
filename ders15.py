def selamla():
    """Merhaba mesajını yazdırır"""
    print("Merhaba")


#selamla()


def selamla1(isim):
    print("Merhaba", isim)


#selamla1("sdfgh")


def selamla2(isim):
    return "Merhaba " + isim

def topla(s1,s2):
    return s1+s2


print(selamla2("Ahmet"),topla(5,6))
sonuc= 5*2+topla(7,9)
print(sonuc)
print(selamla2("Ahmet").upper())
