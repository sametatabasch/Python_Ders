import math # matematik fonksiyonlarını ugulamada kullanabilmek için math kütüphanesini ekliyoruz
'''
Öğenci vize notunu girdikten sonra dersi geçmek(50) için alması gereken notu yazan program
'''
vize = 100
while vize >= 0 and vize <= 100:
    vize = int(input("Vize Notunuz:"))
    final = 0

    final = math.ceil((40 - vize * 0.4) / 0.6)
    if final < 40:
        final = str(final)+" alman yetiyor ama kuralar gereği 40 "
    print("Geçmek için en az ", final, "almalısın")
