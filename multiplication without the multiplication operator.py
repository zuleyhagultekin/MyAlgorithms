#çarpma işlemi kullanmadan iki sayıyı çarpan program.
sayac = 0

sayı1 = int(input("sayı1: "))
sayı2 = int(input("sayı2: "))

sayac = sayac + sayı1

if sayı2 == 1:
    sayac = sayac + sayı1

else:
      for i in range(1,sayı2):
        sayı2 -= 1
        sayac = sayac + sayı1

print(sayac)