#klavyeden girilen 25 adet sayıdan negatif olanların toplamını,çift olanların toplamını,7'ye eşit olanların adetini bulup ekrana yazdıran program.
sayılar = []
cift = 0
negatif = 0
esit = 0
i = 1
for i in range(25):
    sayı = int(input("sayı: "))
    sayılar.append(sayı)
    if sayı < 0:
        negatif += sayı
    if sayı % 2 == 0:
        cift += sayı
    if sayı == 7:
        esit += 1

print(esit)
print(cift)
print(negatif)
