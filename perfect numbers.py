def perfect_number(N):
    i = 1
    top = 0
    while i < N:
        if N % i == 0:
            top += i
        i += 1

    if top == N:
        print(f"{N} bir perfect number'dır.")

    else:
        print(f"{N} bir perfect number değildir.")

perfect_number(28)