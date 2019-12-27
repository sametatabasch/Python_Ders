def ciftMiTekMi(s=6):
    """
    Girilen sayının çift yada tek olduğunu belirler
    :param s: 'int'
    """
    if s % 2 == 0:
        print("Sayı Çift")
    else:
        print("Sayı Tek")


ciftMiTekMi()
ciftMiTekMi(4)
ciftMiTekMi(45678)
