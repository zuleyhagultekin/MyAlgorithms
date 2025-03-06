#faktoriyel

sayı = int(input("sayı: "))
faktoriyel = 1

for i in range(1,sayı+1):
    faktoriyel *= i

print(f"{sayı}! = {faktoriyel} dir. ")