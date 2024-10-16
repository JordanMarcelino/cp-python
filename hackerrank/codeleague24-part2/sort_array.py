n = input()
arr = list(map(int, input().split()))

for i in range(len(arr)):
    for j in range(0, len(arr) - i - 1):
        if arr[j] > arr[j + 1]:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]

    if i != len(arr) - 1:
        print(" ".join(list(map(str, arr))))
