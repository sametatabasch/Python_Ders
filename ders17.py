def ciftMi(s):
    """
    Girilen sayının çift yada tek olduğunu belirler
    :param s: 'int'
    """
    if s % 2 == 0:
        return True
    else:
        return False


for i in range(0, 36, 1):
    if ciftMi(i):
        print(i, "sayısı Çift sayıdır")

