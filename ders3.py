'''
Kullanıcının girdiği sayının tek mi çift mi olduğunu belirleyen program
'''

sayi = input("Sayı Girin:") # input değişkeni string değer döner
sayi =int(sayi) # string olan sayi değişkeni integer yapılıyor

if sayi % 2 == 0: # Eğer sayının 2 ile bölümünden kalan 0 ise
    print("Sayı Çifttir") # Yaz Sayı Çifttir
else:
    print("Sayı Tektir") # Yaz Sayı Çifttir