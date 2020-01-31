def ElmaSayisi(para):
    """
    Her seferinde parasının yarısı ile 1 ₺ ye elma alındığında toplam kaç elma alınır
    :param int para : Başlangıçtaki para miktarı
    :return: Toplamda alınan elma miktarı
    :rtype: float
    """
    if para/2<1:
        return 0
    else:
        return para/2 + ElmaSayisi(para/2)


print(ElmaSayisi(10))
def faktoriyel(s):
    if s==1:
        return 1
    else:
        return s*faktoriyel(s-1)

print(faktoriyel(5))