def faktoriyel(n):
    fak = 1
    for i in range(1,n+1):
        fak *= i
        i += 1
    return fak
n = int(input("n: "))
faktoriyel(n)
print(faktoriyel(n))