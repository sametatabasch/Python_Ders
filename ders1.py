'''
Değişken Tanımlama veri atama

Değişken ismini seçerken uyulamsı gereken kurallar
1- Türkçe karakter kullanılmaz
2- Boşluk, sembol özel karakter olmayacak sadece _ kullaılabilir
3- Rakam kullanılabilir fakat rakam ile başlayamaz
4- Programlama dilinde kullanımda olan kelimeler kullanılmaz
'''

# Python büyük küçük harf duyarlıdır.
degisken = 5

Degisken = 8

print(degisken + Degisken)  # 13

degisken = 3  # tekrar değer atadığımızda eski değer silinir yeni değer aktif olur

elma = 5

armut = 7

print(degisken + elma)  # 8
print(elma * armut)  # 35
print(elma ** 2)  # 25
print(Degisken ** (1 / 3))  # 2

meyve = "Muz"

print(meyve * 3)  # MuzMuzMuz

ondalikli = 5.6

print(type(degisken))  # <int>
print(type(meyve))  # <str>
print(type(ondalikli))  # <float>

print(meyve + "Co") # MuzCo
print(meyve, "Co") #Muz Co
'''sep parametresi diğer parametrelerdeki
 metinler birleştirilirke araya eklenecek karakteri belirler'''
print(meyve, "Co", sep="-") #Muz-Co
'''
end parametresi print fonksiyonunun çıktısındaki son karakteri belirler
ön tanımlı olarak \n (enter)olduğu için her print yeni satırda yazar
'''
print(meyve, end="")
print("Armut")
# üsteki iki satırın çıktısı= MuzArmut
