# 1 ila 100 arasındaki çift sayıların toplamının mükemmel sayı olup olmadığını bulan program.
cift = []
for sayı in range(101):
    if sayı % 2 == 0:
        cift.append(sayı)
cift_toplam = sum(cift)
print(cift_toplam)
i = 1
son_toplam = 0
while i < cift_toplam:
    if cift_toplam % i == 0:
        son_toplam += i
    i += 1
print(son_toplam)
if son_toplam == cift_toplam:
    print("mükemmel sayı")
else:
    print("mükemmel değil")