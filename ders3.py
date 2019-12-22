'''
Kullanıcının girdiği sayının tek mi çift mi olduğunu belirleyen program
'''


sayi = int(input("Sayı Girin:"))

if sayi % 2 == 0:
    print("Sayı Çifttir")
else:
    print("Sayı Tektir")