#tam sayı bölmesi yapan program.
bolunen = int(input("bolunen: "))
bolen = int(input("bolen: "))

if bolen == 0:
    print("bir sayıyı sıfıra bölemezsiniz")

sayac = 0
while bolunen >= bolen:
    bolunen -= bolen
    sayac += 2

print(sayac)