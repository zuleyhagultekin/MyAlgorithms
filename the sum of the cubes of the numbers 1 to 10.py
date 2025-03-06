#1'den 10'a kadar olan sayıların küplerinin toplamı

i = 1
toplam = 0
for i in range(1,11):
    toplam += i**3

print(toplam)