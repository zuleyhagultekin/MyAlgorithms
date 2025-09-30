#1-100 arasında rastgele üretilecek bir sayıyı aşağı yukarı ifadeleri ile buldurmaya çalışın.(hak=5)
## 'random modülü' için "python random" şeklinde arama yapın.
## 100 üzerinden puanlama yapın.Her soru 20 puan.

import random

sayi = random.randint(1,10)
hak=5
sayac =0

while hak>0:
    hak-=1
    sayac += 1
    tahmin=int(input("Tahmininiz:"))

    if(tahmin == sayi):
        print(f"tebrikler!{sayac}. denemede doğru bildiniz.Puanınız:{100-(20*(sayac-1))}")
        break
    elif (sayi > tahmin):
        print("Yukarı")
    else:
        print("Aşağı")
    if(hak == 0):
        print(f"hakkınız bitti.Tutulan sayı: {sayi}")