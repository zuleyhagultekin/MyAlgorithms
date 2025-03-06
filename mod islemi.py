#pozitif girilen sayının istenilen sayıya göre mod işlemini yaptıran program.
sayı1 = int(input("sayı1: "))
sayı2 = int(input("sayı2: "))

if sayı1 >= sayı2:
    while sayı1 >= sayı2:
        sayı1 = sayı1-sayı2

print(sayı1)