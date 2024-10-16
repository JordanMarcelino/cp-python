def ways(n):
    if n == 1:
        return 1, [[1]]
    elif n == 2:
        return 1, [[1, 2]]
    elif n == 3:
        return 1, [[1, 2, 3]]
    elif n == 4:
        return 2, [[1, 2, 3, 4], [1, 4]]
    else:
        dp_count = [0] * (n + 1)
        dp_paths = [[] for _ in range(n + 1)]

        dp_count[1] = 1
        dp_paths[1] = [[1]]

        dp_count[2] = 1
        dp_paths[2] = [[1, 2]]

        dp_count[3] = 1
        dp_paths[3] = [[1, 2, 3]]

        dp_count[4] = 2
        dp_paths[4] = [[1, 2, 3, 4], [1, 4]]

        for i in range(5, n + 1):
            dp_count[i] = dp_count[i - 1] + dp_count[i - 3]
            dp_paths[i] = [path + [i] for path in dp_paths[i - 1]] + [
                path + [i] for path in dp_paths[i - 3]
            ]

        return dp_count[n], dp_paths[n]


n = int(input())

count, paths = ways(n)
print(count)

paths.sort(key=lambda x: (-len(x), x))
for path in paths:
    print("-".join(map(str, path)))
