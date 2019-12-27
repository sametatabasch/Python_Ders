import time

def asalMi(s):
    asal = True

    for i in range(2, s, 1):
        if s % i == 0:
            asal = False
            break
    return asal


bas = time.time()
for i in range(2, 1000000):
    if asalMi(i):
        print(i)
bitis = time.time()
print("Bu işlem", bitis - bas, "saniye sürdü")
