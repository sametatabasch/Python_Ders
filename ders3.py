'''
Kullanıcının girdiği sayının tek mi çift mi olduğunu belirleyen program

1 Başla
2 Sayı Al "Bir sayı girin:", sayi
3 Eğer sayi % 2 == 0 ise Yaz "Çift"
4 Değilse yaz "Tek"
5 Bitir
'''

sayi = input("Sayı Girin:") # input değişkeni string değer döner
print(type(sayi)) #<class 'str'>
print(sayi*3)
sayi =int(sayi) # string olan sayi değişkeni integer yapılıyor
print(type(sayi)) #<class 'int'>
print(sayi*5)

if sayi % 2 == 0: # Eğer sayının 2 ile bölümünden kalan 0 ise
    print("Sayı Çifttir") # Yaz Sayı Çifttir
else:
    print("Sayı Tektir") # Yaz Sayı Çifttir