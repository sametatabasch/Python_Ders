'''
Kullanıcıdan cinsiyetini ve yaşını aldıktan sonra eğer yaşı 20 den büyük ve cinsiyeti erkek ise "askere gitmelisin "
değilse "şimdilik askere gitmene gerek yok" mesasını yazdıran programın akış diyagramı ve algoritmasını yazın.

1 Başla
2 yas, cins
3 Sayı Al "Yaşınız: ", yas
4 Al "Cinsiyet (erkek/kadın):", cins
5 Eğer yas>20 and cins=="erkek" ise Yaz "Askere Gitmelisin"
6 değilse Yaz "Şimdilik askere gitmene gerek yok"
7 Bitir
'''

cins = input("Cinsiyet (erkek/kadın):")
cins = cins.strip()
if cins == "kadın" or cins == "Kadın" or cins == "K":
    print("Askere gidemezsin")
elif cins == "erkek" or cins == "Erkek"or cins == "E":
    yas = int(input("Yaşınızı Giriniz:"))
    if yas >= 20 and yas<=35:
        print("Askere Gitmelisin")
    elif yas>35:
        print("Askere gitmek için çok geç")
    else:
        print("Askere gitmek için biraz daha beklemelisin")
