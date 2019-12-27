'''
Aşağıdaki kurallara göre Askere gitme durumunu belirleyen program
k1- Cinsiyet kadın ise "Askere gidemezsin" mesajı yazılacak
k2- Cinsiyet erkek ise kullanıcıdan yaşı istenecek
k3- yaş 20 ile 35 arasında ise "Askere Gitmelisin" mesajı yazılacak
k4- yaş 35 den büyük ise "Askere gitmek için çok geç" mesajı yazılacak
k5-  yaş 20 den küçük ise "Askere gitmek için biraz daha beklemelisin" mesajı yazılacak

1 Başla
2 Al "Cinsiyet (erkek/kadın):", cins
3 cins = cins.strip()
4 Eğer cins == "kadın" or cins == "Kadın" or cins == "K" ise Yaz "Askere gidemezsin"
5 Eğer değilse cins == "erkek" or cins == "Erkek" or cins == "E" ise
    6 Sayı Al "Yaşınızı Giriniz:", yas
    7 Eğer yas >= 20 and yas <= 35 ise Yaz "Askere Gitmelisin"
    8 Eğer Değilse yas > 35 ise Yaz "Askere gitmek için çok geç"
    9 Değilse Yaz "Askere gitmek için biraz daha beklemelisin"
10 Bitir
'''

cins = input("Cinsiyet (erkek/kadın):")
cins = cins.strip()
if cins == "kadın" or cins == "Kadın" or cins == "K":
    print("Askere gidemezsin")
elif cins == "erkek" or cins == "Erkek" or cins == "E":
    yas = int(input("Yaşınızı Giriniz:"))
    if yas >= 20 and yas <= 35:
        print("Askere Gitmelisin")
    elif yas > 35:
        print("Askere gitmek için çok geç")
    else:
        print("Askere gitmek için biraz daha beklemelisin")
