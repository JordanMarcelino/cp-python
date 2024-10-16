n = int(input())


for i in range(n):
    for j in range(n - i - 1):
        print(" ", end="")

    if i % 2 == 0:
        for j in range(i * 2 + 1):
            print("*", end="")
    else:
        for j in range(i + 1):
            print("* ", end="")

    print()
