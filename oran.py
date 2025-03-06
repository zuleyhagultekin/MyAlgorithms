#klavyeden girilen 20 adet sayıdan çift sayıların toplamının tek sayıların toplamına oranına bulan program.

tek = 0
cift = 0
i = 1

for i in range(20):
    sayı = int(input("sayı: "))
    if sayı % 2 == 0:
        cift = cift + sayı
    else:
        tek = tek + sayı

    oran = cift / tek

print(oran)