import os

while True:
    print(("*" * 50))
    print("* 1 - Toplama ".ljust(49), "*", sep="")
    print("* 2 - Çıkartma ".ljust(49), "*", sep="")
    print("*", " 3 - Çarpma ".ljust(48), "*", sep="")
    print("*", " 4 - Bölme ".ljust(48), "*", sep="")
    print("*", " q- Çıkış  ".ljust(48), "*", sep="")
    print(("*" * 50))

    islem = int(input("Yapmak istediğiniz işlem: "))
    sayi1 = input("Birinci Sayıyı girin:")
    sayi2 = input("İkinci Sayıyı girin:")
    islemler = ["+", "-", "*", "/"]
    # eval içerisinde yazılı olan metni bir komut gibi çalıştırmamıza imkan sağlıyor
    print(eval(sayi1 + islemler[islem - 1] + sayi2))
    if islem == "q":
        os.system('cls' if os.name == 'nt' else 'clear')
        break
