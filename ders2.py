'''
Kullanıcının girdiği iki sayının ortalamasın alan program
1 Başla
2 Sayı Al "Birinci Sayıyı Girin:", sayi1
3 Sayı Al "İkinci Sayıyı Girin:", sayi2
4 ort = (sayi1+sayi2)/2
5 Yaz ort
6 Bitir
'''

'''
15. Satır: input() fonksiyonu ile kullanıcıdan veri alınıyor.
bu veri int() fonksiyonu ile tamsayıya dönüştürülüyor ve 
bu sayı sayi1 değişkenine atanıyor.
'''
sayi1 = int(input("Birinci Sayıyı Girin:"))
sayi2 = int(input("İkinci Sayıyı Girin:"))

ort = (sayi1 + sayi2) / 2

print(ort)