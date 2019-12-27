def asalMi(s):
    asal = True

    for i in range(2, s, 1):
        if s % i == 0:
            asal = False
            break
    return asal

def faktoriyel(s):
    carp = 1
    for i in range(1,s+1):
        carp *=i

    return carp

for i in range(1,51):
   if i % 2 == 0:
       print(i,"Sayısının Faktöriyeli=",faktoriyel(i))
   else:
       if asalMi(i):
           print(i,"sayisi asal bir sayidir")
       else:
           print(i,"Asal değildir")
