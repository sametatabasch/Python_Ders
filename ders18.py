def asalMi(s):
    asal = True
    if s < 2: return False
    for i in range(2, s, 1):
        if s % i == 0:
            asal = False
            break
    return asal
for i in range(1, 51):
    if asalMi(i):
        print(i)