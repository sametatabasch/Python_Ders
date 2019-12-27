def selamla():
    """Merhaba mesajını yazdırır"""
    print("Merhaba")


selamla()


def selamla1(isim):
    print("Merhaba", isim)


selamla1("Samet")


def selamla2(isim):
    return "Merhaba " + isim


print(selamla2("Ahmet"))
print(selamla2("Ahmet").upper())
