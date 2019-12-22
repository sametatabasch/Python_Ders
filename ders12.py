import os
while True:
    print(("*" * 50))
    print("* 1 - Toplama ".ljust(49), "*", sep="")
    print("* 2 - Çıkartma ".ljust(49), "*", sep="")
    print("*", " 3 - Çarpma ".ljust(48), "*", sep="")
    print("*", " 4 - Bölme ".ljust(48), "*", sep="")
    print("*", " q- Çıkış  ".ljust(48), "*", sep="")
    print(("*" * 50))

    islem = input("Yapmak istediğiniz işlem: ")
    if islem == "1":
        sayi1 = int(input("Birinci Sayıyı girin:"))
        sayi2 = int(input("İkinci Sayıyı girin:"))
        print(sayi1 + sayi2)
        input("devam etmek için bir tuşa basın...")
        os.system('cls' if os.name == 'nt' else 'clear')
    elif islem == "2":
        sayi1 = int(input("Birinci Sayıyı girin:"))
        sayi2 = int(input("İkinci Sayıyı girin:"))
        print(sayi1 - sayi2)
        input("devam etmek için bir tuşa basın...")
        os.system('cls' if os.name == 'nt' else 'clear')
    elif islem == "3":
        sayi1 = int(input("Birinci Sayıyı girin:"))
        sayi2 = int(input("İkinci Sayıyı girin:"))
        print(sayi1 * sayi2)
        input("devam etmek için bir tuşa basın...")
        os.system('cls' if os.name == 'nt' else 'clear')
    elif islem == "4":
        sayi1 = int(input("Birinci Sayıyı girin:"))
        sayi2 = int(input("İkinci Sayıyı girin:"))
        print(sayi1 / sayi2)
        input("devam etmek için bir tuşa basın...")
        os.system('cls' if os.name == 'nt' else 'clear')
    elif islem == "q":
        os.system('cls' if os.name == 'nt' else 'clear')
        break
