n = int(input())

moras = [1, 2, 5, 10, 20, 50, 100]

results = []
num = 0

while n > 0:
    for i in range(len(moras) - 1, -1, -1):
        if moras[i] <= n:
            n -= moras[i]
            num += 1
            if str(moras[i]) not in results:
                results.append(str(moras[i]))
            break

print(num)
print(" ".join(results))
