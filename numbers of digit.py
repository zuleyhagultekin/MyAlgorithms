#girilen pozitif sayının kaç basamaklı olduğunu gösteren program.

sayı = int(input("sayı: "))
sayac = 1

if sayı <= 9:
    print(sayac)

else:
    while sayı > 9:
        sayı = sayı // 10
        sayac += 1
    print(sayac)